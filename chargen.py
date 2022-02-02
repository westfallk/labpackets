import sys
from scapy.all import *
def sendPacketWithSrc(dstIP, srcIP):
    send(IP(dst=dstIP, src=srcIP)/UDP(dport=19,sport=19)/Raw(load="who is out there?"))
def sendPacket(dstIP):
    send(IP(dst=dstIP)/UDP(dport=19,sport=19)/Raw(load="who is out there?"))


userIn = input()
ipArr = userIn.split(' ')
if(len(ipArr)>2):
    print("pass in two IPs in dotted decimal notation seperated by a space")
elif(len(ipArr)==2):
    sendPacketWithSrc(ipArr[0],ipArr[1])
else:
    sendPacket(ipArr[0])

