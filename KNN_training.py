# Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier 
#from sklearn.model_selection import train_test_split 
#from scapy.all import rdpcap

import joblib as joblib
import Read_pcap_scapy

# Loading data test data
file_name = "Thesis-git\Vagrant_Network\server\server_traffic_5m.pcap"
#file_name = "Thesis-git\DTU_server\dtu_server_nordvpn_25m.pcap"
data = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name)
#print(data)
## Create feature and target arrays 
X = data[:,1:]
y = data[:,0] 

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X, y)

## Save the model as a pickle in a file 
joblib.dump(knn, 'knnModel_7neighbor_5m.pkl') 