import requests
from bs4 import BeautifulSoup
import traceback
import re

#获取网站页面
def getHTMLText(url, code = 'utf-8'):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return "gg"

#获得股票列表
def getStockList(lst, stockURL):
	html = getHTMLText(stockURL, 'GB2312')
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')#利用soup发现列表中所有a标签
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
		 	continue	

#处理每个股票的信息
def getStockInfo(lst, stockURL, fpath):
	count = 0
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html == "":
				continue
			infoDict = {}
			soup = BeautifulSoup(html, 'html.parser')
			stockInfo = soup.find('div', attrs={'class':'stock-bets'})
			if isinstance(stockInfo,bs4.element.Tag):
				name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
				infoDict.update({'股票名称': name.text.split()[0]})

			#股票所有相关键值对的列表
			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd') 
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val

			with open(fpath, 'a', encoding = 'utf-8') as f:
				f.write(str(infoDict) +  '\n')
				count = count + 1
				print('\rloading: {:.2f}%'.format(count*100/len(lst)), end ='')
		except:
			count = count + 1
			print('\rloading: {:.2f}%'.format(count*100/len(lst)), end ='')
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
	stock_info_url = 'http://gupiao.baidu.com/stock/'
	output_file = 'G://BaiduStockInfo.txt'
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()