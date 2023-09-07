#!/bin/bash

if [ -f "remote_hosts.txt" ] ; then
 echo " Previous remote_hosts.txt exists. Deleting it ..."
 rm remote_hosts.txt
fi 

# List of host names
hosts=("hadoop-nameNode-1" "hadoop-dataNode-1" "hadoop-dataNode-2" "hadoop-dataNode-3")

# Loop through each host name
for hst in "${hosts[@]}"; do
    # Get the container ID
    container_id=$(docker ps -qf "name=$hst")

    # Check if the container is running
    if [ -z "$container_id" ]; then
        echo "Container $hst is not running."
    else
        # Get the IP address using docker inspect
        ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$container_id")

        # Print the host name and IP address
        echo "$ip  $hst" >> remote_hosts.txt
    fi
done

    if [ -f "remote_hosts.txt" ]; then
        echo "remote_hosts.txt created with content "
        cat remote_hosts.txt 
    else 
        echo "Cluster not Running"
	echo "Exiting  .... "
	exit 
    fi

for hst in "${hosts[@]}"; do
    docker cp remote_hosts.txt $hst:/tmp/
    docker exec -it $hst sh -c  " cat /tmp/remote_hosts.txt >> /etc/hosts " 

    echo "Copied hosts files to : " $hst
done
