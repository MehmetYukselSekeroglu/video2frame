#!/usr/bin/env
OS_INFO_FILE="/etc/os-release"

printf "[+] Sistem bilgisi ${OS_INFO_FILE} dosyasından alınıyor...\n"

source $OS_INFO_FILE


if [[ "$ID_LIKE" = "debian" ]] ;then
	printf "[+] python3 ve python3-opencv apt kullanılarak indiriliyor...\n"
	sudo apt install -y python3 python3-opencv 1> /dev/null 
	if [ "$?" != "0" ] ;then
		printf "[-] İşlem başarısız oldu. \n"
		exit 1
	else 
		printf "[+] İşlem balarıyla tamamlandı...\n"
		exit 0
	
	fi
else 
	printf "[+] Sistem debian değildir lütfen python3 ve python3-opencv paketlerini elle kurunuz..\n"
	exit 0

fi	


 
