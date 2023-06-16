
FROM ubuntu:latest

LABEL author="Chandan Goswami " email="goswami75@gmail.com"
LABEL version="0.2"

ENV KAFKA_HOME=/usr/sbin/kafka/

RUN mkdir -p "${KAFKA_HOME}"

RUN apt update &&\
    apt install -y default-jre && \
    apt install -y wget && \  
    apt install procps && \  
    apt install -y nodejs && \  
    apt install -y npm && \  
    apt install -y tar 

RUN cd "/tmp/"

RUN wget -q https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz  &&\
    tar xvfz kafka_2.13-3.4.0.tgz 

RUN cp -R kafka_2.13-3.4.0/*  "${KAFKA_HOME}" &&\
    rm  kafka_2.13-3.4.0.tgz && \
    rm -r kafka_2.13-3.4.0 

RUN npm install kafka3.4.0/*  "${KAFKA_HOME}" &&\

CMD [ "tail", "-f", "/dev/null" ]
