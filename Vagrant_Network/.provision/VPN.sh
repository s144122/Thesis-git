

#sudo apt-get -y install dos2unix
#sudo dos2unix -n /usr/shared/vpnsetup.sh /usr/shared/vpnsetupUnix.sh
#sudo apt-get -y install dos2unix
#sudo -u vagrant -H bash <<EOF

sudo apt-get -y update
sudo apt-get -y install openvpn easy-rsa

cd /home/vagrant/
echo $PWD
make-cadir /home/vagrant/openvpn-ca
echo $PWD
cd /home/vagrant/openvpn-ca
echo $PWD
cp /usr/shared/vars /home/vagrant/openvpn-ca
mv openssl-1.0.0.cnf openssl.cnf
echo $PWD
#dos2unix -n /usr/shared/vars /usr/shared/vars.sh

source vars
./clean-all
#printf '\n\n\n\n\n\n\n'|./build-ca 
#./build-key-server server
#./build-dh
##openvpn --genkey --secret keys/ta.key

#source vars
#./build-key client
#cd /home/vagrant/openvpn-ca/keys
#cp ca.crt ca.key client.crt client.key dh2048.pem /usr/shared/
#cp /usr/shared/server.conf /etc/openvpn/
#sudo openvpn /etc/openvpn/server.conf
