import threading, queue, time, random
# 生产者
def product(i):
    while True:
        num = random.randint(0,10000)
        q.put(num)
        print("生产者%d生产了%d数据放入了对列" % (i, num))
        time.sleep(3)
    # 任务完成
    q.task_done()

# 消费者
def customer(i):
    while True:
        item = q.get()
        if item is None:
            break;
        print("消费者%d消费了%d数据" % (i, item))
        time.sleep(2)
    # 任务完成
    q.task_done()


if __name__ == "__main__":
    # 消息队列
    q = queue.Queue()
    # 启动生产者
    for i in range(4):
        threading.Thread(target=product,args=(i,)).start()

        # 启动消费者
    for i in range(4):
        threading.Thread(target=customer,args=(i,)).start()

