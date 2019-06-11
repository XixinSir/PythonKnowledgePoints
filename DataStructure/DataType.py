"""
分类:  整数、 浮点数、 复数
"""

"""
整数:  Python可以处理任意大小的整数  当然包括负整数 在程序中的表示和数学的写法一样
"""

num1 = 10
num2 = 20
num2 = num1
"""用作用域来解释"""
print(id(num1))
print(id(num2))  # 地址一样


# 连续定义多个变量
num3 = num4 = num5 = 1
print(num1, num2, num3)  # 1 1 1

print(id(num3))
print(id(num4))  # 地址一样

# 交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7)  # 6  7
