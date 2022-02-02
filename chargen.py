import sys
from scapy.all import *
dstIP = input()
send(IP(dst=dstIP)/UDP(dport=19,sport=19)/Raw(load="who is out there?"))