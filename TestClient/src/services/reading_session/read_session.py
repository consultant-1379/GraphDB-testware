from services.reading_session.session_data import SessionData
from services.reading_session.read_thread import ReadThread


class ReadSession:

    def __init__(self):
        self._session_data = SessionData()
        self._read_thread = ReadThread(self._session_data)

    def start_reading(self):
        self._read_thread.start()

    def stop_reading(self):
        self._read_thread.stop()
        self._read_thread.join()
        return self._session_data


