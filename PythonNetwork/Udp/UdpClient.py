'''
Created on Jan 22, 2018

@author: zzm
'''

from socket import *

HOST='192.168.1.100'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('> ')
    if not data:
        break;
    udpCliSock.sendto(data,ADDR)
    data,ADDR=udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data
udpCliSock.close()