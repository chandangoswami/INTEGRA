docker-compose -f docker-compose_kafka.yml  up  -d
sleep 10
docker-compose -f docker-compose.yml  up --scale dataNode=3  -d
sleep 10
./remhostcp.sh
