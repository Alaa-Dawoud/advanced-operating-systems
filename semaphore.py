import threading
import time
s=1
def test():
    global s
    if(s==1):
        s=0
def set():
    global s
    if(s==0):
        s=1
def execute_task():
    global s
    while(s==0):
        continue
    test()
    print("Starting executing task by thread", threading.current_thread().getName())
    time.sleep(2)
    print("finished execution")
    time.sleep(1)
    set()

def semaphore():
    while(len(thread_list)>0):
        thread_list[0].start()
        thread_list[0].join()
        #thread at index 0 finished execution
        thread_list.remove(thread_list[0])


thread_list = []
t1 = threading.Thread(target=execute_task)
thread_list.append(t1)
t2 = threading.Thread(target=execute_task)
thread_list.append(t2)

# thread to start semaphore to continue main program to add threads while semaphre
# is running
t3 = threading.Thread(target=semaphore)
t3.start()

time.sleep(1)
print("a new thread entered thread list")
t4 = threading.Thread(target=execute_task)
thread_list.append(t4)