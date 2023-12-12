import time


class Process:
    name: str
    arrival_time: int
    service_time: int
    service_time_remaining: int
    wait_time: int
    executed_time_during_turn: int

    def __init__(self, name, arrival_time, service_time):
        self.name = name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.service_time_remaining = service_time
        self.wait_time = 0
        self.executed_time_during_turn = 0

    def do_critical_section(self):
        while self.service_time_remaining > 0:
            print(f"Process `{self}, named: {self.name}` is currently running")
            time.sleep(1)
            self.service_time_remaining -= 1
            self.executed_time_during_turn += 1

    def get_process_waiting_time(self):
        pass
        # return self.wait_time

    def get_turnaround_time(self):
        pass
