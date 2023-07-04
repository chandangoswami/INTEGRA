#!/bin/bash

docker-compose -f docker-compose-brok-spark.yml  down
docker-compose -f docker-compose-brok-spark.yml  up --scale spark-worker=3
