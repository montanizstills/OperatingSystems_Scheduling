from collections import deque
ALGORITHM_NAME = "RoundRobin"

arrivals = {0: "A", 3: "B", 6: "C", 8: "D"}
services = [10,2,8,7]
n = len(arrivals)
sumOfServiceTimes = 0
#Setting time quantum slightly larger than avg service time
quantum = (sum(services) /n) + 1
rem_st = [0] * n
# Copy the burst time into rt[]
for i in range(n):
    rem_st[i] = services[i]
t = 0
wt = [0] * n
queue = deque()
done = False
while (not done):
    for i in range(sum(services) + 1):
        if i in arrivals:
            queue.enqueue(arrivals[i])




            


