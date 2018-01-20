# 程序需要采用自顶向下的设计方法，采用自底向上的执行方法

from random import random

def printIntro():
	print("这个程序模拟两个选手A和B的某种竞技比赛")
	print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getInputs():
	a = eval(input("输入选手A的能力值（0-1）："))
	b = eval(input("输入选手B的能力值（0-1）："))
	n = eval(input("模拟比赛的场次："))
	return a,b,n

def simNGames(n,probA,probB):
	winsA, winsB = 0, 0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA,probB)
		if scoreA > scoreB:
			winsA += 1
		else:
			winsB += 1
	return winsA, winsB

def gameOver(a,b):
	return a == 15 or b == 15

def simOneGame(probA,probB):
	scoreA, scoreB = 0, 0
	serving = 'A'
	while not gameOver(scoreA,scoreB):
		if serving == 'A':
			if random() < probA:
				scoreA += 1
			else:
				serving = 'B'
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = 'A'
	return scoreA, scoreB

def printSummary(winsA, winsB):
	n = winsA + winsB
	print("竞技分析开始，共模拟{}场比赛".format(n))
	print("选手A获胜了{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
	print("选手B获胜了{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)

main()

# 结果：
# 这个程序模拟两个选手A和B的某种竞技比赛
# 程序运行需要A和B的能力值（以0到1之间的小数表示）
# 输入选手A的能力值（0-1）：0.45
# 输入选手B的能力值（0-1）：0.5
# 模拟比赛的场次：1000
# 竞技分析开始，共模拟1000场比赛
# 选手A获胜了392场比赛，占比39.2%
# 选手B获胜了608场比赛，占比60.8%
