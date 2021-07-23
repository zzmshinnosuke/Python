'''
Created on Jan 22, 2018

@author: zzm
'''
from socket import *

HOST="192.168.1.100"
PORT=21517
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()