"""
立即中断循环 退出循环语句  执行循环语句后面的语句
"""
for m in range(100):
    print(m)
    if m == 50:
        break
print("break用来退出循环,执行循环后面的语句")


num = 1
while num < 10:
    print(num)
    num += 1
    if num == 50:
        break
print("break用来退出循环,执行循环后面的语句")

