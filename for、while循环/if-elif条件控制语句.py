'''
if -else 语句

if - elif - else 语句
格式：
if 表达式1 ：
    语句1
elif 表达式2：
    语句2
elif 表达式3：
     语句3
else：  # 可有可无
    语句e
'''

age = int(input())
if age < 0:
    print('娘胎里')
elif age <= 3:
    print('婴儿')
elif age <= 6:
    print('儿童')
elif age <= 18:
    print('童年')
# elif     else if
# 每个el都是对它上面所有表达式的否定



