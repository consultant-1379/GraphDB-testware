import utilprocs
import os
from neo4j import GraphDatabase, basic_auth

CHART_NAME = os.environ.get('baseline_chart_name')
BASELINE_RELEASE_NAME = CHART_NAME + '-baseline-release-dl'
NAMESPACE = os.environ.get('kubernetes_namespace')

GRAPHDB_SERVICE_NAME = "eric-graphdb-n4j"
TEST_DATA_LABEL = 'TestData'

HOST = ("bolt+routing://" + GRAPHDB_SERVICE_NAME + "." + NAMESPACE +
        ".svc.cluster.local")
USER = "neo4j"
PASSWORD = "demo"

driver = GraphDatabase.driver(HOST, auth=basic_auth(user=USER,
                                                    password=PASSWORD))


def create_nodes(number_of_nodes):
    """
    Creates a specified number of nodes in Neo4j. The nodes will contain
    arbitrary data.
    :param number_of_nodes: The number of nodes to be created
    """
    for i, n in enumerate(range(number_of_nodes)):
        create_node(f'Node number {n}')


def create_node(node_name):
    """
    Creates a single node in Neo4j. The node will contain arbitrary data.
    :param node_name: The name which will be given to the node.
    """
    with driver.session() as session:
        cypher_command = ("CREATE (a:" + TEST_DATA_LABEL + " {name:'" +
                          str(node_name) + "', born:2019})")
        res = session.run(cypher_command)
        res.consume()
        utilprocs.log(f'Created a node with the name: {node_name}')


def delete_test_data():
    with driver.session() as session:
        utilprocs.log('Deleting all test data...')
        cypher_command = f'MATCH (a:{TEST_DATA_LABEL}) DELETE a'
        session.run(cypher_command)
