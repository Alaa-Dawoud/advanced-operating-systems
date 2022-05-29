import threading
import time

key_available = True
def execute_task():
    global key_available

    while(not key_available):
        continue
    
    # set key to false to prevent other threads from accessing critical region  
    key_available=False
    print("critical region entered by thread", threading.current_thread().getName())
    print("executing task")
    time.sleep(3)
    print("exiting critical region")
    key_available = True


t1 = threading.Thread(target=execute_task)
t2 = threading.Thread(target=execute_task)
t3 = threading.Thread(target=execute_task)
t4 = threading.Thread(target=execute_task)
t1.start()
t2.start()
t3.start()
t4.start()