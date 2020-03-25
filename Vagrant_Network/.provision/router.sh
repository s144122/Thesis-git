#!/bin/bash

# Update Packages
apt-get update
#sudo apt-get install iptables

sudo sysctl -w net.ipv4.ip_forward=1

