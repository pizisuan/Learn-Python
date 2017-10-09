"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

"""

def normalize(name):
	s = name[0].upper()
	i = 1
	while i < len(name):
		s = s + name[i].lower()
		i = i + 1
	return s

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)