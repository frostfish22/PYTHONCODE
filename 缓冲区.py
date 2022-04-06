import threading
import time
import random

mutex1 = threading.Semaphore(1) #对缓冲区的访问mutex1=1
mutex2 = threading.Semaphore(1) #队计数变量的访问mutex2=1
Count=0 #计数变量：Count=0
s1 = threading.Semaphore(0) #p1对p2的信号量
s2 = threading.Semaphore(0) #p1对p3的信号量
s3 = threading.Semaphore(0) #p1对p4的信号量

def p1():
    for i in range(5):
        mutex1.acquire() #获取对缓冲区访问的信号量，使用缓冲区
        print("p1发送信息") #在缓冲区放入信息
        mutex2.acquire() #放入信息后，计数变量就被获取
        global Count #计数变量重置为0
        Count=0
        mutex2.release() #缓冲区用完，释放缓冲区
        s1.release() #开始给p2，p3，p4释放信号量，让它们能获取信息
        s2.release()
        s3.release()
        
def p2():
    while 1:
        s1.acquire() #获取来自p1的信号量
        print("p2接收信息") #获取缓冲区内的信息
        mutex2.acquire() #因为要获取缓冲区的信息，所以就要获取缓冲区的信号量
        global Count
        Count=Count+1 #对计数变量+1
        if Count==3: #如果p1，p2，p3都接收到信号量，就释放缓冲区，让p1可以获取并放入信息
            mutex1.release()
        mutex2.release() #获取数据后就释放，让p2和p3有的获取
        
def p3():
    while 1:
        s2.acquire() #获取来自p1的信号量
        print("p3接收信息") #获取缓冲区内的信息
        mutex2.acquire() #因为要获取缓冲区的信息，所以就要获取缓冲区的信号量
        global Count 
        Count= Count+1 #对计数变量+1
        if Count==3: 
            mutex1.release() #如果p1，p2，p3都接收到信号量，就释放缓冲区，让p1可以获取并放入信息
        mutex2.release()#获取数据后就释放，让p3有的获取
        
def p4():
    while 1:
        s3.acquire() #获取来自p1的信号量
        print("p4接收信息") #获取缓冲区内的信息
        mutex2.acquire() #因为要获取缓冲区的信息，所以就要获取缓冲区的信号量
        global Count
        Count=Count+1 #对计数变量+1
        if Count==3:
            mutex1.release() #如果p1，p2，p3都接收到信号量，就释放缓冲区，让p1可以获取并放入信息
        mutex2.release() #获取数据后就释放

if __name__ == '__main__':
    p11 = threading.Thread(target=p1)
    p22 = threading.Thread(target=p2)
    p33 = threading.Thread(target=p3)
    p44 = threading.Thread(target=p4)
    p11.start()
    p22.start()
    p33.start()
    p44.start()