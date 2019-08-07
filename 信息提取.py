import requests
import re
from bs4 import BeautifulSoup
r  = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
'''
for tag in soup.find_all(re.compile('b')):
	print (tag.name)
print (soup.find_all(id = 'link1'))

#正则表达式找link
print (soup.find_all(id = re.compile('link')))
'''
#正则表达式查找string
#soup.find_all() = soup()
print (soup(string = re.compile("python")))

