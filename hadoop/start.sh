#! /bin/bash
docker-compose -f docker-compose_kafka.yml  up  -d
sleep 5
docker-compose -f docker-compose.yml  up --scale dataNode=3  -d
sleep 5
./remhostcp.sh
sleep 5
docker exec -it ZOO1  bash -c " node /opt/sub-pub/kafka_prod.js"
