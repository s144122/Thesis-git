#!/bin/bash
# Update Packages
echo "Network traffic generating"
#wget 10.0.100.2
j=0
sudo mkdir tempwebsitefolder
#let list = '10.0.100.2/index.html' '10.0.100.2/pic1.png' '10.0.100.2/pic2.png' '10.0.100.2/pic3jpg' '10.0.100.2/pic4.jpg'


#runtime="5 minute"
runtime="5 seconds"
endtime=$(date -ud "$runtime" +%s)

while [[ $(date -u +%s) -le $endtime ]]
do
	#if [$RANDOM -lt 32767/2]
	sudo rm -rf tempwebsitefolder/*
	ranNum=$[RANDOM%10+1]
	if [ `expr $j % 2` -eq 0 ]
	then #via vpn
		sudo ip route del 10.0.100.0/24 via 192.168.100.1 dev eth1
		sudo ip route add 10.0.100.0/24 via 10.8.0.5 dev tun0
		for i in seq $RANDOM/5000
		do 
			if (( $RANDOM%5 == 0 ))
			then 
				wget -p 10.0.100.2/index.html -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 1 ))
			then 
				wget -p 10.0.100.2/pic1.png -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 2 ))
			then 
				wget -p 10.0.100.2/pic2.png -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 3 ))
			then 
				wget -p 10.0.100.2/pic3.jpg -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 4 ))
			then 
				wget -p 10.0.100.2/pic4.jpg -P tempwebsitefolder/
			fi
			
		done
	else #not via vpn
		sudo ip route del 10.0.100.0/24 via 10.8.0.5 dev tun0
		sudo ip route add 10.0.100.0/24 via 192.168.100.1 dev eth1
		for i in seq $RANDOM/5000
		do 
			#wget -p ${list[`expr $RANDOM % 5` -eq 0]}; -P tempwebsitefolder/
			if (( $RANDOM%5 == 0 ))
			then 
				wget -p 10.0.100.2/index.html -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 1 ))
			then 
				wget -p 10.0.100.2/pic1.png -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 2 ))
			then 
				wget -p 10.0.100.2/pic2.png -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 3 ))
			then 
				wget -p 10.0.100.2/pic3.jpg -P tempwebsitefolder/
			fi
			if (( $RANDOM%5 == 4 ))
			then 
				wget -p 10.0.100.2/pic4.jpg -P tempwebsitefolder/
			fi
		done
	fi
	let "j=j+1"
done