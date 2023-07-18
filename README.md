# INTEGRA - The general purpose Joiner with AI   #

This Repo consist entire Integra project with its Code bases. Following is the structure of project folder.

 # INTEGRA(root folder)  

  + INTEGRA
    + frontend  => ReactJS code for presentation layer.
    + broker    => Kafka Publisher and Kafka Produce code .
    + compute   => Pyspark code for enabling the Workflow.
    + my-kafka  => DockerFiles for individual component of kafka Cluster. 
    + my-spark  => DockerFiles for individual component of Spark Cluster.
    - Readme.md 
    - integra_start.sh => script to start the Integra cluster.
    - integra_stop.sh  => script to stop the Integra cluster.
    - zoosh     => script to log into Zookeeper machine. 
    - mash      => script to log into Spark Master machine.
    - Readme.md 
 
The above structure of folder will remain until need arises to fork the compute and frontend layers.

