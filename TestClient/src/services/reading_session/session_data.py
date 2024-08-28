class SessionData:
    def __init__(self):
        self.total_reads = 0
        self.average_reads = 0
        self.min_reads_per_second = 0
        self.max_reads_per_second = 0
        self.start_time = 0
        self.stop_time = 0
        self.logs = []
