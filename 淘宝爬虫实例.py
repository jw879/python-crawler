import requests
import re
#获得页面的函数：

def getHTMLText(url):
    kv = {'cookie':'thw=gb; cna=9B9qFPq+/VwCAR/NRvsjrVdg; hng=GLOBAL%7Czh-CN%7CUSD%7C999; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=qd9CefkfWC%2F0x6iwPSI6houZqEsCxtVNMGOBAM%2Fw6IAUW2ligv4p4uqg69St6e894yT3SZh8qWo6ijWt9vTu6w%3D%3D; miid=270358422071057433; t=a2bb767d653e103a8d77e1dbf6f78300; cookie2=10fcfcc6e6e3811122c0416507a9564e; _tb_token_=78e53353b303e; _m_h5_tk=a0506e7a4e27051510fe8bd0f90190ce_1563149031864; _m_h5_tk_enc=01340c54d723731fbcaad8c26b274606; _fbp=fb.1.1563140407653.1790332102; alitrackid=world.taobao.com; swfstore=108302; _cc_=W5iHLLyFfA%3D%3D; lastalitrackid=login.taobao.com; v=0; unb=2188920924; sg=%E8%AE%BA4c; _l_g_=Ug%3D%3D; skt=1622bd8104e33e0b; cookie1=UtfU5%2BFLrQ8oNCsYK73yUQw21gP%2FZG821D3zN2gp8OM%3D; csg=04d9d324; uc3=vt3=F8dBy3%2F%2F3wD30yU5GxA%3D&id2=UUkGWzPsFSbWxw%3D%3D&nk2=0XnmPP%2FpauY%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU2MzE0Nzc3Nw%3D%3D; tracknick=%5Cu4E0D%5Cu8981%5Cu8BAE%5Cu8BBA; lgc=%5Cu4E0D%5Cu8981%5Cu8BAE%5Cu8BBA; dnk=%5Cu4E0D%5Cu8981%5Cu8BAE%5Cu8BBA; _nk_=%5Cu4E0D%5Cu8981%5Cu8BAE%5Cu8BBA; cookie17=UUkGWzPsFSbWxw%3D%3D; mt=ci=9_1; JSESSIONID=9CC1D3CD8E1B6F0745508E6D1930C9DD; l=bBPBY0GmvMevj7OEBOCiCZ6PIEQOkIRAguWbrWDpi_5IY1L_eh_Okcx6Qep6Vx5RsoLB4s6vWje9-etus; isg=BCoqhJGyA84S2IlhwfGf7olse5DGfefDXA71drTjpn0I58qhnCv-BX-dd0PeFyaN; uc1=cookie14=UoTaG770NqPnOQ%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=VT5L2FSpczFp&tag=8&cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0; whl=-1%260%260%261563148945472',
          'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


#对获得的页面进行解析：
def parsePage(ilt, html):
	try:#正则表达式提取商品和价格信息
		plt = re.findall(r'\"view_price\"\:"[\d.]*"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		#通过循环来分割提取商品和价格冒号后面的信息
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print("parse_page({})异常".format(page))

#将淘宝的商品信息输出到屏幕上：
def printGoodList(ilt):
	#调整每个列表名称的长度
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号", "价格","商品名称"))
	count = 0
	for g in ilt:
		count = count + 1 
		print(tplt.format(count, g[0], g[1]))
	

#主函数
def main():
	goods = '书包'
	depth = 2
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodList(infoList)

main()