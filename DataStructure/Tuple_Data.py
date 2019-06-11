"""
tuple

本质:  是一种有序集合

特点:
1、与列表非常相似
2、一旦初始化就不能修改
3、使用小括号
"""

# 创建空的元组
tuple1 = ()
print(tuple1)  # ()

# 创建带有元素的元组
# 元组中的元素类型可以不同
tuple2 = (1, 2, 3, "good", True)
print(tuple2)  # (1, 2, 3, 'good', True)

# 定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)  # (1,)
print(type(tuple3))  # <class 'tuple'>


# 元组元素的访问
# 格式: 元组名[下标]  (下标从0开始)
tuple4 = (1, 2, 3, 4, 5)
print(tuple4[0])  # 1
print(tuple4[4])  # 5
# print(tuple4[5]) 下标超过范围 怎么捕获此异常
#  获取最后一个元素
print(tuple4[-1])  # 最后一个 5
print(tuple4[-2])
print(tuple4[-5])  # 第一个   1
try:
    print(tuple4[-6])
except IndexError:
    print("元组下标超过界限")  # 注意越界是 IndexError异常


# 修改元组
tuple5 = (1, 2, 3, 4, [5, 6, 7])
#  tuple5[-1] = [7, 8, 9] 报错 元组不能修改
tuple5[-1][0] = 500
print(tuple5)


# 删除元组
tuple6 = (1, 2, 3)
del tuple6
# print(tuple6)  # NameError: name 'tuple6' is not defined



# 元组的操作
t7 = (1, 2, 3)
t8 = (4, 5, 6, 7, 8)
t9 = t7 + t8
print(t9)  # (1, 2, 3, 4, 5, 6)
print(t7, t8)  # (1, 2, 3) (4, 5, 6)


# 元组重复
t10 = (1, 2, 3)
print(t10 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 判断元素是否在元组中
t11 = (1, 2, 3)
print(4 in t11)  # False


# 元组的截取
# 格式: 元组名[开始下标: 结束下标]
# 从开始下标开始截取, 截取到结束下标之前 最后一个取不到
t12 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t12[3:7])  # (4, 5, 6, 7)
print(t12[3:])  # (4, 5, 6, 7, 8, 9)
print(t12[:7])  # (1, 2, 3, 4, 5, 6, 7)


# 二位元组：  元素为一维元组的元组
t13 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(t13[1][1])  # 5


# 元组的方法
#  len()  返回元组中元素的个数
t14 = (1, 2, 3, 4, 5)
print(len(t14))  # 5


# max()  返回元组中的最大值   min
print(max(5, 6, 7, 8, 9))  # 9
print(min(5, 6, 7, 8, 9))  # 5


# 将列表转换成元组
list = [1, 2, 3]
t15 = tuple(list)
print(t15)  # (1, 2, 3)


# 元组的遍历

