import re

match = re.search(r'PY.*N', 'PYANBNCNDN')
#贪婪匹配：默认返回匹配最长的字符串
print (match.group(0)) 

match1 = re.search(r'PY.*?N', 'PYANBNCNDN')
#最小匹配：默认返回匹配最短的字符串
print (match1.group(0)) 