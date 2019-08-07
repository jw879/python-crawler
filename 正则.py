import re

# search函数的使用
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
	print (match.group(0)) #.group(0) = 获得匹配后的字符串

# match 函数的使用
match = re.search(r'[1-9]\d{5}', '100081')
if match:
	print (match.group(0))

# findall
ls = re.findall(r'[1-9]\d{5}', '100081')
print (ls)

# split， 将匹配到的字符串去掉，返回一个列表
sp = re.split(r'[1-9]\d{5}', 'bit100081 tsu100084')
print (sp)
# 最大分割几次
maxsp = re.split(r'[1-9]\d{5}', 'bit100081 tsu100084', maxsplit = 1)
print (maxsp)

# finditer
for m in re.finditer(r'[1-9]\d{5}', 'qwe100081 asd100084'):
	if m:
		print (m.group(0))

# sub替换函数
sub = re.sub(r'[1-9]\d{5}', ':zipcode', 'qwe242000, asd243000')
print (sub)  

# 面向对象调用法，先对对象进行编译，后面直接调用
regex = re.compile(r'[1-9]\d{5}')
exp = regex.search('qwe245000')
print (exp)

