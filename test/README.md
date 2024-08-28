# Testing strategy for GraphDB Integration chart

## How to run the tests

### Prerequisites

* Have Python 3 installed
* Have Pip 3 installed

### Install helm charts

To run the tests against the integration chart, we must first install
the Integration Chart and the TestClient Chart. Make sure that you have 
the necessary helm repos added. You will need the helm repo of the 
integration chart and the testclient. To add these helm repos,
run the following commands:

    helm repo add IntChart https://armdocker.rnd.ericsson.se/artifactory/proj-helm_aia-generic-local/snapshots/eric-graphdb-int
    helm repo add TestClient https://armdocker.rnd.ericsson.se/artifactory/proj-helm_aia-generic-local/snapshots/graphdb-test-client

Install the integration chart in your namespace:

    helm install IntChart/eric-graphdb-int --name int-chart --namespace <<YOUR-NAMESPACE>> --version <<YOUR-VERSION>>

Install the Test Client chart in your namespace:

    helm install TestClient/graphdb-test-client --name test-client --namespace <<YOUR-NAMESPACE>> --version <<YOUR-VERSION>>

* Note: Replace `<<YOUR-NAMESPACE>>` with the namespace that you wish to install the charts in. Replace `<<YOUR-VERSION>>`
with the version of the chart you wish to install.

### Install git submodules

Before running the tests, make sure you have the testframework submodule initialised. This can be done as follows:

    git submodule sync
    git submodule update --init --recursive

### Install python dependencies

Next, you must install the Python dependencies for the testframework. From the root of the project, run the following:

    pip3 install -r ./testframework/requirements.txt

### Verify python dependencies

After installing the dependencies, you may wish to verify that you have the correct versions of the dependencies installed. You can verify that you have the correct versions of the dependencies installed by running the following command:

    `while read -r line; do IFS='='; read -r -a array <<< ${line};installed="`pip3 freeze | grep ${array[0]}`"; echo "Required $line installed $installed"; done < testframework/requirements.txt`

For each of the dependencies, this command will print out the version of the dependency required and the version which your system has installed. It will be in the following format:

`Required kubernetes==6.0.0 installed kubernetes==6.0.0`

From this, you will be able to see if there is any discrepencies between what is required and what is installed on your system. In most cases, it will not be an issue if there are differences in the MINOR or PATCH number. However, if there are differences in the MAJOR number, you should resolve the difference be installing the correct version.

### Running the tests

Run the tests against the the helm installation:

    python3 -u ./testframework/bootstrap_wrapper.py -c ./test/test-config.yaml -n <<YOUR-NAMESPACE>>

* Note: Replace `<<YOUR-NAMESPACE>>` with the namespace that you wish to run the tests in. This namespace MUST be the same namespace that you installed the
Integration Chart and the TestClient Chart in.

### Clean up

Once the tests are complete, you may wish to delete the Integration chart and
the Test Client chart:

    helm delete --purge IntChart
    helm delete --purge TestClient

