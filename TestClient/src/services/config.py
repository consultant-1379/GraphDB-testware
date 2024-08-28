import json
import os
import argparse

_config_file_values = {}


def port():
    return _get_config_value('port')


def graphdb_url():
    return _get_config_value('graphdb_url')


def graphdb_user():
    return _get_config_value('graphdb_user')


def graphdb_password():
    return _get_config_value('graphdb_password')


def _get_config_value(key):
    config_value = os.environ.get(key)
    if config_value:
        print('Value of {} was found as an environment variable'.format(key))
        print(config_value)
        return config_value
    config_value = _config_file_values.get(key)
    print('Value of {} was found in config file'.format(key))
    print(config_value)
    return config_value


def _load_config():
    global _config_file_values
    config_file_path = get_config_file_path()
    print('The config file being used is: {}'.format(config_file_path))
    with open(config_file_path) as config_file:
        _config_file_values = json.load(config_file)
    _verify_config()


def get_config_file_path():
    parser = argparse.ArgumentParser(
        description='Test client for GraphDB')
    parser.add_argument('-c', '--config-file',
                        dest='config_file',
                        type=str, required=False,
                        help="The json config file to use")
    args = parser.parse_args()
    if args.config_file:
        return args.config_file
    else:
        return 'config.json'


def _verify_config():
    if not _config_file_values:
        raise Exception('No config values have been set!')


_load_config()
