"""
exit立即中断循环 退出循环语句  执行循环语句后面的语句
"""

if __name__ == "__main__":
    for m in range(10):
        print(m)
        if m == 5:
            exit()
    print("exit结束整个程序")

# 直接退出整个程序  下面这句不会执行了
print("Hello World")
