"""
rate monotonic assignment implementaion
task = (period, execution_time)
"""
import time

refrence_time = time.time()
class Task():
    def __init__(self, name, period, execution):
        self.name = name
        self.period = period
        self.execution = execution
        self.remain_execution = execution
    def start_execution(self, ex_time):
        if self.remain_execution !=0:
            for _ in range(ex_time):
                time.sleep(1)
                print("finished execution of task", self.name, "at", int(time.time()-refrence_time))
                self.remain_execution-=1
                if self.remain_execution == 0:
                    print("=================================")
                    print("Task", self.name, "has been finished execution")
                    print("=================================")
        else:
            print("task has already finished execution")

def check_priority(tasks):
    time_now = int(time.time()-refrence_time)
    for task in tasks:
        #check for period times for every task to set remain_ex to execution_time
        # if time reached period
        if(int(time_now % task.period) == 0):
            task.remain_execution = task.execution
    priorities = sorted([task for task in tasks if task.remain_execution !=0], key=lambda x: x.period)
    return priorities
def rma(tasks):
    while True:
        priority_tasks = check_priority(tasks)
        #check if all tasks are finished and no tasks to execute for now
        if(len(priority_tasks)==0):
            print("No tasks to execute for current time")
            time.sleep(1)
            continue
        priority_tasks[0].start_execution(priority_tasks[0].remain_execution)
T1 = Task("T1", 24, 7)
T2 = Task("T2", 36, 12)
T3 = Task("T3", 48, 4)
tasks = [T1, T2, T3]
rma(tasks)
