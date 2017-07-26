import jieba
txt = open("三国演义.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
	if len(word) == 1:
		continue
	else:
		counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word, count)) 

# 结果如下：
# 曹操          936
# 孔明          831
# 将军          772
# 却说          656
# 玄德          570
# 关公          509
# 丞相          491
# 二人          466
# 不可          441
# 荆州          421
# 不能          387
# 孔明曰        385
# 玄德曰        383
# 如此          378
# 张飞          348
