#!/bin/bash

set -e

docker build -t integra/kafka-base:latest  docker/base
docker build -t integra/kafka-zookeeper:latest  docker/zookeeper
docker build -t integra/kafka-broker:latest  docker/broker
