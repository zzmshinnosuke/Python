'''
Created on Jan 22, 2018

@author: zzm
'''
from socket import *
from time import ctime

HOST='192.168.1.100'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s'% (ctime(),data),addr)
    print '...received from and returned to:', addr, data

udpSerSock.close()

