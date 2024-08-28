import time
from testclient_service import TestClientService as TestClient


def test_testclient():
    TestClient.create_data()
    token = TestClient.start_reads()
    # Wait for a few seconds to allow the Test Client to perform some reads
    time.sleep(4)
    result = TestClient.stop_reads(token)
    print(f'Total reads: {result["total_reads"]}')
    print(f'Average reads: {result["average_reads"]}')
    print(f'Min reads per second: '
          f'{result["min_reads_per_second"]}')
    print(f'Max reads per second: '
          f'{result["max_reads_per_second"]}')
    TestClient.delete_data()
