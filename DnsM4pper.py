 #!/usr/bin/python
# -*- coding:utf-8 -*-

#Install DNSLib

#git clone https://github.com/rthalley/dnspython
#cd dnspython/
#python setup.py install

import dns
import dns.resolver
import dns.reversename
import socket
import time
import os

cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'
normal = '\033[0;0m'
os.system('clear')

DNSBanner = """
─────███────██
──────████───███
────────████──███
─────────████─█████
████████──█████████
████████████████████
████████████████████
█████████████████████
█████████████████████
█████████████████████
██─────██████████████
███────────█████████
█──█───────────████
█──────────────██
██──────────────█────────▄███████▄
██───███▄▄──▄▄███──────▄██$█████$██▄
██──█▀───▀███────█───▄██$█████████$██▄     ▒█▀▀▄ ▒█▄░▒█ ▒█▀▀▀█ 　 ▒█▀▄▀█ ░█▀█░ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
██──█───█──██───█─█──█$█████████████$█     ▒█░▒█ ▒█▒█▒█ ░▀▀▀▄▄ 　 ▒█▒█▒█ █▄▄█▄ ▒█▄▄█ ▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ 
██──█──────██─────█──█████████████████     ▒█▄▄▀ ▒█░░▀█ ▒█▄▄▄█ 　 ▒█░░▒█ ░░░█░ ▒█░░░ ▒█░░░ ▒█▄▄▄ ▒█░▒█
██──██────██▀█───█─────██████████████
─█───██████──▀████───────███████████
──────────────────█───────█████████
─────────────▀▀████──────███████████
────────────────█▀──────██───████▀─▀█
────────────────▀█──────█─────▀█▀───█
──▄▄▄▄▄▄▄────────██────█───████▀───██
─█████████████────▀█──█───███▀──▄▄██
─█▀██▀██▀████▀█████▀──█───██████▀─▀█
─█────────█▄─────────██───████▀───██
─██▄████▄──██────────██───██──▄▄▄██
──██▄▄▄▄▄██▀─────────██──█████▀───█
─────────███────────███████▄────███
────────███████─────█████████████
───────▄██████████████████████
████████─██████████████████
─────────██████████████
────────███████████
───────█████
──────████
+================================================+
|                  DNSM4PPER                     |
+================================================+
| ♚ Coded: łuŧЋ1єr ルシアー                      |
| ♚ Contact: @Xcultevil (Telegram)               |
| ♚ Date: 07/03/2017                             |
| ♚ Chanell:telegram.me/Phantasm_Lab             |
| ♚ I take no responsibilities for the           |
|   use of this program !                        |
+================================================+
|            łαbørαŧøriø Fαηŧαsмα                |
+================================================+
"""
def DNSMAPPER():
	try:
		print purpleClaro + DNSBanner
		DOMAIN = raw_input(azul +'Digite Seu Dominio: ')
		GHOSTLAB001 = dns.resolver.query(DOMAIN,'A')
		GHOSTLAB000 = dns.resolver.query(DOMAIN, 'MX')
		GHOSTLAB002 = dns.resolver.query(DOMAIN,'NS')
		GHOSTLAB003 = dns.resolver.query(DOMAIN,'AAAA')
		GHOSTLAB004 = dns.resolver.query(DOMAIN,'SOA')
		GHOSTLAB005 = dns.resolver.query(DOMAIN,'TXT')
		print('')
		for ip in GHOSTLAB001:
			time.sleep(0.5)
			print amarelo + "Web Hosting IPV4: ", ip
			print('')

		for MX in GHOSTLAB000:
			print cyanClaro + "Mail Servers:",MX
			time.sleep(0.5)
			print('')

		for Maper in GHOSTLAB002:
			print purpleClaro + "Domains Maper:",Maper
			time.sleep(0.5)
			print('')

		for Lab3 in GHOSTLAB003:
			time.sleep(0.5)
			print verde + "Web Hosting IPV6: ", Lab3
			print('')

		for Lab4 in GHOSTLAB004:
			time.sleep(0.5)
			print vermelho + "Start Of Autority (SOA): ", Lab4
			print('')

		for Lab5 in GHOSTLAB005:
			time.sleep(0.5)
			print cyanClaro + "Text Recording: ",Lab5
		ip = socket.gethostbyname("www."+DOMAIN)
		Reverse = dns.reversename.from_address(ip)
		print('')
		print purpleClaro + "DNS ReverseName: ", Reverse, "\n"
		time.sleep(0.5)
		print purpleClaro + "DNS ReverseName: ", dns.reversename.to_address(Reverse)
		print('')
	except KeyboardInterrupt:
		print vermelho + "[404] Error Not Found! (KeyboardInterrupt)"

DNSMAPPER()


