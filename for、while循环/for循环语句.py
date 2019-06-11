'''
for语句
格式：
for 变量名 in 集合:
    语句
逻辑：按顺序取"集合"中的每个元素赋值给'变量',再去执行语句。如此循环往复，直到取完'集合'中的元素截止。
'''

num = 0
for i in(1, 2, 3, 4, 5):  # 列表里面的元素是都可以取到的(换成元组也一样)
    num += i
print(num)

sum = 0
for h in(1, 101):  # 这样会把列表中的每个元素相加  列表中只有1和101
    sum += h
print(sum)

sum = 0
for mm in range(1,101): # 这里是从1加到100
    sum += mm
print(sum)



'''
range([start],end,step)函数  列表生成器
start默认为0，step默认为1
功能：生成数列 
'''
a = range(10)
print(a)
for x in range(10):  # 写在range里面的,开始的可以取到,最后的值取不到
    print(x)
for y in range(2, 20, 2):
    print(y)
# 同时便利下标和元素
for index, m in enumerate((1, 2, 3, 4, 5)):  # index,m= 下标,元素  元组和列表都可以这样枚举
    print(index, m)

