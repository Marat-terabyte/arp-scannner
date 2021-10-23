#!/usr/bin/env python3

import scapy.all as scapy
from colorama import Fore
import os

if os.getuid() != 0:
    print(Fore.RED + '[!] You are not root!\n\tUse "sudo"')
    quit()


def assembly_packet(ip):
    ip = str(ip + '/24')
    arp_packet = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')

    arp = broadcast / arp_packet

    del ip, arp_packet, broadcast

    return arp

def send_and_get_data(ip):
    answered_list = scapy.srp(assembly_packet(ip), timeout = 10, verbose = False)[0]

    print('''
---------------------------------
|     IP              MAC       |
---------------------------------
    ''')

    for i in answered_list:
        print(f'{i[1].psrc}\t{i[1].hwsrc}')

ip = input('[!] Enter IP:')


if __name__ == '__main__':
    send_and_get_data(ip)
