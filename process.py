class Process:
    name: str
    arrival_time: int
    service_time: int
    service_time_remaining: int
    wait_time: int

    def __init__(self, name, arrival_time, service_time):
        self.name = name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.service_time_remaining = service_time
        self.wait_time = 0
