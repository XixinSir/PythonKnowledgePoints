import threading
import time


def func():
    # 创建一个事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            # 阻塞，等待事件的触发
            event.wait()  # set一次，这里就接受到一个消息
            # 重置
            event.clear()
            print("sunck is a good man!!%d"%i)

    t=threading.Thread(target=run).start()
    return event



e = func()


#触发事件
for i in range(5):
    time.sleep(2)
    e.set()