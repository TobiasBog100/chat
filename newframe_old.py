
# only on schoolserver



import pickle

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from threading import *

from time import time
from time import sleep

from os.path import abspath
from os import system
from os import listdir

from const.connection import managment

a = managment.ddd()
#a = filedialog.askopenfile()
#print(a)

a =str(time()).replace(".","")

print (a)
print (int(a))
print(abspath("."))

"/skole/tjener/home0/niko115/chat/data/chats/main.txt"
"""
d = open("settings/settingssize.dmp", "wb")
p = pickle.Pickler(d)
p.dump([1000,10000,10])
d.close()

d = open("settings/settingsuser.dmp", "wb")
p = pickle.Pickler(d)
p.dump(["User","#000000"])
d.close()
"""


"""
root = Tk()
s = StringVar()
root.title("Counting Seconds")
label = Label(root, fg="green")
label.grid()
a = Entry(root)
a.grid()
label.config(background="#055")
root.mainloop()
print(s.get())
"""

d = open("settings/settingsuser.dmp", "rb")
p = pickle.Unpickler(d)
s = p.load()
print(s)
d.close()

d = open("settings/settingssize.dmp", "rb")
p = pickle.Unpickler(d)
s = p.load()
print(s)
d.close()







class image():

    def __init__(self,filenn):
        self.filen = filenn
        self.openpic = Tk(className=" Bild")

        if (len(self.filen)-5)<(self.filen.lower()).find(".gif"):
            canvasp = Canvas(master=self.openpic)
            canvasp.pack()

            pic = PhotoImage(master=self.openpic,file=self.filen)
            canvasp.create_image(30,30, anchor=NW, image=pic)


            self.openpic.mainloop()

        else:
            system(self.filen)





def func(filed):
    im = image(filed)
    return 0


# class

