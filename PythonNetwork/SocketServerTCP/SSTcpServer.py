'''
Created on Jan 22, 2018

@author: zzm
'''

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import  ctime

HOST='192.168.1.100'
PORT=21556
ADDR=(HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        data=self.rfile.readline()
        print '...connected from:', self.client_address,data
        self.wfile.write('[%s] %s' % (ctime(),data))
        
tcpServ=TCP(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
