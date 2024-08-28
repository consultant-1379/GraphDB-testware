from services.reading_session.read_session import ReadSession
import string
import random

_read_sessions = {}


def start_reading():
    read_session = ReadSession()
    session_token = generate_session_token()
    print(f'Session token has been generated: {session_token}')
    _read_sessions[session_token] = read_session
    read_session.start_reading()
    return session_token


def stop_reading(session_token):
    read_session = _read_sessions[session_token]
    session_data = read_session.stop_reading()
    del _read_sessions[session_token]
    return session_data


def generate_session_token(size=10, chars=string.ascii_lowercase
                           + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
