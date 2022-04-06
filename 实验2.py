import threading
import time
import random

semaphore=threading.Semaphore(2)#定义信号量对象，且信号量初始化为3

def run(ii):
    semaphore.acquire()#读取关联了信号量的共享资源，信号量-1
    print(ii,'号车可以进入')
    time.sleep(random.randint(0,10)*1)#线程睡眠，停止一段时间
    print(ii,'号停车位释放')
    semaphore.release()#释放信号量，信号量+1

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run,args=(i,))
        t.start()