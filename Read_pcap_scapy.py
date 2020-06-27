from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from scapy.all import *
import numpy as np
import matplotlib.pyplot as plt
from pcap_splitter.splitter import PcapSplitter
import os
import os, re, os.path
import glob
##################### Import file #####################
#file_name = "Thesis-git/Vagrant_Network/server/server3_traffic.pcap"
#file_name = "Thesis-git/Vagrant_Network/server/server_traffic_10s.pcap"
#file_name = "Thesis-git\Vagrant_Network\server\server_traffic_25s.pcap"
#file_name = "Thesis-git\DTU_server\dtu_server_nordvpn_5m.pcap"

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

vpn_ip = '192.168.100.2'
nonvpn_ip = '192.168.100.3'


VPN_IP_List5m = ["37.120.194.215","37.120.131.76","37.120.194.204","193.36.116.178"]
VPN_IP_List7m = ["37.120.131.142","185.212.169.100","185.236.203.92","37.120.194.236","45.12.221.220","37.120.194.204","37.120.194.236"]
VPN_IP_List10m = ["37.120.131.228","193.36.116.178","37.120.194.204","193.36.116.170"]
VPN_IP_List12m = ["37.120.194.135","37.120.131.142","37.120.194.218","37.120.194.228","37.120.194.138","185.245.84.180","82.211.198.175","37.120.194.204","37.120.194.144"]
VPN_IP_List15m = ["185.245.84.164","37.120.194.180","37.120.194.141","37.120.131.142","37.120.131.155","82.102.20.211","45.12.221.220"]
VPN_IP_List17m = ["82.102.20.235","37.120.194.228","185.245.84.164","37.120.194.212","37.120.131.220","37.120.131.228","45.12.221.220","37.120.131.142","2.58.46.230","2.58.46.236","37.120.131.132","2.58.46.230"]
VPN_IP_List20m = ["37.120.131.196","37.120.131.220","193.36.116.180","37.120.131.142","37.120.194.4","37.120.194.135","185.245.84.84","185.245.84.188","37.120.131.228","2.58.46.236","82.102.20.235"]
VPN_IP_List25m = ["37.120.194.4","2.58.46.230","45.12.221.220","37.120.194.236","37.120.131.132","37.120.131.204","37.120.131.137","37.120.194.153","185.236.203.92","185.245.84.172","185.245.84.164","37.120.131.142","37.120.194.188","37.120.194.135","185.245.84.244","45.12.221.212"]

#VPN_IP_List = VPN_IP_List5m + VPN_IP_List7m + VPN_IP_List10m + VPN_IP_List12m + VPN_IP_List15m + VPN_IP_List17m + VPN_IP_List20m + VPN_IP_List25m
#nonvpn_ip = "82.211.198.175"





# Number of sessions in file 
def NumberOfSessions(packets):
    count = 0
    Sessions = packets.sessions()
    vpn = 0
    non_vpn = 0
    for Session_info,Session_packets in Sessions.items():
        count = count + 1
        #print(Session_info)
        #if(substringInList(VPN_IP_List,Session_info) == True):
        #    vpn = vpn + 1
        #if(Session_info.find(nonvpn_ip) != -1):
        #    non_vpn = non_vpn + 1
    #print('Number of VPN sessions:      {}'.format(vpn))
    #print('Number of non_VPN sessions:  {}'.format(non_vpn))
    #print('Total number of sessions:    {}'.format(count))
    #List =[]
    #for Session_info,Session_packets in Sessions.items():
    #    start   = " "
    #    end     = ">"
    #    ip = Session_info[Session_info.find(start)+len(start):Session_info.rfind(end)]
        #if (Session_info not in List and Session_info.find('ARP') == -1):
            #print(Session_info)
            #List.append(Session_info)
        #if (Session_info.find('82.211.198.175') == -1 and Session_info.find('ARP')):
            #print(Session_info)
        #if (Session_info.find('10.13.') != -1 and Session_info.find('ARP') == -1):
        #    start   = " "
        #    end     = ">"
        #    ip = Session_info[Session_info.find(start)+len(start):Session_info.rfind(end)]
        #    print(ip)    
        #for packet in Session_packets:
            #ip = (IP(packet).src, ">", IP(packet).dst, "|", Session_info)
            #ip = Session_info.src
        #    start   = " "
        #    end     = ">"
        #    ip = Session_info[Session_info.find(start)+len(start):Session_info.rfind(end)]
            #print(IP(packet).src, ">", IP(packet).dst, "|", Session_info)
        #    if(ip not in List and Session_info.find('ARP')):
        #        List.append(ip)
        #        print(ip)
    
    #print(List)
    return count
