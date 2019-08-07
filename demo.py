import requests
import io
import sys
from bs4 import BeautifulSoup
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='ISO-8859-1')

url = "https://www.rightmove.co.uk/house-prices/Cardiff.html"

r  = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
try:
	taglist = soup.find_all('tr', attrs={'class': False}) 
	for trtag in taglist:
		sp = trtag.find('td', 'soldPrice')  #在每个tr标签下,查找所有的td标签
		st = trtag.find('td', 'soldType')
		sd = trtag.find('td', 'soldDate')
		nb = trtag.find('td', 'noBed')
		print (sp.string)
		print (st.string) 
		print (sd.string) 
		print (nb.string)    
except:
	print ("")