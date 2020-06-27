# Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier 
import joblib as joblib
import Read_pcap_scapy

file_name = "Thesis-git\Vagrant_Network\server\server_traffic_2m.pcap"
#file_name = "Thesis-git\DTU_server\dtu_server_nordvpn_25m.pcap"


data = Read_pcap_scapy.FindFeaturesInLargeFiles(file_name)
#print(data[0:10])

## Create feature and target arrays 
X = data[:,1:]
y = data[:,0] 
  
## Load the model from the file 
knn_from_joblib = joblib.load('knnModel_7neighbor_5m.pkl')  

## Calculate the accuracy of the model 
print('KNN score: {}'.format(knn_from_joblib.score(X, y)))


print('Predict')
#print(knn_from_joblib.predict(X))

true_negativ = 0
false_negativ = 0
true_positive = 0
false_positive = 0

#f = open('predict.csv', 'w')
predict = knn_from_joblib.predict(X)
for i in range(len(predict)):
    if (predict[i] == 0 and y[i] == 0):
        true_negativ = true_negativ + 1
        #f.write('{}\n'.format(0))
    if (predict[i] == 0 and y[i] == 1):
        false_negativ = false_negativ + 1
        #f.write('{}\n'.format(1))
    if (predict[i] == 1 and y[i] == 1):
        true_positive = true_positive + 1
        #f.write('{}\n'.format(2))
    if (predict[i] == 1 and y[i] == 0):
        false_positive = false_positive + 1
        #f.write('{}\n'.format(3))
#f.close()
print("true_negativ: {}".format(true_negativ))
print("false_negativ: {}".format(false_negativ))
print("true_positive: {}".format(true_positive))
print("false_positive: {}".format(false_positive))