#NumberOfSessions(packets)


#Finding the average delay between each packet in every session
def AverageDelayFlow(packets):
    Sessions = packets.sessions()
    AverageDelay = []
    for Session_info,Session_packets in Sessions.items():
        delay = 0
        for i in range(len(Session_packets)-1):
            p0 = Session_packets[i].time
            p1 = Session_packets[i+1].time
            delay = delay + (p1 - p0)
        AverageDelay.append([Session_info,float(len(Session_packets)),float(delay/len(Session_packets))])
    #print(len(AverageDelay))
    #print(AverageDelay)
    return AverageDelay

#Finding the duration of each flow/conversation
def durationFlow(packets):
    Sessions = packets.sessions()
    duration = []
    for Session_info,Session_packets in Sessions.items():
        delay = 0
        d = Session_packets[len(Session_packets)-1].time - Session_packets[0].time
        #print(d)
        duration.append([Session_info,float(d)])
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
    Sessions = packets.sessions()
    SizeOfSession = []
    for Session_info,Session_packets in Sessions.items():
        TotalSizeOfSession = 0
        for i in range(len(Session_packets)):
            TotalSizeOfSession = TotalSizeOfSession + len(Session_packets[i])
            AverageSizeOfPacketInSession = TotalSizeOfSession / len(Session_packets)
        #print('Session: {}  | Length of session: {}     | Size of session: {}'.format(Session_info,len(Session_packets),TotalSizeOfSession))
        SizeOfSession.append([Session_info,float(len(Session_packets)),float(TotalSizeOfSession),float(AverageSizeOfPacketInSession)])
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

#A function that calls all the functions with features and places them in a list with only the values
def MakeArrayWithAllFeatures(packets):

    NumberOfSessionsL = NumberOfSessions(packets)
    AverageDelayFlowL = AverageDelayFlow(packets)
    durationFlowL = durationFlow(packets)
    PacketsPerSecondSessionL = PacketsPerSecondSession(packets)
    SizeOfSessionsL = SizeOfSessions(packets)
    BytesPerSecondOfSessionL = BytesPerSecondOfSession(packets)

    List = []
    for i in range(NumberOfSessionsL):
        if(AverageDelayFlowL[i][0].find(nonvpn_ip) != -1):
            List.append([0,AverageDelayFlowL[i][1],AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][2],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
            #List.append([0,AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
            #List.append([0,AverageDelayFlowL[i][2],PacketsPerSecondSessionL[i][1]])
        #if(substringInList(VPN_IP_List,AverageDelayFlowL[i][0]) == True):
        if(AverageDelayFlowL[i][0].find(vpn_ip) != -1):
            List.append([1,AverageDelayFlowL[i][1],AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][2],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
            #List.append([1,AverageDelayFlowL[i][2],durationFlowL[i][1],PacketsPerSecondSessionL[i][1],SizeOfSessionsL[i][3],BytesPerSecondOfSessionL[i][1]])
            #List.append([1,AverageDelayFlowL[i][2],PacketsPerSecondSessionL[i][1]])

        #array = np.array(List)
    return List


def substringInList(List, String):
    for i in List:
        if (String.find(i) != -1):
            return True
    return False


def FindFeaturesInLargeFiles(file_name):
    path = "D:\sessions/"
    # Create folder if it doesn't exist
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    # Split the large file unto smaller files one for each bi-directional session
    # Only 
    os.system("SplitCap.exe -r {} -s session -o {}".format(file_name,path))

    # Make a list of the path of each of the pcap files in the path
    file_names = glob.glob(path+"*.pcap")
    List = []
    #Use the files and combined the features in the array
    count = 1
    length = len(file_names)
    for f in file_names:
        print("{} out of {}".format(count,length))
        packets = rdpcap(f)
        for i in MakeArrayWithAllFeatures(packets):
            List.append(i)
        #print("List")
        count = count + 1

    ## Remove files
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))
    
    array = np.array(List)
    return array


#print(FindFeaturesInLargeFiles(file_name))


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