from ast import Try
import socket
from threading import Thread
import time
def main(target,ports):
    print("开始扫描：%s"%target)
    for port in range(1,int(ports)):
        t = Thread(target=portscan,args=(target,port))
        t.start()
        
def portscan(target,port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target,port))
        print("[*] %s:%d 开放"%(target,port))
        client.close()
    except:
        pass
    
if __name__ == "__main__":
    target = input("请输入IP:")
    ports=input("请输入端口(1-?):")
    print(ports)
    start=time.time()
    main(target,ports)
    end=time.time()
    print("耗时 %.5f秒"%(end-start))