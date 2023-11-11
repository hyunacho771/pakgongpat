from pwn import *
import time
JOKER="\x5f\x75\x43\x30\x6e\x5f"

token=int(time.time())

pwd=JOKER+'_'+str(token)

p=process(['./darim', pwd])

p.interactive()

