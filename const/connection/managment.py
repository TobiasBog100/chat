from os.path import abspath
from time import time
from os import system
from os import listdir
from time import sleep

class send():

    def __init__(self,name, color,message):
        self.name = name
        self.color = color
        self.message = message.replace("\n","")
        self.filen = "/skole/tjener/home0/niko115/chat/data/chats/main.txt"
        self.filet = "/skole/tjener/home0/niko115/chat/data/var/"

        #self.filen = "I:/002_Befehlslisten/chat/structur/chat/data/chats/main.txt"
        #self.filet = "I:/002_Befehlslisten/chat/structur/chat/data/var/"

        self.sendline()


    def sendline(self):


        s = str([self.name,self.color,self.message])+"\n"
        self.insert(self.filen,s)

    def insert(self,filename,s):
            try:
                f = open(self.filen,"r")
                f.close()
            except:
                f = open(self.filen,"w")
                f.write("")
                f.close()

            count=0
            boo = True
            while boo and count<1000:
                if True:#try:
                    f = open(self.filen,"r")
                    f.seek(0,0)
                    content = f.read()
                    f.close()
                    f = open(self.filen,"w")
                    f.write((s+content))
                    f.close()
                    boo = False
                #except:
                    count +=1

                othertime = ((listdir(self.filet))[0]).replace(".txt","")
                owntime = str(time()).replace(".","")

                if len(othertime)<15:
                    othertime = othertime + "0"

                if len(owntime)<15:
                    owntime =  owntime + "0"

                s1 = self.filet + othertime + ".txt"
                s2 = owntime + ".txt"
                ren = "rename " + s1 + " " + s2
                #ren = ren.replace("/","\\")
                print(ren)
                system(ren)



class get():

    def __init__(self):
        self.content = ""
        self.folder = (abspath(".")).replace("const/connection","")
        self.filen = "/skole/tjener/home0/niko115/chat/data/chats/main.txt"
        #self.filen = "I:/002_Befehlslisten/chat/structur/chat/data/chats/main.txt"

        self.getline()

    def getline(self):

        boo = True
        count=0
        self.folder = self.folder + "/data/chats/main.txt"
        while boo and count<1000:
            #try:
                i = 0
                fo = open(self.folder, "r")
                compare = fo.readline()

                fo.close()

                f = open(self.filen ,"r")
                while i<20000:
                    save = f.readline()

                    if save == compare or save =="" :
                        break
                    else:
                        self.content = self.content + save
                    sleep(1)
                    i += 1

                f.close()

                self.insert(self.folder,self.content)


                boo=False
                sleep(1)
                
            #except:
                #count +=1

    def insert(self,filename,s):
            try:
                f = open(filename,"r")
                f.close()
            except:
                f = open(filename,"w")
                f.write("")
                f.close()

            count=0
            boo = True
            while boo and count<1000:
                #try:
                    f = open(filename,"r")
                    f.seek(0,0)
                    content = f.read()
                    f.close()

                    f = open(filename,"w")
                    f.write((s+content))
                    f.close()
                    boo = False
                #except:
                    #count +=1
                    sleep(1)

class sendpic():

    def __init__(self, filep):
        self.filep = filep
        self.filen = "/skole/tjener/home0/niko115/chat/data/picture/"
        #self.filen = "I:/002_Befehlslisten/chat/structur/chat/data/picture/"
        self.sendpict()

    def sendpict(self):

        count=0
        boo = True
        while boo and count<1000:
                try:
                    t = time()
                    s = str(t).replace(".","")
                    copy = "cp " + self.filep + " " + self.filen + s + (self.filep[len(self.filep)-4:len(self.filep)])
                    system(copy)
                    boo = False

                except:
                    count +=1



class ddd():
    def __init__(self):
        self.content = "aas"
        print (self.content)
