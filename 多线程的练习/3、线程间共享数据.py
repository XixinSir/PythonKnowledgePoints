import threading

num = 0

def run(n):
    global num
    for i in range(10000000):
        num=num+n  # 当两个线程都执行这一步的时候,究竟谁先执行这步并不确定,有一种混乱的现象,导致最终运行结果每次都不是一个确定的值
        num=num-n


if __name__=="__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("numm=",num)