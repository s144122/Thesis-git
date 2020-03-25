#!/bin/bash
#https://community.openvpn.net/openvpn/wiki/BridgingAndRouting

#sudo apt-get -y install dos2unix
#sudo dos2unix -n /usr/shared/vpnsetup.sh /usr/shared/vpnsetupUnix.sh
#sudo apt-get -y install dos2unix
#sudo -u vagrant -H bash <<EOF
#./build-ca << /usr/shared/input.txt
#dos2unix -n /usr/shared/vars /usr/shared/vars.sh
#sudo apt-get -y install expect

sudo apt-get -y update
sudo apt-get -y install openvpn easy-rsa


cd /home/vagrant/
make-cadir /home/vagrant/openvpn-ca
cp -avr /usr/shared/openvpn-ca /home/vagrant/
cd /home/vagrant/openvpn-ca/keys
sudo cp ca.key ca.crt server.crt server.key dh2048.pem /etc/openvpn
cp /usr/shared/server.conf /etc/openvpn/
sudo systemctl enable openvpn@server
sudo systemctl start openvpn@server
sudo systemctl status openvpn@server

sudo ip route add 10.0.100.0/24 via 192.168.100.1 dev eth1
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -I POSTROUTING -o eth1 -s 10.8.0.0/24 -j MASQUERADE



#sudo openvpn /etc/openvpn/server.conf
#make-cadir /home/vagrant/openvpn-ca
#cd /home/vagrant/openvpn-ca
#cp /usr/shared/vars /home/vagrant/openvpn-ca
#mv openssl-1.0.0.cnf openssl.cnf

#source vars
#./clean-all
#echo -e "\n\n\n\n\n\n\n"|./build-ca 
#echo -e "\n\n\n\n\n\n\n\ny\ny\n"|./build-key-server server
# ./build-dh
# openvpn --genkey --secret keys/ta.key

# source vars
# echo -e "\n\n\n\n\n\n\n\n\n\ny\ny\ny\n"|./build-key client
# cd /home/vagrant/openvpn-ca/keys
# cp ca.crt client.crt client.key dh2048.pem /usr/shared/
# cp /usr/shared/server.conf /etc/openvpn/
# sudo openvpn /etc/openvpn/server.conf

# sudo ip route add 10.0.100.0/24 via 192.168.100.1 dev eth1

#cp -avr /home/vagrant/openvpn-ca /usr/shared
