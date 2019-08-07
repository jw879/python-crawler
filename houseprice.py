import requests
import io
import sys
from bs4 import BeautifulSoup
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='ISO-8859-1')

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status
		return r.text
	except:
		return "gg"

def parsePage(ilt, html):
	try:
		html = getHTMLText(url)
		soup = BeautifulSoup(html, 'html.parser')
		
	pass

def pringHouseList(ilt):
	pass


def main():
	depth = 2
	start_url = 'https://www.rightmove.co.uk/house-prices/Cardiff.html?country=england&locationIdentifier=REGION%5E281&searchLocation=Cardiff'
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&index=' + str(25*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printHouseList(infoList)

main()
