from multiprocessing import Semaphore
import threading
import time
import random

apple = threading.Semaphore(0) #定义苹果信号量
orange = threading.Semaphore(0) #定义橘子信号量
mutex = threading.Semaphore(1) #定义盘子信号量

def Father():
    for i in range(5):
        mutex.acquire() #先获取盘子的信号量
        if random.random()>0.5: #随机选择放橘子还是苹果
            print("放橘子")
            orange.release() #释放橘子信号量，表示橘子已经放在盘子里
        else:
            print("放苹果")
            apple.release() #释放苹果信号量，表示苹果放在了盘子里
        
def Daughter():
    while 1:
        orange.acquire() #如果有橘子信号量，就获取橘子
        print("从盘中取出橙子")
        mutex.release() #橘子获取后，盘子为空，所以释放盘子信号量
        time.sleep(1)

def Son():
    while 1:
        apple.acquire() #如果有苹果信号量，就获取苹果
        print("从盘中去出苹果")
        mutex.release() #苹果获取后，盘子为空，所以释放盘子信号量
        time.sleep(1)
        
if __name__ == '__main__':
    father = threading.Thread(target=Father)
    daughter = threading.Thread(target=Daughter)
    son = threading.Thread(target=Son)
    father.start()
    daughter.start()
    son.start()