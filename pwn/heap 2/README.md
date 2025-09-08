# heap 2

Author: Abrxs, pr1or1tyQ

Can you handle function pointers? Download the binary [here](chall). Download the source [here](chall.c). Connect with the challenge instance here: `nc mimas.picoctf.net 55843`

## Solution

Same as heap 1 but we overwrite the variable `x` now with the address of the `win` function. Its compiled without PIE so the address is the same as on our system.

```c
void check_win() { ((void (*)())*(int*)x)(); }
```
