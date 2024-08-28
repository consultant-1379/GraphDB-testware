import requests
import os


class TestClientService:

    _TEST_CLIENT_PORT = '5001'
    _NAMESPACE = os.environ.get('kubernetes_namespace')
    _TEST_CLIENT_URL = (f'http://test-client-graphdb-test-client.'
                        f'{_NAMESPACE}.svc.cluster.local:{_TEST_CLIENT_PORT}')

    @staticmethod
    def create_data():
        print('Using the test client to create data...')
        response = requests.get(f'{TestClientService._TEST_CLIENT_URL}/create')
        print(response.text)

    @staticmethod
    def delete_data():
        print('Using the test client to delete data...')
        response = requests.get(f'{TestClientService._TEST_CLIENT_URL}/delete')
        print(response.text)

    @staticmethod
    def start_reads():
        print('Instructing the test client to start reading...')
        response = requests.get(f'{TestClientService._TEST_CLIENT_URL}'
                                f'/read/start')
        response_as_json = response.json()
        token = response_as_json['token']
        print('The test client has started reading')
        print(f'The read session token is: {token}')
        return token

    @staticmethod
    def stop_reads(token):
        print('Instructing the test client to stop reading...')
        response = requests.get(
            f'{TestClientService._TEST_CLIENT_URL}/read/stop/{token}')
        response_as_json = response.json()
        print('Finished reading!')
        return response_as_json
