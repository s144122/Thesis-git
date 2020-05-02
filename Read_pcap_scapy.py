from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from scapy.all import *
import numpy as np
import matplotlib.pyplot as plt

##################### Import file #####################
#file_name = "Thesis-git/Vagrant_Network/server/server3_traffic.pcap"
#file_name = "Thesis-git/Vagrant_Network/server/server_traffic_10s.pcap"
#file_name = "Thesis-git/Vagrant_Network/server/server_traffic_15s.pcap"
#packets = rdpcap(file_name)
##################### information about the file #####################
#print('Number of packets {} contained in {}'.format(len(packets),file_name))

##################### extract basis information on a packet ##########################
#pkt = packets[0]
#print(type(pkt))
#print(dir(pkt))
#print(str(pkt))
#print(pkt)
#print(hexdump(pkt))
#print(pkt.show())
#print(pkt.time)
#print(pkt.summary)
#print(pkt[IP].src)
#print(pkt[IP].dst)

##################### TCP Sessions #####################


# Number of sessions in file 
def NumberOfSessions(packets):
    count = 0
    s = packets.sessions()
    vpn = 0
    non_vpn = 0
    for k,v in s.items():
        count = count + 1
        if(k.find('192.168.100.2') != -1):
            vpn = vpn + 1
        if(k.find('192.168.100.3') != -1):
            non_vpn = non_vpn + 1
    print('Number of VPN sessions:      {}'.format(vpn))
    print('Number of non_VPN sessions:  {}'.format(non_vpn))
    print('Total number of sessions:    {}'.format(count))
    return count
#NumberOfSessions(packets)
#Finding the average delay between each packet in every session
def AverageDelayFlow(packets):
    s = packets.sessions()
    AverageDelay = []
    for k,v in s.items():
        delay = 0
        for i in range(len(v)-1):
            p0 = v[i].time
            p1 = v[i+1].time
            delay = delay + (p1 - p0)
        AverageDelay.append([k,float(len(v)),float(delay/len(v))])
    #print(len(AverageDelay))
    #print(AverageDelay)
    return AverageDelay

#should have been the average delay between each packet in every session added with each other so every session that had the same IP addresses
# was added together and divided by the number of occurrences 
'''
def AverageDelaySummedSessions(AverageDelay):
    AverageDelayUniq = []
    for ad in AverageDelay:
        found = False
        for sublist in AverageDelayUniq:
            #print(ad[0])
            #print(sublist[0])
            if sublist[0] == ad[0]:
                found = True
                sublist[1] = sublist[1] + ad[1]
                sublist[2] = sublist[2] + 1
                break
        if (not found):
            AverageDelayUniq.append([ad[0],ad[1],1])
    #print(len(AverageDelayUniq))
    return AverageDelayUniq
'''
#Finding the duration of each flow/conversation
def durationFlow(packets):
    s = packets.sessions()
    duration = []
    for k,v in s.items():
        delay = 0
        d = v[len(v)-1].time - v[0].time
        #print(d)
        duration.append([k,float(d)])
    #print(duration)
    #print(len(duration))
    return duration

#Flow packets per second.
def PacketsPerSecondSession(packets):
    AverageDelay = AverageDelayFlow(packets)
    #print(AverageDelay)
    packetsPerSecond = []
    for session,number,time in AverageDelay:
        if(time > 0):
            packetsPerSecond.append([session,float(1/time)])
        else:
            packetsPerSecond.append([session,0])
    return packetsPerSecond

#Total size of all packets in one direction before the flow turns(one session as a session is only one direction)
#and the total number of packets in each session
def SizeOfSessions(packets):
    s = packets.sessions()
    SizeOfSession = []
    for k,v in s.items():
        TotalSizeOfSession = 0
        for i in range(len(v)):
            TotalSizeOfSession = TotalSizeOfSession + len(v[i])
            AverageSizeOfPacketInSession = TotalSizeOfSession / len(v)
        #print('Session: {}  | Length of session: {}     | Size of session: {}'.format(k,len(v),TotalSizeOfSession))
        SizeOfSession.append([k,float(len(v)),float(TotalSizeOfSession),float(AverageSizeOfPacketInSession)])
    return SizeOfSession

