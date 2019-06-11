import re
# pip 包管理工具
"""
re.match函数
原型:match(pattern,string,flags=0)
patter:匹配的正则表达式
string:要匹配的字符串
flags: 标志位,用于控制正则表达式的匹配方式
re.I  忽律大小写
re.L  做本地户识别
re.M  多行匹配,影响^和$
re.S  使.匹配包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符,影响\w   \W  \b  \B
re.X  使我们更灵活的方式理解正则表达式


参数:匹配的正则表达式
功能:尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,返回None#注意是起始位置
"""

# re.match扫描整个字符串,返回从起始位置匹配成功的匹配
# www.baidu.com
print(re.match("www","www.baidu.com"))  # 返回的是对象
print(re.match("www","www.baidu.com").span())
print(re.match("www","ww.baidu.com"))
print(re.match("www","baidu.wwwdu.com"))

print("---------re.I的作用----------------")
print(re.match("www","wwW.baidu.com"))
print(re.match("www","wwW.baidu.com",flags=re.I))

print("---------------------re.search函数-------------------------")
"""
re.search函数
原型:serrch(pattern,string,flags=0)

patter:匹配的正则表达式
string:要匹配的字符串
flags: 标志位,用于控制正则表达式的匹配方式
参数:匹配的正则表达式

功能:扫描整个字符串,并返回第一个成功的匹配
"""
print(re.search("www","www.baidu.com").span())
print(re.search("www","baidu.www.com"))

print("--------------------re.findall-------------------------")
"""
re.findall函数
原型:findall(pattern,string,flags=0)

参数:匹配的正则表达式
patter:匹配的正则表达式
string:要匹配的字符串
flags: 标志位,用于控制正则表达式的匹配方式

功能:扫描整个字符串,并返回结果列表
"""
print(re.findall("sunck","sunck is a good man!good man is sunck! Sunck sunck good man ",flags=re.I))

