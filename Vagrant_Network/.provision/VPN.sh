

#sudo apt-get -y install dos2unix
#sudo dos2unix -n /usr/shared/vpnsetup.sh /usr/shared/vpnsetupUnix.sh

#sudo -u vagrant -H bash <<EOF
cd /home/vagrant/
echo $PWD
sudo apt-get -y update
sudo apt-get -y install openvpn easy-rsa
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
#cp /usr/shared/vars /home/vagrant/openvpn-ca/
#mv /home/vagrant/openvpn-ca/openssl-1.0.0.cnf /home/vagrant/openvpn-ca/openssl.cnf
cp /usr/shared/vars ~/openvpn-ca/
cat vars
mv openssl-1.0.0.cnf openssl.cnf
echo $PWD
source vars
./clean-all
./build-ca
#/home/vagrant/openvpn-ca/build-key-server vpnserver -y
#/home/vagrant/openvpn-ca/build-dh
#openvpn --genkey --secret keys/ta.key
#source vars
#/home/vagrant/openvpn-ca/build-key client1
#cd ~/openvpn-ca/keys
#echo $PWD
#sudo cp ca.crt ca.key vpnserver.crt vpnserver.key ta.key dh2048.pem /etc/openvpn
#gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz | sudo tee /etc/openvpn/server.conf
#cp /usr/shared/server.conf /etc/openvpn/
#sudo nano /etc/openvpn/server.conf

#EOF