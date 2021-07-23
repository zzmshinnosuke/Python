'''
Created on Jan 22, 2018

@author: zzm
'''

from socket import *

HOST='192.168.1.100'
PORT=21556
BUFSIZ=1024
ADDR=(HOST,PORT)
  
while True:
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data=tcpCliSock.recv(BUFSIZ)
    
    if not data:
        break
    print data.strip()

tcpCliSock.close()