import socket
import select

class server1():
    def __init__(self):
        self.ipp = ""
        self.port = 40000
        self.buffer = 4
        self.clients = []

    def inits(self):
        
        self.serverm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.serverm.bind((self.ipp,self.port)) 
        self.serverm.listen(self.buffer)

    def start(self):
        
        self.inits()
        try:
            lesen, schreiben, oob = select.select([self.serverm] + clients, [], [])


            for self.sock in lesen: 
                if self.sock is self.serverm: 
                    client, addr = self.serverm.accept() 
                    self.clients.append(client) 
                    print ("+++ Client %s verbunden" % addr[0])
                else: 
                    nachricht = self.sock.recv(1024) 
                    ip = self.sock.getpeername()[0] 
                    if nachricht: 
                        print ("[%s] %s" % (ip, nachricht)) 
                    else: 
                        print ("+++ Verbindung zu %s beendet" % ip) 
                        self.sock.close() 
                        clients.remove(self.sock) 
        finally: 
            for c in self.clients: 
                c.close() 
            self.serverm.close()

