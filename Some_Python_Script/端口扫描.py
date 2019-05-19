#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    print('[*] scan Start!\n')
    setdefaulttimeout(1)
    for p in range(1,10000):
        t = threading.Thread(target=portScanner,args=('192.168.1.140',p))
        threads.append(t)
        t.start()     
    for t in threads:
        t.join()
    print('\n[*] scan Over!Find %d open ports ' % (openNum))

if __name__ == '__main__':
    main()