class frame():

    def __init__(self):
        self.mainframe = Tk(className=" Whatspy")

        try:
            self.mainframe.wm_iconbitmap("Icon.ico")
        except:
            pass

        self.color1 = ""
        self.name = ""

        self.size1 = 0
        self.size2 = 0
        self.size3 = 0

        self.time = ((listdir("settings/var"))[0]).replace(".txt","")

        self.owntime = str(self.time).replace(".","")


        self.inits()
        self.initt()


        self.integer1 = IntVar()
        self.boolean1 = True

        self.string1 = StringVar()
        self.string2 = StringVar()

        self.string3 = StringVar()
        self.string4 = ""

        self.string2.set("Courier")



        self.mainframe.M = Menu(self.mainframe)

        self.mainframe.M.m = Menu(self.mainframe.M, tearoff =0)

        self.mainframe.M.m.add_radiobutton(label = "rot", variable = self.string1, value = "800")
        self.mainframe.M.m.add_radiobutton(label = "gruen", variable = self.string1, value = "080")
        self.mainframe.M.m.add_radiobutton(label = "blau", variable = self.string1, value = "008")

        self.mainframe.M.m.m1 = Menu(self.mainframe.M.m,tearoff =0)

        self.mainframe.M.m.m1.add_radiobutton(label = "weiß", variable = self.integer1, value = 1)
        self.mainframe.M.m.m1.add_radiobutton(label = "schwarz", variable = self.integer1, value = 2)

        self.mainframe.M.m.add_cascade(menu = self.mainframe.M.m.m1, label = "Helligkeit")

        self.mainframe.M.add_cascade(menu = self.mainframe.M.m, label = "Farbe")


        self.mainframe.M.add_command(label= "Aendern", command = self.color)

        self.mainframe.M.add_separator()
        self.mainframe.M.add_command(label= "Hochladen", command = self.sendpic)
        self.mainframe.M.add_command(label= "Oeffnen", command = self.openpic)
        self.mainframe.M.add_separator()


        self.mainframe.M.add_command(label= "Einstellungen", command = self.settings)

        self.mainframe.M.add_command(label= "Hilfe/Readme", command = self.help)

        self.mainframe.config(menu = self.mainframe.M)





        self.mainframe.canvas1 = Canvas(master = self.mainframe ,width = "10c", height = "10c", background = "#080")
        self.mainframe.canvas1.pack(fill = BOTH, expand = 1)

        self.mainframe.canvas1.canvasinl = Label(master=self.mainframe.canvas1,background = "#080")
        self.mainframe.canvas1.canvasinl.grid(row=0 , column=0, padx="1m")

        self.mainframe.canvas1.canvasinu = Label(master=self.mainframe.canvas1,background = "#080")
        self.mainframe.canvas1.canvasinu.grid(row=0 , column=1, pady="1m")

        self.mainframe.canvas1.canvasinr = Label(master=self.mainframe.canvas1,background = "#080")
        self.mainframe.canvas1.canvasinr.grid(row=0 , column=3, padx="1m")

        self.mainframe.canvas1.canvasinc = Label(master=self.mainframe.canvas1,background = "#080")
        self.mainframe.canvas1.canvasinc.grid(row=3 , column=2, pady="1m")


        self.mainframe.canvas1.baryy = Scrollbar(master = self.mainframe.canvas1, orient=VERTICAL)
        self.mainframe.canvas1.baryy.grid(row=4 , column=2, sticky="NS")

        self.mainframe.canvas1.barxx = Scrollbar(master = self.mainframe.canvas1, orient=HORIZONTAL)
        self.mainframe.canvas1.barxx.grid(row=5 , column=1, sticky="EW")

        self.mainframe.canvas1.message = Text(master= self.mainframe.canvas1 ,yscrollcommand = self.mainframe.canvas1.baryy.set, xscrollcommand = self.mainframe.canvas1.barxx.set ,font="Courier",relief = SUNKEN, height=3 ,width=70, wrap=NONE)

        self.mainframe.canvas1.baryy.config(command = self.mainframe.canvas1.message.yview)
        self.mainframe.canvas1.barxx.config(command = self.mainframe.canvas1.message.xview)
        self.mainframe.canvas1.message.grid(row=4 , column=1, sticky="E")







        self.mainframe.canvas1.bary = Scrollbar(master = self.mainframe.canvas1, orient=VERTICAL)
        self.mainframe.canvas1.bary.grid(row=1 , column=2, sticky="NS")

        self.mainframe.canvas1.barx = Scrollbar(master = self.mainframe.canvas1, orient=HORIZONTAL)
        self.mainframe.canvas1.barx.grid(row=2 , column=1, sticky="EW")

        self.mainframe.canvas1.editor = Text(master= self.mainframe.canvas1 ,yscrollcommand = self.mainframe.canvas1.bary.set, xscrollcommand = self.mainframe.canvas1.barx.set ,font="Courier",relief = SUNKEN, height=20 ,width=70, wrap=NONE)
        self.mainframe.canvas1.editor.config(state=DISABLED)

        self.mainframe.canvas1.bary.config(command = self.mainframe.canvas1.editor.yview)
        self.mainframe.canvas1.barx.config(command = self.mainframe.canvas1.editor.xview)
        self.mainframe.canvas1.editor.grid(row=1 , column=1, sticky="E")



        self.mainframe.canvas1.Button1 = Button(master= self.mainframe.canvas1, text="Senden", command= self.send)
        self.mainframe.canvas1.Button1.grid(row=6, column=1, pady="5m")

        self.mainframe.canvas1.Checkbutton1 = Checkbutton(master= self.mainframe.canvas1, onvalue="Courier" , offvalue="Arial", command=self.stil ,indicatoron=False,variable=self.string2, textvariable=self.string2,width =6 )
        self.mainframe.canvas1.Checkbutton1.grid(row=6, column=1, pady="5m", padx="5m", sticky=W)



        self.askfile  = {}
        self.askfile["initialdir"] = abspath(".")+"/data/picture"
        self.askfile["title"] = " Bildwahl"


        self.mainframe.protocol("WM_DELETE_WINDOW", self.closewindow)

        self.mainframe.resizable(width=FALSE, height=FALSE)




        self.newthread = self.starttext(self.mainframe.canvas1.editor, self.size1)
        self.newthread.start()
        self.currentthread = self.currenttext(self.mainframe.canvas1.editor)
        self.currentthread.start()



    def closewindow(self):
        yesno = messagebox.askyesno(" Beenden","Wollen die den Chat wirklich beenden?\nSind alle anderen Bildschirme geschlossen.")
        if yesno:
            self.currentthread.setrun()
            self.currentthread = 0

            self.mainframe.destroy()
            #self.manager()
        return 0



    def inits(self):
        d = open("settings/settingssize.dmp", "rb")
        p = pickle.Unpickler(d)
        s = p.load()
        d.close()

        self.size1 = s[0]
        self.size2 = s[1]
        self.size3 = s[2]
        return 0

    def initt(self):
        d = open("settings/settingsuser.dmp", "rb")
        p = pickle.Unpickler(d)
        t = p.load()
        d.close()

        self.name = t[0]
        self.color1 = t[1]

        return 0

    def color(self):
        if self.string1.get() != "":
            self.s =  "#" + str(self.string1.get())
            if self.integer1.get()==1 :
                self.s =self.s.replace("8", "C")
            elif self.integer1.get()==2:
                self.s =self.s.replace("8", "4")

            self.mainframe.canvas1.config(background = self.s)

            self.mainframe.canvas1.canvasinl.config(background = self.s)

            self.mainframe.canvas1.canvasinu.config(background = self.s)

            self.mainframe.canvas1.canvasinr.config(background = self.s)

            self.mainframe.canvas1.canvasinc.config(background = self.s)

        if self.integer1.get() != 0 and self.boolean1:
            self.mainframe.M.m.m1.add_radiobutton(label = "neutral", variable = self.integer1, value = 0)
            self.boolean1 = False
        elif self.integer1.get() == 0:
            self.mainframe.M.m.m1.delete(2)
            self.boolean1 = True





    def send(self):
        self.string4=self.mainframe.canvas1.message.get(1.0,END)
        managment.send(self.name,self.color1,self.string4)
        sleep(0.1)
        self.mainframe.canvas1.message.delete(1.0,END)
        return 0



    def sendpic(self):
        managment.send(self.name,self.color1,"Sendet Bild")

        filed = str(filedialog.askopenfilename(**(self.askfile)))
        if filed=="":
            return 0

        managment.sendpic(filed)

        return 0

    def openpic(self):
        filed = str(filedialog.askopenfilename(**(self.askfile)))#.replace(abspath(".").replace("\\","/"),"")
        #filed= filed[1:]

        if filed=="":
            return 0

        func(filed)

        return 0


    def settings(self):
        self.sett = Tk()
        self.sett.title(" Einstellungen")

        button1 = Button(self.sett, text="Speicher", width=25, command=self.sizesettings)
        button1.pack()

        button2 = Button(self.sett, text="Benutzer", width=25, command=self.usersettings)
        button2.pack()

        self.sett.mainloop()
        return 0

    def usersettings(self):

        self.sett.destroy()

        self.ustring1 = ""

        self.ustring2 = self.color1


        def userendbutton():

            d = open("settings/settingsuser.dmp", "wb")
            p = pickle.Pickler(d)
            self.ustring1 = self.user.entry1.get()

            if self.ustring1 != self.name and self.ustring1 != "" and self.ustring1 != " ":
                self.name = self.ustring1
            if self.ustring2 != self.color1 :
                if self.ustring2.find("#")==-1:
                    self.ustring2 = "#000000"
                self.color1 = self.ustring2
            p.dump([self.name,self.color1])
            d.close()

            self.user.destroy()


        self.user = Tk()
        self.user.title(" Benutzereinstellungen")
        label1 = Label(self.user, text="Name", width=20)
        label2 = Label(self.user, text="Farbe", width=20)
        label1.grid(row=0,column=0, pady="1m")
        label2.grid(row=1,column=0, pady="1m")
        self.user.entry1 = Entry(master=self.user, width=30)
        self.user.entry1.grid(row=0,column=1, pady="1m")

        button1 = Button(self.user, text="Farbe erstellen", width=30, command=self.colorbutton)
        button1.grid(row=1,column=1, pady="1m")

        button1 = Button(self.user, text="Fertig", width=30, command=userendbutton)
        button1.grid(row=2,column=1, pady="2m")

        self.user.mainloop()
        return 0



    def sizesettings(self):

        self.sett.destroy()

        def sizeendbutton():
           try:
            d = open("settings/settingssize.dmp", "wb")
            p = pickle.Pickler(d)
            if int(self.size.entry1.get())>100 and int(self.size.entry1.get())<1001:
                self.size1 = int(self.size.entry1.get())
            if int(self.size.entry2.get())>1000 and int(self.size.entry1.get())<int(self.size.entry2.get()):
                self.size2 = int(self.size.entry2.get())
            if int(self.size.entry3.get())>1:
                self.size3 = int(self.size.entry3.get())

            p.dump([self.size1,self.size2,self.size3])
            d.close()

            self.size.destroy()
           except:
               pass


        self.size = Tk()
        self.size.title(" Speichereinstellungen")

        label1 = Label(self.size, text="Anzahl der angezeigten Nachrichten", width=40)
        label2 = Label(self.size, text="Anzahl der gespeicherten Nachrichten", width=40)
        label3 = Label(self.size, text="Anzahl der gespeicherten Bilder", width=40)
        label1.grid(row=0,column=0, pady="1m")
        label2.grid(row=1,column=0, pady="1m")
        label3.grid(row=2,column=0, pady="1m")

        self.size.entry1 = Entry(master=self.size, width=30)
        self.size.entry1.grid(row=0,column=1, pady="1m")
        self.size.entry2 = Entry(master=self.size, width=30)
        self.size.entry2.grid(row=1,column=1, pady="1m")
        self.size.entry3 = Entry(master=self.size, width=30)
        self.size.entry3.grid(row=2,column=1, pady="1m")

        self.size.entry1.insert(1,str(self.size1))
        self.size.entry2.insert(1,str(self.size2))
        self.size.entry3.insert(1,str(self.size3))

        button1 = Button(self.size, text="Fertig", width=30, command=sizeendbutton)
        button1.grid(row=3,column=1, pady="2m")

        self.size.mainloop()
        return 0





    def help(self):

        d = open("const/help.dmp", "rb")
        p = pickle.Unpickler(d)
        s = p.load()
        d.close()
        helpme = Tk()
        helpme.title("Hilfe")
        label1 = Label(master= helpme,text=s, font=("Arial",11))
        label1.pack()
        helpme.mainloop()

        return 0



    def stil(self):

        if self.string2.get()=="Courier":

            self.mainframe.canvas1.editor.config(font="Courier")
            self.mainframe.canvas1.message.config(font="Courier")
        else:

            self.mainframe.canvas1.editor.config(font="Arial")
            self.mainframe.canvas1.message.config(font="Arial")


    def colorbutton(self):

        def end():
            self.ustring2 = self.var
            self.color1.destroy()



        self.var="#000000"

        def change(event):
            try:
                show.config(background="#"+str(hex(scale1.get())).lstrip("0x").zfill(2)+str(hex(scale2.get())).lstrip("0x").zfill(2)+str(hex(scale3.get())).lstrip("0x").zfill(2))
                self.var="#"+str(hex(scale1.get())).lstrip("0x").zfill(2)+str(hex(scale2.get())).lstrip("0x").zfill(2)+str(hex(scale3.get())).lstrip("0x").zfill(2)
            except:
                pass

        self.color1 = Tk()
        self.color1.title(" Farbenmixer")
        scale1 = Scale(self.color1, orient=VERTICAL, label="rot",from_=255, to =0, command=change)
        scale1.grid(row=0,column=0)

        scale2 = Scale(self.color1, orient=VERTICAL, label="gruen",from_=255, to =0, command=change)
        scale2.grid(row=0,column=1)

        scale3 = Scale(self.color1, orient=VERTICAL, label="blau",from_=255, to =0, command=change)
        scale3.grid(row=0,column=2)

        self.color1.bind_all(sequence="<Any-ButtonRelease>", func=change)

        show = Canvas(self.color1, width=70,height=70, background="#000000")
        show.grid(row=0,column=3)

        button1 = Button(self.color1, text="Fertig", width=10, command=end)
        button1.grid(row=1, column=3)


        self.color1.mainloop()
        return 0

    class currenttext(Thread):

        def __init__(self, t):
            Thread.__init__(self)
            self.runvar = True
            self.configtext = t
            self.filenown = "settings/var"

        def run(self):

            owntime = str(time()).replace(".","")
            sleep(2.5)

            var=0
            while self.runvar:

                sleep(0.5)
                try:
                    othertime = ((listdir(self.filenown))[0]).replace(".txt","")
                except:
                    continue

                if len(othertime)<15:
                    othertime = othertime + "0"

                if len(owntime)<15:
                    owntime =  owntime + "0"



                #if not(int(owntime)<int(othertime)):
                    #continue

                list = []
                try:
                    self.configtext.config(state=NORMAL)
                    end = str(int(float(self.configtext.index("end")))-1) + "."

                    length1 = end + "0"
                    length2 = end + "1000"

                    line = self.configtext.get(length1,length2)
                    #print(line)

                    f = open("data/chats/main.txt","r")

                    vars = 0


                    while vars <1000:
                        rline = f.readline()

                        rline = rline.replace("\n","")
                        if rline == "":
                            break


                        evalline = eval((rline))
                        #print(evalline)
                        #print(line.find(evalline[0]), line.find(evalline[2]))
                        if line.find(evalline[0])!=-1 and line.find(evalline[2])!=-1:

                            break


                        list.append(evalline)
                        #del list[len(list)-1]

                        #print(list)
                        vars += 1

                    f.close()




                    for c in list:

                            argument1 = c[0]
                            argument2 = c[2]
                            color = c[1]


                            connection = "\n" + argument1 + ": " + argument2

                            self.configtext.insert(END,connection)

                            end = str(int(float(self.configtext.index("end")))-1) + "."


                            length1 = end + "0"
                            length2 = end + str(len(argument1))



                            #self.configtext.configure(font="Arial")
                            self.configtext.tag_add("currcolor" + str(var), length1,length2)
                            self.configtext.tag_configure("currcolor" + str(var), foreground=color)

                            var +=1

                            #self.configtext.delete(END)

                    self.configtext.config(state=DISABLED)

                except:
                    pass
            return 0


        def setrun(self):
            self.runvar = False
            return 0





    class starttext(Thread):

        def __init__(self,t,s):
            Thread.__init__(self)
            self.configtext = t
            self.size = s

        def run(self):
                sleep(1)
                f = open("data/chats/main.txt","r")
                list = f.readlines()
                f.close()

                a = len(list)
                if a>self.size:
                    del list[self.size::]

                var=0
                self.configtext.config(state=NORMAL)
                for c in list:
                    c.replace("\n","")
                    r = eval(c)
                    argument1 = r[0]
                    argument2 = r[2]
                    color = r[1]


                    connection = "\n" + argument1 + ": " + argument2

                    self.configtext.insert("1.0",connection)
                    #end = str(int(float(self.configtext.index("end")))-2) + "."

                    length1 = "2." + "0"
                    length2 = "2." + str(len(argument1))



                    #self.configtext.configure(font="Arial")
                    self.configtext.tag_add("usercolor" + str(var), length1,length2)
                    self.configtext.tag_configure("usercolor" + str(var), foreground=color)

                    var +=1

                #self.configtext.mark_set("insert", "16.0")

                self.configtext.config(state=DISABLED)


                return 0



    def gettime(self):
        return self.owntime

    def settime(self,timee):
        self.owntime = timee


    def mainlooop(self):

        self.mainframe.mainloop()

