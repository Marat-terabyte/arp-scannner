#!/usr/bin/env python

import scapy.all as scapy

ip = []
mac = []

def arp_request(ip):
	arp_packet = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
	
	global arp_broadcast
	arp_broadcast = broadcast/arp_packet
	

def send_arp(arp):
	answer_list = scapy.srp(arp_broadcast , timeout = 1)[0]
	print()
	
	for a in answer_list:

		ip_addr = a[1].psrc
		mac_addr = a[1].hwsrc
		
		print(f'''
		-------------------------------------
		|         IP              MAC       |
		-------------------------------------
		
		{ip_addr}           {mac_addr}
		
		''')
	

arp_request('192.168.0.1/24')
send_arp(arp_broadcast)
