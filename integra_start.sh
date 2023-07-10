#!/bin/bash

docker-compose -f ./my-kafka/docker-compose-brok-spark.yml  down
docker-compose -f ./my-kafka/docker-compose-brok-spark.yml  up --scale spark-worker=3 -d 

exit_sts=$? 

if [ $exit_sts -eq 0 ] 
then 
  echo "INtegra Sarted Sucessfully .... " $? 
else
  echo "INtegra failed with status " $? 
fi
