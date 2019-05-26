import threading

def thread_job():
    print('This is Thread_job,number is %s'% threading.current_thread())

def main():
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__=='__main__':
    main()