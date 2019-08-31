import threading
import time
import os
import re
import requests
from queue import Queue
file_count = 0
filePath = 'H:/NUAA/NUAA/NUAA_PIC'
files = os.listdir(filePath)
nameList=[] #存储名字名称列表
nameSepList=[] #存储分分离后的文件名称列表
#把文件名存储起来 过滤拿到我们想要的文件后缀
threadLock = threading.Lock()
global start


def storefile():
    Stu_16_list=[]
    for file in files:
        if(file[2:4]=='16'):
            print(file[0:9])
            nameList.append(file[0:9])





#分离文件名 给每个线程分一个
def separateName(threadCount):
    for i in range(0,len(files),threadCount):
        nameSepList.append(nameList[i:i+threadCount])


#多线程函数
def multithreading(threadCount):
    separateName(threadCount)#先分离
    for i in range(threadCount):
        t=threading.Thread(target=run_one_thread,args=(nameSepList[i],))
        t.start()

#每个线程的运作 参数为文件名称的列表
def run_one_thread(name_list):
    for k in name_list:
        print(k)
        with open(filePath + k, 'rt') as f:
            #threadLock.acquire()
            global file_count
            file_count+=1
            #threadLock.release()
            #print('已经完成: {:.2%}'.format(file_count/len(files)))      
            content = f.read()
            get = re.findall(r"GET\['(.+?)'\]", content)
            #post = re.findall(r"POST\['(.+?)'\]", content)
            for i in get:
                 #print('已经完成: {:.2%}'.format(file_count/len(files))+' FileName：'+k+'  ParamName:'+i)
                 get_rep(k, i)
            f.close()



def Record_To_File(filename,name):
    answer = open('answer.txt','a+')
    end = time.time()
    answer.write("Got It!   !!!!!!! " + filename + " The param is: _GET[\'" + name +"\']"+" Need time :"+str(end-start)+"s\n")
    print("Got It!   !!!!!!! " + filename + " The param is: _GET[\'" + name +"\']")
    answer.close()


if __name__=='__main__':
    start = time.time()
    storefile()
    multithreading(20)


    
