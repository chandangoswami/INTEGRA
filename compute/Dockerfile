FROM  integra/spark-base:latest

RUN apt-get update && apt install python3.8-venv python3-wheel -y

RUN mkdir -p /opt/integra
RUN cd /opt/integra

RUN python -m venv stream
RUN . stream/bin/activate

RUN pip install wheel pyspark==3.2.*

EXPOSE 8888 

CMD ["/usr/bin/tail", "-f", "/dev/null"]

