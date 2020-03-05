#!/bin/bash

# Update Packages
#apt-get update

echo "Hello world"
sudo apt-get -y install dos2unix
sudo apt-get -y install openvpn

sudo cp /usr/shared/client.ovpn /etc/openvpn/client.conf
#sudo openvpn --client --config /etc/openvpn/client.conf
dos2unix -n /usr/shared/traffic.sh /usr/shared/trafficUnix.sh
#sudo systemctl start openvpn@client










#bash /usr/shared/trafficUnix.sh
# while :
# do
	# if $RANDOM > 32767/2
	# then #to vpn
		# ip route del default  
		# ip route add default via 10.0.0.30
		# for i in seq $RANDOM
		# do
			# #wget 10.0.0.10
			# curl 10.0.0.10 
		# done
	# else #to router
		# ip route del default  
		# ip route add default via 10.0.0.40
		# for i in seq $RANDOM
		# do
			# #wget 10.0.0.10
			# curl 10.0.0.10
		# done
	# fi
# done