import socket


 

class server1():
    def __init__(self,ipp):
        self.ipp = ipp
        self.port = 40000


    def inits(self):
        
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.c.connect((self.ipp, self.port))

    def send(self, text):
        inits()
        try: 
            while True: 
                nachricht = str(text).encode(encoding="UTF-8",errors="ignore") 
                self.c.send(nachricht) 
        finally:

            self.c.close()
