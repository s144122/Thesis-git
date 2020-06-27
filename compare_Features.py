import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA 
from sklearn import preprocessing 
from sklearn.preprocessing import StandardScaler
from scapy.all import rdpcap
import matplotlib.pyplot as plt
import Read_pcap_scapy

file_name = "Thesis-git\Vagrant_Network\server\server_traffic_5s.pcap"

data = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name)


featureData = data[:,1:]
target = data[:,0] 
df = pd.DataFrame(featureData)
scaler = StandardScaler()
scaler.fit(df)


StandardScaler(copy=True,with_mean=True,with_std=True)
scaled_data = scaler.transform(df)
#print(scaled_data)

#print(length)
#for i in range(length):
#    plt.plot(featureData[i],'ro')
#plt.ylabel('Time')
#plt.legend(["notVPN", "VPN"])
#plt.scatter(list(range(0, len(notVPN))),notVPN)
#plt.scatter(list(range(0, len(VPN))),VPN)
#plt.show()

#range(len(featureData)
#f.write('{}\n'.format(scaled_data[i]))

#f = open('25s_data.csv', 'w')
#for i in (featureData):
#    f.write(i)
#    f.write('\n')
#f.close()

#f = open('25s_scaled_data.csv', 'w')
#for i in (scaled_data):
#    f.write(i)
#    f.write('\n')

#f.close()


import csv
#print(scaled_data)

with open("5s_scaled_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(scaled_data)