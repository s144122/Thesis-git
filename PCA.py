# Import necessary modules
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA 
from sklearn import preprocessing 
from sklearn.preprocessing import StandardScaler
from scapy.all import rdpcap
import matplotlib.pyplot as plt
import Read_pcap_scapy


# Loading data
file_name = "Thesis-git/Vagrant_Network/server/server_traffic_15s.pcap"

data_file = rdpcap(file_name)
#print(Read_pcap_scapy.NumberOfSessions(data_file))
data = Read_pcap_scapy.MakeArrayWithAllFeatures(data_file)
#print(data)
featureData = data[:,1:]
target = data[:,0] 
df = pd.DataFrame(featureData)
#print(df)
scaler = StandardScaler()
scaler.fit(df)

StandardScaler(copy=True,with_mean=True,with_std=True)
scaled_data = scaler.transform(df)
#print(scaled_data)

pca = PCA(n_components=7)
pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)


#The following code constructs the Scree plot
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
#print("per_var")
#print(per_var)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
 
plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()
 
#the following code makes a fancy looking plot using PC1 and PC2
#pca_df = pd.DataFrame(pca_data, index=[*wt, *ko], columns=labels)
# 
#plt.scatter(pca_df.PC1, pca_df.PC2)
#plt.title('My PCA Graph')
#plt.xlabel('PC1 - {0}%'.format(per_var[0]))
#plt.ylabel('PC2 - {0}%'.format(per_var[1]))
# 
#for sample in pca_df.index:
#    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
# 
#plt.show()
## get the name of the top 10 measurements (genes) that contribute
## most to pc1.
## first, get the loading scores


for i in range(len(pca.components_)):
    loading_scores = pd.Series(pca.components_[i])
    ## now sort the loading scores based on their magnitude
    sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
 
    # get the names of the top 7 genes
    top_features = sorted_loading_scores[0:7].index.values
 
    ## print the gene names and their scores (and +/- sign)
    print("print features for pca {}:".format(i+1))
    print(loading_scores[top_features])
    #print(loading_scores)
