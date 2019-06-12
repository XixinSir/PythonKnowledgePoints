"""
什么是字符串
字符串是以单引号或双引号括起来的任意文本
'abc'
"def"
字符串不可变
"""

# 创建字符串
str1 = "Hello The World"
str3 = "you are beautiful"
str5 = "i love you"


"""字符串运算"""
# 字符串连接
str6 = "sunck is "
str7 = "a good man"
str6 = "aaaaaa"  # 相当于重新赋值
str8 = str6 + str7
print("str6=", str6)  # str6= aaaaaa
print("str7=", str7)  # str7= a good man
print("str8=", str8)  # str8= aaaaaaa good man


# 输出重复字符串
str9 = "good"
str10 = str9 * 3
print("str10=", str10)  # str10= goodgoodgood


# 访问字符串中的某一个字符
# 通过索引下标查找字符,索引从0开始
# 字符串名[下标]
str11 = "sunck is a good man!"
print(str11[1])
# str11[1] = "a"
# print("str11=", str11) 报错  字符串不可变


# 截取字符串中的一部分
str13 = "sunck is a good man"
# 给定下标到给定下标之前
str15 = str13[6:15]
# 开头截取到下标之前
str16 = str13[0:5]
print("str15=", str15)  # str15= is a good
print("str16=", str16)  # str16= sunck
# 给定下标到结尾
str17 = str13[16:]
print("str17=", str17)  # str17= man



str18 = "sunck is a good man"
print("good" in str18)  # True
print("good1" in str18)  # False
print("good1" not in str18)  # True







# 格式化输出
#  %s    %d   %f 占位符  占一个位置

print("sunck is a good man")
num = 10
str19 = "sunck is a nice man"
f = 10.123456789
print("num =", num)  # 逗号会产生一个空格   num = 10
# 小数默认有6位  如果指定位数 会四舍五入           精确到小数点后三位,会四舍五入
print("num = %d, str19 = %s, f = %.3f" % (num, str19, f))  # 占位符 num = 10, str19 = sunck is a nice man, f = 10.123










"""
转义字符  \ 
将一些字符转换成有特殊含义的字符
\n  一个字符 内存中和a一样 
"""

# \n
print("num = %d\nstr19 = %s\nf = %.3f" % (num, str19, f))

# \ 防止转义 将转义字符转化为正常的
print("sunck  \n is")
print("sunck  \\n is")  # sunck  \n is 防止转义

#  \'  \"
# print('tom is a 'good' man') 出错
print('tom is a \'good\' man')  # tom is a 'good' man
print('tom is a "good" man')

# 如果字符串内有很多换行  用\n写在一行不好阅读
print("""
good
nice 
handsome
""")  # 注释也相当于字符串

# \t 制表符
print("sunck\tgood")  # sunck	good

# 如果字符串中 好多字符都需要转义,就需要加入好多\  为了简化  Python允许用r表示内部的字符串默认不转义
print("\\\t\\")  # \	\
print(r"\\\t\\")  # \\\t\\

print("""
C:\\Users\\Administrator\\Desktop\\tDataStructure
""")  # C:\Users\Administrator\Desktop\tDataStructure
print(r"C:\Users\Administrator\Desktop\tDataStructure")  # C:\Users\Administrator\Desktop\tDataStructure

# windows路径 C:\Users\Administrator\Desktop\tDataStructure
# Linux中的路径  /root/user/sunck/Desktop/Python-1704/day3



# eval(str)
# 将字符串str当成有效的表达式来求值并返回计算结果
# 可以用eval 或 int 判断输入的是否是整数
num1 = eval("123")  # 123
print(type(num1))  # <class 'int'>
print(eval("+123"))  # +123
print(eval("-123"))  # -123
print(eval("123+123"))  # 246
print(eval("1-123"))  # -122
# print(eval("a123"))  # 报错
# print(eval("12a3"))  # 报错





# len(str)
# 返回字符串的长度(字符个数) 循环
print(len("sunck is a good man凯"))  # 19




# lower(str)转换字符串中大(小)写字母为小(大)写字母  upper(str)
str20 = "SUNCK is a Good Man"
str21 = str20.lower()  # 相当于重新生成 不是改变
print(str21)  # sunck is a good man
print(str20)  # SUNCK is a Good Man



# swapcase()  大小写转换
str22 = "SUNCK is a Good Man"
print(str22.swapcase())  # sunck IS A gOOD mAN



# capitalize()  首字母大写，其他小写
str23 = "SUNCK is a Good Man"
print(str23.capitalize())  # Sunck is a good man




# 每个单词的首字母大写
str24 = "SUNCK is a Good Man"
print(str24.title())  # Sunck Is A Good Man



# center(width, fillchar)  # character 字符
# 写文档 放在开头
# 返回一个指定宽度的居中字符串, fillchar为填充的字符串  默认是空格填充
str25 = "SUNCK is a Good Man"
print(str25.center(40))  #           SUNCK is a Good Man
print(str25.center(40, "*"))  # 第二个参数只能是一个
# print(str25.center(10, "* ")) 报错



# ljust(width[,fillchar])       []可有可无    左对齐
# 返回一个指定宽度的左对齐字符串, fillchar为填充的字符串  默认是空格填充  右侧填充
str26 = "sunck is a good man"
print(str26.ljust(40, "%"))  # sunck is a good man*********************


# rjust(width[,fillchar])       []可有可无    右对齐
# 返回一个指定宽度的右对齐字符串, fillchar为填充的字符串  默认是空格填充  # 左侧填充
str27 = "sunck is a good man"
print(str27.rjust(40, "%"))  # sunck is a good man*********************



# zfill(width)
# 返回一个长度为width的字符串,原字符串右对齐,前面补0
str28 = "sunck is a good man"
print(str28.zfill(40))  # 000000000000000000000sunck is a good man


