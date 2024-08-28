from threading import Thread
import time
import services.graphdb_service as graphdb_service
from services.reading_session.session_data import SessionData
from services.reading_session.read_log import ReadLog


class ReadThread(Thread):

    # The max number
    _MAX_READS = 200000

    def __init__(self, session_data: SessionData):
        self._session_data = session_data
        self._stopped = False
        Thread.__init__(self)

    def run(self):
        print("About to start reading")
        logs = self._session_data.logs
        first_log = ReadLog()
        first_log.start_time = time.time()
        logs.append(first_log)
        while (self._session_data.total_reads < ReadThread._MAX_READS
               and not self._stopped):
            result = graphdb_service.read_test_data()
            while logs[-1].start_time + 1 < time.time():
                read_log = ReadLog()
                read_log.start_time = logs[-1].start_time + 1
                logs.append(read_log)
            logs[-1].reads += 1
            self._session_data.total_reads += 1

        self._session_data.start_time = logs[0].start_time
        self._session_data.stop_time = logs[-1].start_time
        # delete the last log because it will only be a fraction of a second
        if len(logs) > 1:
            del logs[-1]
        time_elapsed = (self._session_data.stop_time -
                        self._session_data.start_time)
        self._session_data.average_reads = (self._session_data.total_reads
                                            / time_elapsed)
        self._session_data.min_reads_per_second = logs[0].reads
        self._session_data.max_reads_per_second = logs[0].reads
        for log in logs:
            if log.reads > self._session_data.max_reads_per_second:
                self._session_data.max_reads_per_second = log.reads
            if log.reads < self._session_data.min_reads_per_second:
                self._session_data.min_reads_per_second = log.reads
        print("Finished reading")

    def stop(self):
        self._stopped = True
        print("Stop flag is set")
