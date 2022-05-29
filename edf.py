"""
earliest deadline first implementaion
task = (deadline, execution_time)
"""
import time

refrence_time = time.time()
class Task():
    def __init__(self, name, deadline, execution):
        self.name = name
        self.deadline = deadline
        self.execution = execution
        self.remain_execution = execution
        self.earliest_deadline = None
    def start_execution(self):
        if self.remain_execution !=0:
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
        #check for deadline times for every task to set remain_ex to execution_time
        # if time reached deadline
        if(int(time_now % task.deadline) == 0):
            task.remain_execution = task.execution
        task.earliest_deadline = task.deadline - int(time_now % task.deadline)
    priorities = sorted([task for task in tasks if task.remain_execution !=0], key=lambda x: x.earliest_deadline)
    return priorities
def edf(tasks):
    while True:
        priority_tasks = check_priority(tasks)
        #check if all tasks are finished and no tasks to execute for now
        if(len(priority_tasks)==0):
            print("No tasks to execute for current time")
            time.sleep(1)
            continue
        priority_tasks[0].start_execution()
T1 = Task("T1", 2, 1)
T2 = Task("T2", 5, 3)
tasks = [T1, T2]
edf(tasks)
