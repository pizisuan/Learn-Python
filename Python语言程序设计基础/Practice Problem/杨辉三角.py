#杨辉三角

def triangles(n):
	row = []
	if n == 1:
		row = [1]
	elif n == 2:
		row = [1,1]
	else:
		temp = triangles(n-1)
		row = [1]+[temp[i]+temp[i+1] for i in range(len(temp)-1)]+[1]
	return row

for i in range(1,11):
	print(triangles(i))


# 结果
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]