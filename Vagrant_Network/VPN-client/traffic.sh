#!/bin/bash

# Update Packages
#apt-get update
#wget 10.0.0.10
echo "Hello world"

while :
do
	if [$RANDOM -lt 32767/2]
	then #to vpn
		ip route del default  
		ip route add default via 10.0.0.30
		for i in seq $RANDOM
		do
			curl 10.0.0.10 
		done
	else #to router
		ip route del default  
		ip route add default via 10.0.0.40
		for i in seq $RANDOM
		do
			curl 10.0.0.10
		done
	fi
done