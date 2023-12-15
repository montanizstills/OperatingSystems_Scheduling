
'''
processes have arrival times and service times.
steps:
1. calculate waiting time (wt).
2. calculate turnaround time = service time (st) + wt

1. calculate waiting time.

keep track of the process with the shortest rt.
when a process arrives:
    it gets added to queue
    sort the queue by hrrn
once a process finishes:
    queue.pop()

queue must be sorted after every insertion in descending order of their hrrn.
every time the waiting time is increased -> update spn
'''

import math
ALGORITHM_NAME = "HRRN"

# Saving the value as a list because multiple processes can arrive at the same time
# arrivals = {0: ["A"], 2: ["B"], 4: ["C"], 6: ["D"], 8: ["E"]}
# services = {"A": 3, "B": 6, "C": 4, "D": 5, "E": 2}
#
# test_processes = {
#     'A': (0, 3),
#     'B': (2, 6),
#     'C': (4, 4),
#     'D': (6, 5),
#     'E': (8, 2)
# }

class Process:
    def __init__(self, process_name, arrival_time, service_time):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.ratio = 1
        self.wait_time = 0

    def updateRatio(self):
        self.ratio = (self.wait_time + self.service_time)/ self.service_time

def convertData(data):
    arrivals = {}
    services = {}

    for key in data:
        item = eval(data[key])
        services[key] = item[1]
    for key in data:
        item = eval(data[key])
        arrival = item[0]
        # print(arrival)
        # exit(1)
        if arrival in arrivals:
            arrivals[arrival] = arrivals[arrival].append(key)
        else:
            arrivals[arrival] = [key]
    return arrivals, services


def run(data):
    arrivals, services = convertData(data)
    n = len(services)

    # Waiting time
    wt = {}

    # Setting up latestLength to see how many seconds we have to loop to.
    latestArrival = max(arrivals.keys())
    longestService = 0
    for process in arrivals[latestArrival]:
        longestService = max(longestService, services[process])
    latestLength = latestArrival + longestService

    # Initializing remaining service time
    rt = {}

    queue = []
    currProcess = ""

    # Initially remaining time is the same as service time
    for i in services.keys():
        rt[i] = services[i]

    for i in range(max(sum(services.values()) + 1, latestLength)):
        print("time = ", i)

        # Increase the wait time for all the processes in queue
        increaseWaitTime(queue, wt)
        # If process arrives then begin servicing if no process currently running
        # If there is an existing process, add this to queue
        if i in arrivals:
            for j in range(len(arrivals[i])):
                process_name = arrivals[i][j]
                arrival, service = data[process_name]
                process = Process(process_name, arrival, service)
                queue.append(process)


            if currProcess == "" and queue:
                # Sorting the queue in increase order of their ratio times
                queue.sort(key=lambda process: process.ratio)
                currProcess = queue.pop()

        # If no process has arrived, then currProcess is set to ""
        elif currProcess == "":
            continue

        # If the process had been completed, then remove from processor and pop process from queue
        if currProcess != "" and rt[currProcess.process_name] == 0:
            # Sorting the queue in increase order of their ratio times
            queue.sort(key=lambda process: process.ratio)
            if queue:
                currProcess = queue.pop()
            else:
                currProcess = ""
        # If a process is running, reduce remaining time to completion by 1 second
        if currProcess != "" and rt[currProcess.process_name] != 0:
            rt[currProcess.process_name] -= 1

        print("queue =")
        if queue:
            for item in queue:
                print(item.process_name, ":", item.ratio)

        if currProcess:
            print("curr process =", currProcess.process_name)


    print("wait times = ", dict(sorted(wt.items())))

    tt = calculateTurnaroundTime(services, wt)
    print("turnaround time =", tt)

    avg_tt = sum(tt.values()) / len(tt.values())
    print("Average turnaround time  =", avg_tt)

    return {
        "turnaroundtimes": tt,
        "averageTurnAroundTime": avg_tt
    }


# Function to increase the wait times of the processes every second they are in the waiting queue.
def increaseWaitTime(queue, wt):
    if queue:
        for process in queue:
            wt[process.process_name] = wt.get(process.process_name, 0) + 1
            process.wait_time = wt[process.process_name]
            process.updateRatio()


# Turnaround time = service time + wait time
def calculateTurnaroundTime(services, wt):
    tt = {}
    for key, val in services.items():
        tt[key] = val + wt.get(key, 0)
    return tt

if __name__ == "__main__":
    data = {
        'A': (0, 10),
        'B': (3, 2),
        'C': (6, 8),
        'D': (8, 7)
    }
    run(data)





