from scapy.all import *

packet = IP(dst="example.com")/ICMP()
send(packet)
