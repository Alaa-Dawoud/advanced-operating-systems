"""
minimum laxity first implementaion
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
        self.slack_time = None
    def start_execution(self):
        if self.remain_execution !=0:
            # check if ex_time has half a second (float)
            if(isinstance(self.execution, float)):
                time.sleep(0.5)
                print("finished execution of task", self.name, "at", round(time.time()-refrence_time, 1))
                self.remain_execution-=0.5
                if self.remain_execution == 0:
                    print("=================================")
                    print("Task", self.name, "has been finished execution")
                    print("=================================") 
            else:
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
    time_now = round(time.time()-refrence_time, 1)
    for task in tasks:
        #check for deadline times for every task to set remain_ex to execution_time
        # if time reached deadline
        
        if(int(time_now % task.deadline) == 0):
            task.remain_execution = task.execution
        # get slack time for each task
        t = int(time_now % task.deadline)
        task.slack_time = (task.deadline - t) - task.remain_execution
    # set priorities according to minimum slack time
    priorities = sorted([task for task in tasks if task.remain_execution!=0], key=lambda x: x.slack_time)
    return priorities

def mlf(tasks):
    while True:
        priority_tasks = check_priority(tasks)
        priority_tasks[0].start_execution()
T1 = Task("T1", 4, 2)
T2 = Task("T2", 10, 3)
T3 = Task("T3", 12, 3)
tasks = [T1, T2, T3]
mlf(tasks)
