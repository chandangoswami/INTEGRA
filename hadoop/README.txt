This folder consists of following folders and files
1. Dockerfile_withHadoop - DockerFile to create hadoop image with all its binaries configs.
2. Dockerfile_withHadoop_and_spark - DockerFile to create hadoop image plus spark Image with all its binaries configs.
3. config - All hadoop configuration files and utilities for hadoop installation.
4. docker-compose.yml - Compose file to create cluster and env variables.
4. data - folder from host docker mount (root) 
3. apps - 
3. base -

Following is sequence of command to execute in hadoop-nameNode-1 machine.

  cd hadoop-3.2.2/etc/hadoop/
  ./remhost.sh - To create entires for /etc/hosts for all participating machine. [ automate ]
  jps - To see if JVM process is running.
  hdfs namenode -format -> V imp. Format the HDFS before start of hdoop deamons.
  start-all.sh - Start all deamons
  jps -> check all deamons are running... On NameNode ( MASTER node) 3 deamons will be running 
	  i)   NameNode -> Hdfs process
	  ii)  SecondaryNameNode -> Hdfs process
	  iii) ResourceManager -> Yarn process
  stop-all.sh - Stops all HDFS deamons
