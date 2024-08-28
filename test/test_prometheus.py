import time

import prometheus_service as pm_service
import neo4j_service
import utilprocs


def test_allocated_bytes():
    allocated_bytes = (pm_service.get_metric(pm_service.ALLOCATED_BYTES))
    utilprocs.log(f'The number of allocated bytes is: {allocated_bytes}')
    assert (allocated_bytes > 0), ('The number of allocated bytes must be '
                                   'greater than 0')


def test_number_of_transactions_basic():
    number_of_transactions = (pm_service
                              .get_metric(pm_service.OPENED_TRANSACTIONS))
    utilprocs.log(f'The number of transactions is: {number_of_transactions}')
    assert (number_of_transactions > 0), ('The number of transactions must be '
                                          'greater than 0')


def test_number_of_transactions():
    """
    test_prometheus.test_number_of_transactions

    Do 200 transactions, then check that Prometheus has recorded them
    """
    num_transactions = 200
    total_transactions_before = pm_service.sum_metrics(
        pm_service.OPENED_TRANSACTIONS)
    neo4j_service.create_nodes(num_transactions)
    new_transactions = 0
    for n in range(15):
        time.sleep(1)
        total_transactions_after = pm_service.sum_metrics(
            pm_service.OPENED_TRANSACTIONS)
        new_transactions = total_transactions_after - total_transactions_before
        if new_transactions >= num_transactions:
            break
    error_message = ('The number of transactions recorded by prometheus was '
                     f'less than {num_transactions}')
    neo4j_service.delete_test_data()
    assert new_transactions >= num_transactions, error_message
