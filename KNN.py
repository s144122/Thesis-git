# Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
from scapy.all import *
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('TkAgg') 
import Read_pcap_scapy
# Loading data
#irisData = load_iris()

file_name = "Thesis-git/Vagrant_Network/server/server_traffic_25s.pcap"
#file_name = "Thesis-git/Vagrant_Network/server/server3_traffic.pcap"
data_file = rdpcap(file_name)
data = Read_pcap_scapy.MakeArrayWithAllFeatures(data_file)
#print(data)
# Create feature and target arrays 
X = data[:,1:]
y = data[:,0] 

#X = irisData.data 
#y = irisData.target 

#print(X)
#print(y)

'''
# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split( 
             X, y, test_size = 0.2, random_state=42) 

knn = KNeighborsClassifier(n_neighbors=7) 
  
knn.fit(X_train, y_train) 

#print(X_test)
#print(y_test)
# Calculate the accuracy of the model 
print('KNN score: {}'.format(knn.score(X_test, y_test)))

print('KNN predict: {}'.format(knn.predict(X_test))) 
'''

# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split( 
             X, y, test_size = 0.2, random_state=42) 
  
neighbors = np.arange(1, 10) 
train_accuracy = np.empty(len(neighbors)) 
test_accuracy = np.empty(len(neighbors)) 

# Loop over K values 
for i, k in enumerate(neighbors): 
    knn = KNeighborsClassifier(n_neighbors=k) 
    knn.fit(X_train, y_train) 
      
    # Compute traning and test data accuracy 
    train_accuracy[i] = knn.score(X_train, y_train) 
    test_accuracy[i] = knn.score(X_test, y_test) 
  
print(train_accuracy)
print(test_accuracy)
# Generate plot 
#plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
#plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 

plt.plot(test_accuracy)
plt.plot(train_accuracy)
plt.ylabel('Accuracy')
plt.legend(["test_accuracy", "train_accuracy"])
plt.show()