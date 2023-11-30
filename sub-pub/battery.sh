#! /bin/sh

for itr in `seq 5`
  do 
	  echo Iternation number $itr 
	  node kafka_prod.js & 
  done
