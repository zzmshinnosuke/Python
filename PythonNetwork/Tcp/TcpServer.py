'''
Created on Jan 22, 2018

@author: zzm
'''
from socket import *
from time import ctime

HOST='192.168.1.100'
PORT=21517
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection ....'
    tcpCliSock,addr=tcpSerSock.accept()
    print '...connected from:', addr
    
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break;
        tcpCliSock.send('[%s] %s'%(ctime(),data))
    tcpCliSock.close()
tcpSerSock.close()
    