# 文本文件与二进制文件的区别

textFile = open("7.1.txt","rt")
print(textFile.readline())
textFile.close()

binFile = open("7.1.txt","rb")
print(binFile.readline())
binFile.close()

# 结果：
# 中国是一个伟大的国家
# b'\xd6\xd0\xb9\xfa\xca\xc7\xd2\xbb\xb8\xf6\xce\xb0\xb4\xf3\xb5\xc4\xb9\xfa\xbc\xd2'


# 文本文件逐行打印

fname = input("请输入要打开的文件：")
fo = open(fname, "r")
for line in fo:
	print(line)
fo.close()


# 向文件写入一个列表

fname = input("请输入要写入的文件：")
fo = open(fname, "w+")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
	print(line)
fo.close()
