import re
print("-------匹配单个字符与数字---------")
'''
.         匹配换行符以外的任意字符
[0123456789]      []是字符集合,表示匹配方括号中所包含的任意一个字符
[sunck]   匹配s  u  n c  k中任意一个字符
[a-z]     匹配任意小写字母
[A-Z]     匹配任意大写字母
[0-9]     匹配任意数字,类似[0123456789]
[0-9a-zA-Z]  任意数字和字母
[0-9a-zA-Z_]   数字字母下划线
[^sunck]     匹配除了sunck这几个字母以外的所有字符,中括号里的成为脱字符,表示不匹配集合中的字符
[^0-9]       匹配所有的非数字字符

^ 称为脱字符  表示不匹配集合中的字符
\d        匹配数字,效果同[0-9]
\D        匹配非数字字符,效果同[^0-9]
\w        匹配数字，字母和下划线 同[0-9a-zA-Z_]
\W        匹配非数字，字母和下划线  效果同[^0-9a-zA-Z_]
\s        匹配任意的空白符(空格、换行、回车、换页、制表)，效果同[\f\n\r\t]
\S        匹配任意的非空白符，效果同[^\f\n\r\t]
'''
print('---------------------\d的用法--------------------------')
print(re.search("[^0-9]", "sunck is a good man 5"))
print(re.findall("\d*", "sunck is a good man 55555555555"))
print(re.search("\D", "sunck is a good man 5"))
print(re.search("\w", "_sunck is a good man 5"))
print(re.search(".", "sunck is a go\nod man 5", flags=re.S))


print("---------------错字符(边界字符)------------------")
"""
^  行首匹配 和在[]里的^不是一个意思 每一行行首都匹配
$  行尾匹配 
\A 匹配字符串开始,它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z 匹配字符串结束,它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾
\b 匹配一个单词的边界 也就是指单词和空格间的位置  "er\b"可以匹配never,不能匹配nerve
\B 匹配非单词边界
"""
# search只能匹配一个
print(re.search("^sunck","sunck is a good man"))
print(re.search("man$","sunck is a good man"))
print(re.search("man$","man is a good sunck"))
print(re.search("^sunck","man is a good sunck"))
print(re.search("^sunck","sunck is a good man\nsunck is a nice man",re.M))  # 用search只匹配一个
print(re.search("\Asunck","sunck is a good man\nsunck is a nice man",re.M))





print("------------findall--------------")
print(re.findall("^sunck","sunck is a good man\nsunck is a nice man"))
print(re.findall("\Asunck","sunck is a good man\nsunck is a nice man"))
print(re.findall("^sunck","sunck is a good man\nsunck is a nice man",re.M))
print(re.findall("\Asunck","sunck is a good man\n sunck is a nice man",re.M))
print(re.findall("man$","sunck is a good man\nsunck is a nice man",re.M))
print(re.findall("man\Z","sunck is a good man\n sunck is a nice man",re.M))


print("--------------------------------------")
print(re.search(r"er\b","never"))
print(re.search(r"er\b","nerve"))
print(re.search(r"er\B","never"))
print(re.search(r"er\B","nerve"))







print("---------------匹配多个字符-----------------")
"""
说明:下方的x、y、z均为假设的普通字符,不是正则表达式的元字符
(xyz)  匹配小括号内的xyz(作为一个整体去匹配)
x?     匹配0个或者1个x
x*     匹配0个或者任意多个x (*表示匹配0个或者任意多个字符(换行符除外))
x+     匹配至少一个x
x{n}   匹配确定的n个x(n是一个非负整数)
x{n,}  匹配至少n个x
x{n,m} m匹配至少n个 最多mg个x  注意: n<=
x|y    |表示或 匹配的是x或y
"""
print(re.findall(r"(sunck)","sunckgood is a good man,sunck is a good man"))
print(re.findall(r"o?","sunckgood is a good man,sunck is a good man"))  # 结果最后又一个孔大哥的

print(re.findall(r"a?","aaa"))     # 非贪婪匹配 尽可能少的匹配
print(re.findall(r"a*","aaa"))  # 结果又一个空的字符串是结尾
print(re.findall(r"a*","aaabaa")) # 贪婪匹配 尽可能多的匹配

print(re.findall(r"a+","aaa"))
print(re.findall(r"a+","aaabaaaaaaaaaa"))


print(re.findall(r"a{3}","aaa"))
print(re.findall(r"a{3}","aaaa"))
print(re.findall(r"a{3}","aa"))
print(re.findall(r"a{3}","aaabaa"))

print(re.findall(r"a{3,}","aaa"))
print(re.findall(r"a{3,}","aa")) # 贪婪匹配 尽可能多的匹配

print(re.findall(r"a{3,6}","aaaa"))
print(re.findall(r"a{3,6}","aaaaaaa"))
print(re.findall(r"a{3,6}","aaaabaaa"))


print(re.findall("((s|S)unck)","sunck-----SuNck"))

# 需求,提取sunck.........man
str = "sunck is a good man! sunck is a nice man! sunck is a very handaome man"
print(re.findall(r"^sunck.*man$", str))  # 贪婪匹配
print(re.findall(r"sunck.*?man", str))

print("----------------特殊-----------------")
"""
*?  +?  x?  最小匹配  通常都是尽可能多的匹配,可以使用这种解决贪婪匹配
* + 都是贪婪 

(?:x)  类似(xyz),但不表示一个组
"""
# 注释: /* part1 */   /* part2 */
print(re.findall(r"//*.*/*/", r"/* part1 */   /* part2 */"))

