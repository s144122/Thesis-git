import urllib.request
import random
import time
import os

List1 = ["http://detectvpn.compute.dtu.dk/","http://detectvpn.compute.dtu.dk/test1.html","http://detectvpn.compute.dtu.dk/test4.html","http://detectvpn.compute.dtu.dk/test5.html","http://detectvpn.compute.dtu.dk/test6.html","http://detectvpn.compute.dtu.dk/test7.html","http://detectvpn.compute.dtu.dk/test8.html","http://detectvpn.compute.dtu.dk/test9.html"]
List2 = ["http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/index.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/page/2/en/index.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/html/index.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/html/shelldoc.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/html/step.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/html/step3.html","http://detectvpn.compute.dtu.dk/test2/httrack2/www.httrack.com/html/step9_opt11.html"]
List3 = ["http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/index.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/uddannelse.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/forskning.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/innovation.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/samarbejde.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/om-dtu.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Om-DTU/Profil.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Uddannelse/Diplomingenior.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Uddannelse/Bachelor.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Uddannelse/Kandidat.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Uddannelse/Phd.html","http://detectvpn.compute.dtu.dk/test3/dtu/www.dtu.dk/Uddannelse/Moed-DTU/Moed-uddannelserne/Online-infoaften.html"]

List = List1 + List2 + List3
#print(len(List))

#vpnpath = '"C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\\vpncli.exe"'
#vpnpath = '"C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.exe"'
vpnpath = r'"C:\Program Files (x86)\NordVPN\NordVPN.exe"'
#os.system("{} -s disconnect".format(vpnpath))
os.system("{} -d".format(vpnpath))
#os.system('taskkill /IM "ProtonVPN.exe" /F')

command = " -c"
#os.system(vpnpath + command)
#os.system("curl https://ipinfo.io/ip")
#time.sleep(20)
#print("VPN IP:")
#os.system("curl https://ipinfo.io/ip")
IP = []
t = 25*60
time_start = time.time()
count = 1
while (time.time()-time_start) < t:
    if 0 == random.randint(0,1):#Without VPN
        print("Waiting / NonVPN connection")
        time.sleep(25)
        print("nonVPN IP:")
        os.system("curl https://ipinfo.io/ip")
        #IP.append(["nonVPN",os.system("curl https://ipinfo.io/ip")])
        for i in range(random.randint(10, 50)):
            rand = random.randint(0, len(List)-1)
            try:
                urllib.request.urlopen(List[rand]).read()
            except:
                pass
            #print(count)
            #count = count + 1
        
    else:#With VPN
        #os.system("{} -s < Thesis-git\\vpninfo.txt".format(vpnpath))
        os.system("{} {}".format(vpnpath,command))
        print("Connecting to VPN")
        time.sleep(25)
        print("VPN IP:")
        os.system("curl https://ipinfo.io/ip")
        #IP.append(["VPN",os.system("curl https://ipinfo.io/ip")])
        for i in range(random.randint(10, 50)):
            rand = random.randint(0, len(List))
            try:
                urllib.request.urlopen(List[rand]).read()
            except:
                pass
            
            #print(count)
            #count = count + 1
        os.system("{} -d".format(vpnpath))
        time.sleep(5)
        os.system("{} -d".format(vpnpath))
        #print(count)

#print(IP)









#os.system("{} -s disconnect".format(vpnpath))