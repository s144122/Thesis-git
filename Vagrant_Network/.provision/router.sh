#!/bin/bash

# Update Packages
sudo apt-get update
#sudo apt-get install iptables

sudo sysctl -w net.ipv4.ip_forward=1

#sudo tcpdump -i eth1 -w router1_traffic_30s.pcap