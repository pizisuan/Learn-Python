"""
Python提供的sum()函数可以接受一个list并求和。
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""

from functools import reduce
def prod(L):
	def multiply(a,b):
		return a*b
	return reduce(multiply,L)
#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))