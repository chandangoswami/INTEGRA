FROM adoptopenjdk/openjdk8
LABEL author="Chandan Goswami" email="chandanG@integra.com"
LABEL version="0.2"

ENV DAEMON_RUN=true
ENV HADOOP_VERSION=2.7
ENV HADOOP_HOME=/opt/hadoop 

RUN apt-get update &&\
    apt-get install -y vim wget curl openssh-server net-tools

RUN apt-get clean

RUN echo exit 0 > /usr/sbin/policy-rc.d

# 1 Create Password less ssh access to ALL keys
# 1.1 Create entires for password less access 
RUN mkdir /var/run/sshd && \
    sed -ri 's/^#?PermitEmptyPasswords\s+.*/PermitEmptyPasswords yes/' /etc/ssh/sshd_config && \
    sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -ri 's/^#?ChallengeResponseAuthentication\s+.*/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config

# 1.2 Create entires for password less access 
RUN mkdir -p ~/.ssh && \
    chmod 700 ~/.ssh && \
    ssh-keygen -f ~/.ssh/id_rsa -N '' && \
    cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys && \
    echo "Host * " > ~/.ssh/config && \
    echo "    StrictHostKeyChecking no " >> ~/.ssh/config && \
    chmod 600 ~/.ssh/* 

EXPOSE 22

# Download hadoop Binaries to the Opt

CMD ["/usr/sbin/sshd", "-D"]

