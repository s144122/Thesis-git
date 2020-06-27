# Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
#from sklearn.datasets import load_iris
from scapy.all import rdpcap
import numpy as np 
import matplotlib.pyplot as plt
import joblib as joblib
#import matplotlib
import Read_pcap_scapy
import pickle


# Loading data test data
file_name_test = "Thesis-git\Vagrant_Network\server\server_traffic_20s_new.pcap"

# Loading traning data
#file_name_traning = "Thesis-git\Vagrant_Network\server\server_traffic_5m.pcap"



#data_file = rdpcap(file_name)
#data_train = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name_traning)
#np.save("array.npy", data_train)
#with open('outfile', 'wb') as fp:
#    pickle.dump(data_train, fp)

with open ('outfile', 'rb') as fp:
    data_train_load = pickle.load(fp)

# Create feature and target arrays 
X_train = data_train_load[:,1:]
y_train = data_train_load[:,0]

# Split into training and test set 
#X_train, X_test, y_train, y_test = train_test_split( 
#             X, y, test_size = 0.4, random_state=42)

data_test = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name_test)
X_test = data_test[:,1:]
y_test = data_test[:,0] 

neighbors = np.arange(1, 20) 
#train_accuracy = np.empty(len(neighbors)) 
test_accuracy = np.empty(len(neighbors)) 

# Loop over K values 
for i, k in enumerate(neighbors): 
    knn = KNeighborsClassifier(n_neighbors=k) 
    knn.fit(X_train, y_train) 
      
    # Compute test data accuracy 
    test_accuracy[i] = knn.score(X_test, y_test) 
  
#print(train_accuracy)
print(test_accuracy)
# Generate plot 
#plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
#plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 

#plt.plot(test_accuracy)
#plt.plot(train_accuracy)
#plt.ylabel('Accuracy')
#plt.legend(["test_accuracy", "train_accuracy"])
#plt.show()






#file_name = "Thesis-git\Vagrant_Network\server\server_traffic_5m.pcap"
#data = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name)

## Create feature and target arrays 
#X = data[:,1:]
#y = data[:,0] 

#knn = KNeighborsClassifier(n_neighbors=7)
#knn.fit(X, y)

## Save the model as a pickle in a file 
#joblib.dump(knn, 'knnModel.pkl') 
  
## Load the model from the file 
#knn_from_joblib = joblib.load('knnModel.pkl')  

## Calculate the accuracy of the model 
#print('KNN score: {}'.format(knn_from_joblib.score(X, y)))