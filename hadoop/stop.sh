#! /bin/bash
docker-compose -f docker-compose.yml down
sleep 5 
docker-compose -f docker-compose_kafka.yml down
