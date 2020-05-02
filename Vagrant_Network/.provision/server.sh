#!/usr/bin/env bash
sudo apt-get update
# nginx intall
sudo apt-get -y install nginx
sudo service nginx start

# set up nginx server
sudo cp /vagrant/.provision/nginx/nginx.conf /etc/nginx/sites-available/site.conf
sudo chmod 644 /etc/nginx/sites-available/site.conf
sudo ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/site.conf

sudo cp /usr/shared/html/* /var/www/html

sudo service nginx restart



# clean /var/www
#sudo rm -Rf /var/www

# symlink /var/www => /vagrant
#ln -s /vagrant /var/www

# seing the network traffic if on VM
sudo apt-get install iftop 

sudo ip route add 192.168.100.0/24 via 10.0.100.1 dev eth1



#sudo tcpdump -i eth1
#sudo tcpdump -i eth1 -w server1_traffic_30s.pcap