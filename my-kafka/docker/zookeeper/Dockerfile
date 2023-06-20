
FROM integra/kafka-base:latest

LABEL author="Chandan Goswami " email="goswami75@gmail.com"
LABEL version="0.2"

EXPOSE $ZOOKEEPER_CLIENT_PORT 

cmd ["/usr/sbin/kafka/bin/zookeeper-server-start.sh" , "/usr/sbin/kafka/config/zookeeper.properties" ] 