class background(Thread):

        def __init__(self):
            Thread.__init__(self)
            self.action = 1
            self.boo = True
            self.filen = "/skole/tjener/home0/niko115/chat/data/chats/data/var"
            #self.filen = "I:/002_Befehlslisten/chat/structur/chat/data/var"
            self.filenown = "settings/var/"


        def run(self):

            sleep(1.5)
            if self.action ==1:
                while self.boo:
                    #try:
                        owntime = window.gettime()
                        othertime = ((listdir(self.filen))[0]).replace(".txt","")



                        if len(othertime)<15:
                            othertime = othertime + "0"

                        if len(owntime)<15:
                            owntime =  owntime + "0"

                        if int(owntime)<int(othertime):
                            managment.get()
                            s1 = self.filenown + owntime + ".txt"
                            s2 = othertime + ".txt"
                            ren = "rename " + s1 + " " + s2
                            #ren = ren.replace("/","\\")
                            system(ren)
                            window.settime(othertime)


                    #except:
                        #pass

                        sleep(0.2)
            else:
                pass


            return 0

        def varset(self):

            self.boo = False

class manage(Thread):

        def __init__(self):
            Thread.__init__(self)


        def run(self):

            sleep(1.5)


# main

print(len("145001389577199"))


window = frame()

unthread = background()
unthread.start()
window.mainlooop()
print("aaa")
unthread.varset()

while unthread.is_alive():
    sleep(0.2)

print("end")

#s = "print(\"hi\")\n"
#code = compile(s, "<STRING>","exec")
#exec(code)


'''
if self.o in listdir():
            self.ask= messagebox.askyesno("Überschreibungswarnung","Datei existiert bereits!!!\nWollen sie sie überschreiben?")
            if not self.ask:
                return 0

'''
