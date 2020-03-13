#!/bin/bash

# Update Packages
apt-get update
#sudo apt-get -y install dos2unix
sudo apt-get -y install openvpn

#dos2unix -n /usr/shared/traffic.sh /usr/shared/trafficUnix.sh


cp /usr/shared/ca.crt /usr/shared/client.crt /usr/shared/client.key /etc/openvpn
cp /usr/shared/client.conf /etc/openvpn
cd /etc/openvpn
sudo openvpn /etc/openvpnclient.conf
