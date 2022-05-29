import threading
import time

# task 1 needs notification from task 2 to continue executing
signaled = False
def task_1():
    print("started executing task 1 by thread", threading.current_thread().getName())
    print("waiting for task_2's signal to continue executing")
    global signaled
    while(not signaled):
        continue
    print("signal recieved and task 1 finished executing by thread", threading.current_thread().getName())
    # make signaled false for future usage of task1
    signaled = False
def task_2():
    print("started executing task 2 by thread", threading.current_thread().getName())
    time.sleep(2)
    print("giving signal to task 1 to continue")
    global signaled
    signaled=True
    

t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)
t1.start()
t2.start()
