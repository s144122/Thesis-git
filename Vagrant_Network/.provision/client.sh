#!/bin/bash

# Update Packages
apt-get update
#sudo apt-get -y install dos2unix
sudo apt-get -y install openvpn
sudo apt-get -y install traceroute
sudo apt-get -y install nmap

cp /usr/shared/openvpn-ca/keys/ca.crt /usr/shared/openvpn-ca/keys/client.crt /usr/shared/openvpn-ca/keys/client.key /etc/openvpn
cp /usr/shared/client.conf /etc/openvpn
cd /etc/openvpn
sudo systemctl enable openvpn@client
sudo systemctl start openvpn@client
sudo systemctl status openvpn@client


#These three commands doesn't run when starting vagrant. It can't find tun0
sudo ip route del 128.0.0.0/1 via 10.8.0.5 dev tun0
sudo ip route del 192.168.100.2/32 via 10.0.2.2 dev eth0
sudo ip route add 10.0.100.0/24 via 10.8.0.5 dev tun0
#sudo ifconfig tun0 10.8.0.2/32 pointopoint 10.8.0.1



#ip route del default via _gateway
#ip route add default via 10.8.0.6 dev tun0


#ip route add 10.0.100.0/24 via 10.8.0.6 dev tun0
# ip route add 10.0.100.0/24 via 192.168.100.1 dev eth1

#ip route del default via 10.8.0.6 dev tun0
#ip route add default via _gateway




#cat client.conf   <(echo -e '<ca>') /usr/shared/openvpn-ca/keys/ca.crt <(echo -e '</ca>')   <(echo -e '<cert>') /usr/shared/openvpn-ca/keys/client.crt <(echo -e '</cert>n')   <(echo -e '<key>') /usr/shared/openvpn-ca/keys/client.key <(echo -e '</key>n')>> client.ovpn