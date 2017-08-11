import requests
from bs4 import BeautifulSoup

allUniv = []

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = "utf-8"
		return r.text
	except:
		return ""

def fillUnivList(soup):
	data = soup.find_all("tr")
	for tr in data:
		ltd = tr.find_all("td")
		if len(ltd) == 0:
			continue
		singleUniv = []
		for td in ltd:
			singleUniv.append(td.string)
		allUniv.append(singleUniv)

def printUnivList(num):
	print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),"排名","学校名称","省市","总分","培养规模"))
	for i in range(num):
		u = allUniv[i]
		print("{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8}{5:{0}^10}".format(chr(12288),u[0],u[1],u[2],eval(u[3]),u[6]))

def main(num):
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
	html = getHTMLText(url)
	soup = BeautifulSoup(html,"html.parser")
	fillUnivList(soup)
	printUnivList(num)

main(10)

# 结果：
# 排名　　　学校名称　　　　　省市　　　总分　　　　培养规模　　　
#  1  　　　清华大学　　　　北京市　　　95.9　　　　37342　　　
#  2  　　　北京大学　　　　北京市　　　82.6　　　　36137　　　
#  3  　　　浙江大学　　　　浙江省　　　　80　　　　41188　　　
#  4  　　上海交通大学　　　上海市　　　78.7　　　　40417　　　
#  5  　　　复旦大学　　　　上海市　　　70.9　　　　25519　　　
#  6  　　　南京大学　　　　江苏省　　　66.1　　　　20722　　　
#  7  　中国科学技术大学　　安徽省　　　65.5　　　　18507　　　
#  8  　哈尔滨工业大学　　黑龙江省　　　63.5　　　　25249　　　
#  9  　　华中科技大学　　　湖北省　　　62.9　　　　23503　　　
#  10 　　　中山大学　　　　广东省　　　62.1　　　　23837　
