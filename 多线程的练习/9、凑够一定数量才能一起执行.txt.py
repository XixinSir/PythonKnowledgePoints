import threading
import time


bar = threading.Barrier(4)

def run():
    for i in range(10):
        print("%s--start" % (threading.current_thread().name))
        time.sleep(1)
        bar.wait()  # 凑四个
        print("%s--end" % (threading.current_thread().name))

if __name__=="__main__":
    for i in range(5):    # 创建5个线程
        threading.Thread(target=run).start()  # 创建就启动了
