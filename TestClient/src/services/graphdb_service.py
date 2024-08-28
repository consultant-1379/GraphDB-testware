import services.config as config
from neo4j import GraphDatabase, basic_auth


GRAPHDB_URL = config.graphdb_url()
print(GRAPHDB_URL)
TEST_DATA_LABEL = 'TestData'

driver = GraphDatabase.driver(GRAPHDB_URL, auth=basic_auth(
    user=config.graphdb_user(), password=config.graphdb_password()
))
read_sessions = {}


def create_test_data(number_of_nodes):
    print('Creating nodes...')
    with driver.session() as session:
        for node_number in range(number_of_nodes):
            node_name = f'Node number {node_number}'
            cypher_command = ("CREATE (a:" + TEST_DATA_LABEL + " {name:'" +
                              str(node_name) + "', born:2019})")
            session.run(cypher_command)
    print('Finished creating nodes!')

def delete_test_data():
    with driver.session() as session:
        print('Deleting all test data...')
        cypher_command = f'MATCH (a:{TEST_DATA_LABEL}) DELETE a'
        session.run(cypher_command)


def read_test_data():
    with driver.session() as session:
        result = session.run("MATCH (a:" + TEST_DATA_LABEL + ") RETURN a")
        return result

