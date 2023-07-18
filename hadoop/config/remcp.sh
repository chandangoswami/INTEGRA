for fil in `echo hadoop-env.sh core-site.xml hdfs-site.xml yarn-site.xml mapred-site.xml workers`
do 
	echo Coping file $fil;
	rcp  $fil hadoop@hadoop-dataNode-1:/home/hadoop/hadoop-3.2.2/etc/hadoop/ 
	rcp  $fil hadoop@hadoop-dataNode-2:/home/hadoop/hadoop-3.2.2/etc/hadoop/ 
	rcp  $fil hadoop@hadoop-dataNode-3:/home/hadoop/hadoop-3.2.2/etc/hadoop/ 
done
