#http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html
import requests
from bs4 import BeautifulSoup
import bs4

#找到大学信息的网页文本内容
def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

#用beautifulsoup来提取需要的信息的位置以及标签属性
def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
#找到位置后利用循环来提取相应内容（遍历）
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])


#将提取到的信息正确的打印出来
def printUnivList(ulist, num):
#利用中文空格进行排版：
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^9}"
	print (tplt.format("排名", "学校名称", "总分", chr(12288)))
	for i in range(num):
		u = ulist[i]
		print (tplt.format(u[0], u[1], u[2], chr(12288)))

#main函数：
def main():
	unifo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	html = getHTMLText(url)
	fillUnivList(unifo, html)
	printUnivList(unifo, 20) #只例举前20所大学
main ()
