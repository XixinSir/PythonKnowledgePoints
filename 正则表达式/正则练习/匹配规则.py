import re

"""
.              匹配换行符以外的任意一个字符
[]             匹配方括号中所包含的任意一个字符
^              脱字符,表示不匹配集合中的字符
\d             匹配数字,效果同[0-9]
\D             匹配非数字字符,效果同[^0-9]
\w             匹配数字,字母,下划线 [0-9a-zA-Z]
\W             匹配非数字，字母和下划线  效果同[^0-9a-zA-Z_]
\s             匹配任意的空白符(空格、换行、回车、换页、制表)，效果同[\f\n\r\t]
\S             匹配任意的非空白符，效果同[^\f\n\r\t]

"""

print("---------------------------------------------------------------------------------")
print(re.search("[^0-9]","sunck is a good man"))
# *匹配任意多个  0个也能匹配到
print(re.search("(\d)*","sunck is a good man 5555"))
# 非贪婪匹配
print(re.search("\d.*?","sunck is a good man 5555"))
# 贪婪匹配
print(re.search("\d.*","sunck is a good man 5555"))
# 匹配非数字
print(re.search('\D','sunck is a good man'))


print("---------------------错字符(边界字符)--------------------------")
'''
^       行首匹配                 每一行都匹配
$       行尾匹配                  
\A      匹配字符串开始,和^的区别,\A只匹配整个字符串的开头,即使在re.M模式下也不会匹配他行的行首
\Z      匹配字符串结束,和^的区别,\A只匹配整个字符串的结束,即使在re.M模式下也不会匹配他行的行首
\b      匹配一个单词的边界,就是指单词和空格间的位置     "er\b"可以匹配never,不能匹配nerve
\B      匹配非单词边界
'''


print("---------------------------------------------------------------------------------------")

print(re.search("^sunck", "sunc is a good man\nsunck is a good man"))
print(re.search("^sunck", "sunc is a good man\nsunck is a good man", re.M))
print(re.search("\Asunck", "sunc is a good man\nsunck is a good man"))
print(re.search("\Asunck", "sunc is a good man\nsunck is a good man", re.M))

print("---------------------------------------------------------------")
# 注意体会这两者的区别
print(re.search('er\b', "give up neVer"))
print(re.search(r'er\b', "give up neVer"))

print(re.search('er\B', "give up nerve"))
print(re.search(r'er\B', "give up nerve"))

print("---------------------匹配多个字符--------------------------")
"""
下方的X、Y、Z均为假设的普通字符,不是正则表达式的元字符
 (xyz)        匹配小括号内的xyz(作为一个整体去匹配)
  x?          匹配0个或1个x
  x*          0个或任意多个
  x+          至少一个
  x{n}        匹配确定的n个x(n是一个非负整数)
  x{n,}       匹配至少n个x
  x{n,m}      m匹配至少n个  最多m个x   n<=m
  x|y         |表示或  匹配的是x或y
"""
print(re.findall(r"(sunck)",'sunck is a good man,sunck is a good man '))
print(re.findall(r"^(sunck)",'suncksunck is a good man,\nsunck is a good man',re.M))
print(re.findall(r"o?",'gbood man,\nsunck is a good man'))
print("-------------------------------------------------------------------------------")
print(re.findall(r"a?", 'aaa'))
print(re.findall(r"a*",'aaa'))
print(re.findall(r"a*","aabbbaaa"))  # 要注意为什么会出现这种结果

print(re.findall(r"a+","aaaa"))
print(re.findall(r"a+","aaaabbbbaaaa"))


print("-----------------------------------------------")
print(re.findall(r"a{3}","1424aaaa423"))
print(re.findall(r"a{3,6}","1424aaaa423"))
print(re.findall(r"a{3,}","1424aaaa423"))
print(re.findall(r"a{3,}?","1424aaaa423"))

