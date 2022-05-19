"""
(release_time, period, execution_time, deadline)
T3 = (20, 60, 15, 60)
T2 = (15, 60, 10, 40)
T1 = (0, 60, 25, 50)
"""
import time

refrence_time = time.time()
class Task():
    def __init__(self, name, release, period,
                execution, deadline):
        self.name = name
        self.release = release
        self.period = period
        self.execution = execution
        self.deadline = deadline
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
                    break
        else:
            print("task has already finished execution")

def check_release(tasks):
    released_tasks = sorted([task for task in tasks], key=lambda x: x.release)
    # assuming release times are different
    # execute first task until the release of second task and then check priority
    priorities = [released_tasks[0]]
    for i in range(len(released_tasks[:-1])):
        # calculate execution time until next release
        ex_time = released_tasks[i+1].release - released_tasks[i].release
        priorities[0].start_execution(ex_time)
        print("_____________________")
        # append the next task to check priorities
        priorities.append(released_tasks[i+1])
        priorities = check_priority(priorities)
        
    
    # priorities has been finished according to release time
    # now execute according to earliest deadline untile task finish execution

def check_priority(priorities_tasks):
    priorities = sorted([task for task in priorities_tasks], key=lambda x: x.deadline)
    return priorities
def dma(tasks):
    check_release(tasks)
    # now all tasks has been released we then execute according to deadline
    # until all task finish
    sorted_dma = sorted([task for task in tasks], key=lambda x: x.deadline)
    for task in sorted_dma:
        task.start_execution(task.remain_execution)

T1 = Task("T1", 0, 60, 25, 50)
T2 = Task("T2", 15, 60, 10, 40)
T3 = Task("T3", 20, 60, 15, 60)
tasks = [T1, T2, T3]
dma(tasks)
