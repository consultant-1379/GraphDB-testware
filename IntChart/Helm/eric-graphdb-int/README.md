# Neo4j Integration Chart


1. go to folder IntChart/Helm

2. update helm dependencies
helm up dep ./eric-graphdb-int
#lists out dependencies to be updated in repo

3. update repo(s) individually (may be recursively it can be done)

#############################Repositories########################################################################
helm repo add eric-graphdb-n4j        https://armdocker.rnd.ericsson.se/artifactory/proj-helm_aia-generic-local/snapshots/eric-graphdb-n4j
helm repo add eric-pm-server          https://arm.rnd.ki.sw.ericsson.se/artifactory/proj-adp-pm-server-helm
helm repo add eric-log-shipper        https://arm.rnd.ki.sw.ericsson.se/artifactory/proj-adp-log-shipper-helm
helm repo add eric-data-visualizer-kb https://arm.rnd.ki.sw.ericsson.se/artifactory/proj-adp-data-visualizer-kb-helm
helm repo add eric-data-search-engine https://arm.rnd.ki.sw.ericsson.se/artifactory/proj-adp-data-search-engine-helm
###################################################################################################################

4. helm dep up eric-graphdb-int/
   -- downloads dependencies/charts

5. helm install ./eric-graphdb-int --namespace <<DEV-NAMESPACE>>
   -- installs charts

6. kubectl get service -n <<DEV-NAMESPACE>>

   lists out services as below:
   '''
      eric-data-search-engine             ClusterIP   10.101.215.31   <none>        9200/TCP,9300/TCP                              17m
      eric-data-search-engine-data        ClusterIP   None            <none>        9300/TCP                                       17m
      eric-data-search-engine-discovery   ClusterIP   10.103.27.74    <none>        9300/TCP                                       17m
      eric-data-visualizer-kb             NodePort    10.100.64.112   <none>        31000:30340/TCP                                17m
      eric-pm-server                      NodePort    10.98.158.175   <none>        9090:30201/TCP                                 17m
      yellow-jellyfish-neo4j              ClusterIP   None            <none>        7474/TCP                                       17m
   ,,,

   ** wait till all pods are up and running

7. Browse for prometheus and kibana as below:
   cluster IP - 10.210.165.44 (for DEV env)
   a) prometheus http://10.210.165.44:30201 (or listed port from step 5)

   b) kibana http://10.210.165.44:30340 (or listed port from step 5)

      Click Management in left navigation menu
      i) Define index  pattern
         kubelog*
      ii) In configure setting
         add @timestamp
      iii) click "Create index pattern" button

      Click Discover in left navigation menu
      iv) click "Discover" to visualize logs
          a) Add message field
          b) search for neo4j