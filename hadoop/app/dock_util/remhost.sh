hst=hadoop-nameNode-1
remIp=$(ssh hadoop@$hst ifconfig | grep inet | grep -v 127| tr -s ' '| cut -d ' ' -f3) ;
echo $remIp $hst >> host 

for hst in `cat workers`; do remIp=$(ssh hadoop@$hst ifconfig | grep inet | grep -v 127| tr -s ' '| cut -d ' ' -f3) ; echo $remIp $hst >> host ; done 
