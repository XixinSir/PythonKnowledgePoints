import re

"""
re.search:   search(pattern, string, flags=0)
pattern: 匹配的正则表达式
string: 要匹配的字符串
flags: 标志位,用于控制正则表达式的匹配方式
参数: 扫描整个字符串,并返回第一个成功的匹配
"""

# re.search只匹配一个(在字符串的任何位置都可以)  如果字符串有多个,只匹配第一个
print(re.search("www", "www.baidu.com"))
print(re.search("www", "baidu.www.com"))
print(re.search("www", "www.baidu.www.com"))
print(re.search("wWw", "www.baidu.www.com", re.I))
print(re.search("wWw", "www.baidu.www.com", re.I).span())
print(re.search('^w.*', "www.baidu.com"))

"""
re.match  类似上面
只是匹配起始位置的  
"""
print("------------------------------------------------------------")
print(re.match("www", 'www.bai.com'))
print(re.match("www", 'bai.www.com'))
print(re.match("www", 'wWwWW.bai.com', re.I).span())

print("-------------------------------------------------------------")
"""
re.findall     扫描整个字符串  并返回结果列表
"""
print(re.findall('sunck', "sunck is a good man,Sunck is a good man", re.I))
