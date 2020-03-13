#!/bin/bash

# Update Packages
apt-get update
sudo apt-get install iptables

sudo iptables -F
sudo iptables -L -n
sudo iptables -A FORWARD -d 10.0.0.10 -j ACCEPT
sudo iptables -A FORWARD -s 10.0.0.10 -j ACCEPT



