fo = open("price2016.csv","r")
ls = []
for line in fo:
	line = line.replace("\n","")
	ls = line.split(",")
	lns = ""
	for s in ls:
		lns += "{}\t".format(s)
	print(lns)
fo.close()


# 结果：
# 城市	环比	同比	定基	
# 北京	101.5	120.7	121.4	
# 上海	101.2	127.3	127.8	
# 广州	101.3	119.4	120	
# 深圳	102.6	140.9	145.5
