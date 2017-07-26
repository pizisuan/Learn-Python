#加密程序
plaincode = input("请输入明文：")
for p in plaincode:
	if ord("a") <= ord(p) <= ord("z"):
		print(chr(ord("a") + (ord(p) - ord("a") + 3)%26),end = '')
	else:
		print(p,end='')


#解密程序
print("\n")
ciphertext = input("请输入密文：")
for c in ciphertext:
	if ord("a") <= ord(c) <= ord("z"):
		print(chr(ord("a") + (ord(c) - ord("a") - 3)%26),end = '')
	else:
		print(c,end='')
