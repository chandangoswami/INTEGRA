
FROM integra/kafka-base:latest

LABEL author="Chandan Goswami " email="goswami75@gmail.com"
LABEL version="0.2"


ENV KAFKA_HOME=/usr/sbin/kafka/

ENV OVERRIDE_PROPERTY=

RUN cd  "${KAFKA_HOME}"

CMD [ "sh", "-c", "/usr/sbin/kafka/bin/kafka-server-start.sh /usr/sbin/kafka/config/server.properties  $OVERRIDE_PROPERTY" ]
