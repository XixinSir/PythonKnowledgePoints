import threading
import time

sem = threading.Semaphore(4)  # 控制线程数量，让几个同时执行
def run():
    with sem:
        for i in range(10):
            print("%s--%d" % (threading.current_thread().name, i))
            time.sleep(1)

if __name__ == "__main__":
    for i in range(5):    # 创建5个线程
        threading.Thread(target=run).start()  # 创建就启动了
