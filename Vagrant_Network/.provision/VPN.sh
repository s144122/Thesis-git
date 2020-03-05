#!/bin/bash

# Update Packages
apt-get update
apt-get upgrade


#wget https://git.io/vpn -O openvpn-install.sh
#chmod +x openvpn-install.sh


#install VPN server and setup
wget git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh 10.0.0.30 10.0.0.60 1 1194 1 client 
cp /root/client.ovpn /usr/shared/

systemctl status openvpn-server@server.service

#systemctl enable openvpn-server@server.service
#sudo systemctl start openvpn@server # <--- start server

