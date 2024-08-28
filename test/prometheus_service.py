import requests
import os

_NAMESPACE = os.environ.get('kubernetes_namespace')
_PROMETHEUS_URL = 'http://eric-pm-server.{}.svc.cluster.local'.format(_NAMESPACE)
_PROMETHEUS_PORT = '9090'
_PROMETHEUS_QUERY_URL = "{}:{}/api/v1/query?query=".format(_PROMETHEUS_URL,
                                                          _PROMETHEUS_PORT)

OPENED_TRANSACTIONS = 'org_neo4j_kernel_0_numberofopenedtransactions'
TOTAL_STORE_SIZE = 'org_neo4j_kernel_0_totalstoresize{name="Store%20sizes",}'
ALLOCATED_BYTES = 'go_memstats_alloc_bytes'


def get_allocated_bytes():
    return get_metric('go_memstats_alloc_bytes')


def _get_metrics_by_name(metric_name):
    response = requests.get(_PROMETHEUS_QUERY_URL + metric_name)
    response_as_json = response.json()
    results = response_as_json['data']['result']
    return results


def get_metric(metric_name):
    all_results = _get_metrics_by_name(metric_name)
    result_as_string = all_results[0]['value'][1]
    return int(result_as_string)


def sum_metrics(metric_name):
    results = _get_metrics_by_name(metric_name)
    total = 0
    for result in results:
        metric_as_string = result['value'][1]
        metric = int(metric_as_string)
        total += metric
    return total
