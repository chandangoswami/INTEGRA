
FROM ubuntu:latest

LABEL author="Chandan Goswami " email="goswami75@gmail.com"
LABEL version="0.2"


ENV KAFKA_VER=3.4.1
ENV KAFKA_HOME=/usr/sbin/kafka/
ENV ZOOKEEPER_CLIENT_PORT=2181
ENV ZOOKEEPER_SERVER_ID=10

RUN mkdir -p "${KAFKA_HOME}"

RUN apt update &&\
    apt install -y default-jre && \
    apt install -y wget && \  
    apt install procps && \  
    apt install -y net-tools && \  
    apt install -y  vim && \  
    apt install -y tar 

RUN cd "/tmp/"

RUN wget -q https://dlcdn.apache.org/kafka/${KAFKA_VER}/kafka_2.13-${KAFKA_VER}.tgz  &&\
    tar xvfz kafka_2.13-${KAFKA_VER}.tgz 

RUN cp -R kafka_2.13-${KAFKA_VER}/*  "${KAFKA_HOME}" &&\
    rm  kafka_2.13-${KAFKA_VER}.tgz && \
    rm -r kafka_2.13-${KAFKA_VER} 

RUN cd  "${KAFKA_HOME}"

EXPOSE $ZOOKEEPER_CLIENT_PORT 

cmd ["/usr/sbin/kafka/bin/zookeeper-server-start.sh" , "/usr/sbin/kafka/config/zookeeper.properties" ] 
