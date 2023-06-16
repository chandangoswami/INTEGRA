#!/bin/bash

set -e

docker build -t goswami75/kafka-zoo:latest  docker/zookeeper
docker build -t goswami75/kafka-broker:latest  docker/broker
docker build -t goswami75/kafka-client:latest  docker/client
