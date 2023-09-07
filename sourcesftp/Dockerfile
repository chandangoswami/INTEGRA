# Use a base image with a Linux distribution of your choice
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Set up a user for SFTP
RUN useradd -m -d /home/hadoop -s /usr/bin/bash hadoop

# Set the password for the user (Change this in a production environment)
RUN echo 'hadoop:bpt799' | chpasswd

# Allow SFTP access only
RUN echo "Match User hadoop" >> /etc/ssh/sshd_config && \
    echo "    PasswordAuthentication yes" >> /etc/ssh/sshd_config && \
    echo "    ChrootDirectory /home/hadoop" >> /etc/ssh/sshd_config && \
    echo "    ForceCommand internal-sftp" >> /etc/ssh/sshd_config && \
    echo "    ClientAliveInterval   300" >> /etc/ssh/sshd_config && \
    echo "    ClientAliveCountMax   3" >> /etc/ssh/sshd_config 

# Expose SSH port
EXPOSE 22

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]

