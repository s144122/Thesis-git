#!/bin/bash

# Update Packages
apt-get update
sudo apt-get install iptables
sysctl net.ipv4.ip_forward=1


iptables-F

#iptables -t nat -A OUTPUT -d 10.0.0.20 -j DNAT --to-destination 10.0.0.10
iptables -t nat -A POSTROUTING -o ethx -j MASQUERADE

iptables-save



