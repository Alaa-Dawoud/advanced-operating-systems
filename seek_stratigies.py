"""
seek stratigies implementation
tasks=[2, 9, 48]
tasks[i] = track number
"""
#FCFS
def FCFS(tasks):
    return sorted([task for task in tasks], key=lambda x:x[1])
#(track_number, release)
tasks_fcfs = [(84,1), (29,7), (50,3), (63,2)]
# print(FCFS(tasks_fcfs))
#############################
#SSTF
def get_closest(tasks, task):
    # subtract task from each task to get the smallest mone which is the closest
    # neglect the first one as it is the same task (result = 0)
    subtracted = sorted([(abs(t - task), t) for t in tasks], key=lambda x: x[0])
    closest = subtracted[1][1]
    return closest, subtracted
def SSTF(tasks, index):
    # index to represent starting task
    sorted_tasks = [tasks[index]]
    for _ in range(len(tasks)-1):
        # get closest task to current task 
        closest, subtracted = get_closest(tasks, sorted_tasks[-1])
        # if closest already in sorted tasks append the next task in subtracted
        i=1
        while(closest in sorted_tasks):
            i+=1
            closest = subtracted[i][1]
            continue
        sorted_tasks.append(closest)
    print(sorted_tasks)
tasks = [4, 7, 11, 14, 15, 35, 40]
#(tasks, index) index to which task to strat from
# SSTF(tasks, 4)
#############################
#SCAN
def SCAN(tasks, start_track):
    #scan from start_track to outer track and reverse
    # assume number of tracks = 50
    sorted_tasks=[]
    for i in range(start_track, 51):
        if(i in tasks and i not in sorted_tasks):
            sorted_tasks.append(i)
    for i in range(50, -1, -1):
        if(i in tasks and i not in sorted_tasks):
            sorted_tasks.append(i)
    print(sorted_tasks)

tasks = [4, 7, 11, 14, 15, 35, 40]
# SCAN(tasks, 20)
#############################
#LOOK
def LOOK(tasks, start_track):
    #scan from start_track to max track and reverse to min track
    # assume number of tracks = 50
    max_track = max(tasks)
    min_track = min(tasks)
    sorted_tasks=[]
    for i in range(start_track, max_track+1):
        if(i in tasks and i not in sorted_tasks):
            sorted_tasks.append(i)
    for i in range(max_track, min_track-1, -1):
        if(i in tasks and i not in sorted_tasks):
            sorted_tasks.append(i)
    print(sorted_tasks)

tasks = [4, 7, 11, 14, 15, 35, 40]
LOOK(tasks, 15)