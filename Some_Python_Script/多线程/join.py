import threading
import time

def thread_job():
    print('T1 start \n')
    for i in range(10):
        time.sleep(0.2)
    print('Ti finish\n')
        
def thread_job2():
    print('T2 start \n')
    print('T2 finish \n')

def main():
    added_thread=threading.Thread(target=thread_job,name='T1')
    added_thread2=threading.Thread(target=thread_job2,name='T2')
    added_thread.start()
    added_thread2.start()
    added_thread.join()
    added_thread2.join()
    print('add done\n')

if __name__=='__main__':
    main()