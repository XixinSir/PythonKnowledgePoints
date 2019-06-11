'''
while语句:
while 表达式：
    语句

逻辑：当程序执行到while语句时,首先计算“表达式”的值，如果"表达式"值为假，那么结束整个while语句。如果“表达式”的值为真，则执行“语句”，执行完“语句”再计算“表达式”的值，
循环，直到表达式的值为假才停止。
'''

num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
    print(num)
print("sum = %d" % (sum))

str = "sunck is a handsome man"
index = 0
while index < len(str):
    print('str[%d]=%s' % (index, str[index]))
    index += 1

'''
打印出所有三位数中的水仙花数
告诉我五位数中有多少个回文数
从控制台输入一个数，判断是否是质数
从控制台输入一个数，分解质因数
从控制台输入一个字符串，返回这个字符串中有多少个单词
sdf dsnofn ggd   4
   sfdskf  fd  dfi    3
从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
'''
# 字符串是ASCII码值
'''
每一个字符都有一个ASCII码值
字符串存到内存当中
a->数字-》二进制 
   97
A  65
0  48
'''


"""
# 1
num = 100
while num <= 999:
    a = num % 10
    b = num // 10 % 10  # num对10取整再对10取余
    c = num // 100
    if num == a ** 3 + b ** 3 + c ** 3:
        print(num)
    num += 1
"""


'''
# 2
num = int(input())
if num == 2:
    print("是质数")
index = 2
while index <= num - 1:
    if num % index == 0:
        print("不是质数")
    index += 1
if index == num:
    print('是质数')

'''


"""
#3 
str=input()
index = 0
sum = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum += int(str[index])
    index += 1
print('sum = %d' %(sum))
"""

'''
#4
# 90 = 2*3*3*5
num = int(input())
i = 2 
while num != 1
    if num % i == 0:
        print(i)
        num //= i 
    else: 
        i += 1 
        

'''



'''
计算有多少个单词
str = input() 
str1 = str.strip() 
index = 0 
count = 0 
while index < len(str1):
    while str1[index] != "":
        index += 1
        if index= len(str1)
            #结束这个循环
            break
    count += 1
   
    if index= len(str1)
            #结束这个循环
            break
    while str1[index] == '':
        index += 1
print(count)
'''

