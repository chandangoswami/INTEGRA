#!/bin/bash

set -e

docker build -t integra/spark-base:latest ./docker/base
docker build -t integra/spark-master:latest ./docker/spark-master
docker build -t integra/spark-worker:latest ./docker/spark-worker
#docker build -t integra/spark-submit:latest ./docker/spark-submit
