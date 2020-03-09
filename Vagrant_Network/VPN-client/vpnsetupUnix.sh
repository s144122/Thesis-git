#sudo -u vagrant -H bash <<EOF

sudo apt-get -y update
sudo apt-get -y install openvpn easy-rsa
make-cadir /home/vagrant/openvpn-ca
#sudo cd ~/openvpn-ca
cp /usr/shared/vars /home/vagrant/openvpn-ca/
mv /home/vagrant/openvpn-ca/openssl-1.0.0.cnf /home/vagrant/openvpn-ca/openssl.cnf
source vars
/home/vagrant/openvpn-ca/clean-all


#/home/vagrant/openvpn-ca/build-ca
#/home/vagrant/openvpn-ca/build-key-server vpnserver -y
#/home/vagrant/openvpn-ca/build-dh
#openvpn --genkey --secret keys/ta.key
#source vars
#/home/vagrant/openvpn-ca/build-key client1
#cd ~/openvpn-ca/keys
#sudo cp ca.crt ca.key vpnserver.crt vpnserver.key ta.key dh2048.pem /etc/openvpn
#gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz | sudo tee /etc/openvpn/server.conf

#sudo nano /etc/openvpn/server.conf

#EOF