#Flow Bytes per second.
def BytesPerSecondOfSession(packets):
    PacketsPerSecondSessions = PacketsPerSecondSession(packets)
    SizeOfSessionss = SizeOfSessions(packets)
    BytesPerSecondOfSessions = []
    for i in range(len(PacketsPerSecondSessions)):
        BytesPerSecondOfSessions.append([PacketsPerSecondSessions[i][0],float(PacketsPerSecondSessions[i][1])*SizeOfSessionss[i][3]])   
    return BytesPerSecondOfSessions

#Find substring in index 0 in list and output a list only if they contain the substring.
def Findsubstring(list,substring):
    sortedlist = []
    for line in list:
        if (line[0].find(substring) != -1):
            sortedlist.append(line)
    return sortedlist

#Extract values from list to a new list(mostly done for the plot)
def ExtractValuesFromList(list,index):
    values = []
    for line in list:
        values.append(line[index])
    return values

#Makes a plot from a list where it seperates the vpn and non-vpn data
def PlotVPNvsNonVPN(input,index):
    notVPN = Findsubstring(input,'192.168.100.3')
    VPN = Findsubstring(input,'192.168.100.2')
    #print(notVPN)
    #print(VPN)
    notVPN = ExtractValuesFromList(notVPN,index)
    VPN = ExtractValuesFromList(VPN,index)
    #print(notVPN)
    #print(type(notVPN))
    #print(VPN)
    #print(type(VPN))
    
    #f = plt.figure()
    #f.savefig(“name.pdf", bbox_inches='tight')

    plt.plot(notVPN[0:10],'ro')
    plt.plot(VPN[0:10],'o')
    plt.ylabel('Time')
    plt.legend(["notVPN", "VPN"])
    #plt.scatter(list(range(0, len(notVPN))),notVPN)
    #plt.scatter(list(range(0, len(VPN))),VPN)
    
    plt.show()

def MakeArrayWithAllFeatures(packets):
    NumberOfSessionsL = NumberOfSessions(packets)
    AverageDelayFlowL = AverageDelayFlow(packets)
    durationFlowL = durationFlow(packets)
    PacketsPerSecondSessionL = PacketsPerSecondSession(packets)
    SizeOfSessionsL = SizeOfSessions(packets)
    BytesPerSecondOfSessionL = BytesPerSecondOfSession(packets)

    List = []
    for i in range(NumberOfSessionsL):
        if(AverageDelayFlowL[i][0].find('192.168.100.3') != -1):
            List.append([0,AverageDelayFlowL[i][1],AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][2],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
        if(AverageDelayFlowL[i][0].find('192.168.100.2') != -1):
            List.append([1,AverageDelayFlowL[i][1],AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][2],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
    
    array = np.array(List)
    return array

#print('AverageDelayFlow Number of packets in sessions')
#PlotVPNvsNonVPN(AverageDelayFlow(packets),1)
#print('AverageDelayFlow Average Delay of each packets in every session')
#PlotVPNvsNonVPN(AverageDelayFlow(packets),2)
#print('durationFlow Duration of each session')
#PlotVPNvsNonVPN(durationFlow(packets),1)
#print('PacketsPerSecondSession')
#PlotVPNvsNonVPN(PacketsPerSecondSession(packets),1)
#print('SizeOfSessions total size of session')
#PlotVPNvsNonVPN(SizeOfSessions(packets),2)
#print('SizeOfSessions average size of each packet in session')
#PlotVPNvsNonVPN(SizeOfSessions(packets),3)
#print('BytesPerSecondOfSession number of bytes send in a second for each session(the number can be bigger than the actual size because of the length of the session)')
#PlotVPNvsNonVPN(BytesPerSecondOfSession(packets),1)