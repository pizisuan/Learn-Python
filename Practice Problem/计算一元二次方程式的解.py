"""
问题描述：
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的解
提示：计算平方根可以调用math.sqrt()函数

"""

import math
def quadratic(a,b,c):
	if a == 0:  #转变为一次方程：bx + c = 0
		if b == 0:
			if c == 0:
				return "方程为恒等式 0 = 0, 故存在无数解"
			else:
				return "方程为矛盾方程 c = 0, 故方程无解"
		else:
			return -c/b
	else:
		delta = b*b - 4*a*c
		if delta < 0:
			return "方程无实数根"
		elif delta == 0:
			return "方程存在两个相同的实根：%f"%(-b/(2*a))
		else:
			return "方程存在两不同的实根：%f,%f"%((-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a))

print(quadratic(0,0,0))
print(quadratic(0,0,3))
print(quadratic(1,2,1))
print(quadratic(1,4,2))
print(quadratic(3,1,2))
