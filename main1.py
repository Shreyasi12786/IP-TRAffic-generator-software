#Imported modules here
import re
import socket
from textwrap import fill
import threading
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor







# all global variables here

global tcpconn
global tcpaddress
global tcpmessage
global udpaddress
global udpmessage
all_conn = []
all_address =[]
all_msgs =[]
pack_size=[]
method =[]
crc_bits =[]
tcplist=[]
udplist=[]



tcpmainlist =[]
udpmainlist =[]





















# This is the function to start tcp server
def tcpserverstart():
    #creating tcp socket
    HOST = "localhost"
    PORT =9090
    try:
        tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
    #binding the socket and listening for connections
    try:


        tcpserver.bind((HOST, PORT))
        tcpserver.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" )
       
    #accepting connections
    for c in all_conn:
        c.close()

    del all_conn[:]
    del all_address[:]

    while True:
        for items in tcplist:
            table.insert('','end',values=items)
            tcplist.clear()
        try:
            
            tcpconn, tcpaddress = tcpserver.accept()
            tcpmessage =tcpconn.recv(1224)
            tcpserver.setblocking(1)  # prevents timeout
            # recvcount +=1
            # all_msgs.append(tcpmessage)
            # all_conn.append(tcpconn)
            # all_address.append(tcpaddress)
            tcpmainlist.append(tcpaddress[0])
            tcpmainlist.append("TCP")
            tcpmainlist.append("crc_bits")
            tcpmainlist.append(tcpmessage.decode('utf-8'))
            tcpmainlist.append(len(tcpmessage))
            tcpmainlist.append(tcpaddress[1])
            
    
            print("Connection has been established :" + tcpaddress[0])
            # list.append(all_address)
            # list.append(all_conn)
            # list.append(all_msgs)
            # list.append(method)
            tcplist.append(tcpmainlist)
            
            

            

        except:
             
             print("Error accepting connections")
    


    # table.append(parent='',index='end',iid=i,values=(address[0],'TCP','',message,'',address[1]))
    

tcpthread = threading.Thread(target=tcpserverstart)
tcpthread.start()





def udpserverstart():
    HOST = "localhost"
    PORT =5005
    try:
        udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


    try:


        udpserver.bind((HOST, PORT))
        # udpserver.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" )
    
   
    for c in all_conn:
        c.close()

    del all_conn[:]
    del all_address[:]

    while True:
        for items in udplist:
            table.insert('','end',values=items)
            udplist.clear()
        try:
            

            udpmessage, udpaddress = udpserver.recvfrom(1224)
            
            udpserver.setblocking(1)  # prevents timeout
            # recvcount = recvcount + 1
            # all_msgs.append(udpmessage)
            # all_address.append(udpaddress)
            # method.append("UDP")
            udpmainlist.append(udpaddress[0])
            udpmainlist.append("UDP")
            udpmainlist.append("crc")
            udpmainlist.append(udpmessage.decode('utf-8'))
            udpmainlist.append(len(udpmessage))
            udpmainlist.append(udpaddress[1])

            print("Connection has been established :" + udpaddress[0])
            # list.append(all_address)
            # list.append(all_conn)
            # list.append(all_msgs)
            # list.append(method)
            udplist.append(udpmainlist)
            

        except:
            print("Error accepting connections")

    
udpthread = threading.Thread(target=udpserverstart)
udpthread.start()






# # Function to add data in table
def adddata():
    for items in list:
        table.insert('','end',values=items)
    








#the gui for application starts here
root = Tk()
root.title("Packet Sender")


# GUI window 
# width= root.winfo_screenwidth()
# height= root.winfo_screenheight()


# root.geometry("%dx%d" % (width, height))
root.geometry('850x600')
root.maxsize(850,600)

mainIcon = PhotoImage(file="hotspot.png")
root.iconphoto(False, mainIcon)

# bg = PhotoImage(file="61769.png")
# my_label = Label(root,image=bg)
# my_label.pack()
root.config(bg="black")





# GUI MENUbar section
Filemenu = Menu(root)


# File

m1 = Menu(Filemenu, tearoff=0)
m1.add_command(label="Settings")
m1.add_separator()
root.config(menu=Filemenu)
Filemenu.add_cascade(label="File",menu=m1)

# TOOLS

m2 = Menu(Filemenu, tearoff=0)
m2.add_command(label="Intense Traffic Generator")
root.config(menu=Filemenu)
Filemenu.add_cascade(label="Tools",menu=m2)

#Help

m5 = Menu(Filemenu, tearoff=0)
m5.add_command(label="About Us")
root.config(menu=Filemenu)
Filemenu.add_cascade(label="Help",menu=m5)



# print(list)




# The sender frame
frame1=Frame(root,bg="#545454",highlightbackground="#545454", highlightthickness=1)
# frame1.place(x=45,y=40,width=1250,height=330)
frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=20,ipady=2)


#The data rate monitor frame
right = Frame(root,bg="#545454",relief=SUNKEN,highlightthickness=2,highlightbackground="#121850")
# right.place(x=1280,y=40,width=300,height=612)
right.grid(row=0,column=1)
data_rate=Label(right, text="Data Rate :",bg="#545454",fg="#d9d9d9").pack()


packet = StringVar()
# packetSize = StringVar()
# size= packetSize.get()
s= packet.get()

data_font = font.Font(family="comicsansms") 

# The sender gui 
data=Label(frame1, text="Data :",font=(data_font,12,"bold"),bg="#545454",fg="#d9d9d9",justify=LEFT).grid(row=0,column=0,padx=5,pady=3,columnspan=1)
# .place(x=30,y=45)

txt_data = Entry(frame1,font=(data_font,12),bg="#9a9a9a",borderwidth=2, textvariable = packet)
# txt_data.place(x=155,y=45,width=800,height=70)
txt_data.grid(row=1,column=0,columnspan=2,padx=5,pady=5)
txt_data.config(width=44)


def utf8len(s):
    
    length =len(s.encode('utf-8'))
    # txt_size.config(state="normal")
    txt_size.delete(0,END)
   
    txt_size.insert('end',str(length))
    # txt_size.config(state="disable")

data_size=Label(frame1, text="Packet Size :",font=(data_font,12,"bold"),bg="#545454",fg="#d9d9d9").grid(row=2,column=0,padx=5,pady=2)
# .place(x=30,y=130)

txt_size = Entry(frame1,font= (data_font,12) ,bg="#9a9a9a",borderwidth=2)
# txt_size.place(x=155,y=130,width=800)
txt_size.grid(row=3,column=0,padx=5,pady=2)

destip=Label(frame1, text="Address :",font=(data_font,12,"bold"),bg="#545454",fg="#d9d9d9").grid(row=2,column=1,padx=5,pady=2)
# .place(x=30,y=170)
txt_destip = Entry(frame1,font=(data_font,12),bg="#9a9a9a",borderwidth=2)
# txt_destip.place(x=155,y=170,width=800)
txt_destip.grid(row=3,column=1,padx=5,pady=2)


port=Label(frame1, text="Port :",font=(data_font,12,"bold"),bg="#545454",fg="#d9d9d9").grid(row=4,column=0,padx=5,pady=2)
# .place(x=30,y=220)
txt_port = Entry(frame1,font=(data_font,12),bg="#9a9a9a",borderwidth=2)
# txt_port.place(x=155,y=220,width=800)
txt_port.grid(row=5,column=0,padx=15,pady=2)


question=Label(frame1, text="Method :",font=(data_font,12,"bold"),bg="#545454",fg="#d9d9d9").grid(row=4,column=1,padx=5,pady=2)
# .place(x=30,y=270)
cmb_quest = ttk.Combobox(frame1,font=(data_font,12),state="readonly",justify="center")
cmb_quest['values']= ( "Select Protocol","TCP","UDP")

# cmb_quest.place(x=155,y=270,width=800,height=30)
cmb_quest.grid(row=5,column=1,padx=5,pady=2)
cmb_quest.current(0)

# calc = Button(frame1,text="CALC",borderwidth=2,bg="#545454",fg="#d9d9d9",highlightbackground="#121850",highlightthickness=2,command=lambda: utf8len(txt_data.get()))
# calc.config(font=("commicsansms","bold""bold"))
# calc.place(x=963,y=128,height=30,width=60)

# Function to clear the sender form
def clear():
    txt_data.delete(0,END)
    txt_data.delete(0,END)
    txt_destip.delete(0,END)
    txt_port.delete(0,END)
    cmb_quest.current(0)
    txt_size.config(state="normal")
    txt_size.delete(0,END)
    txt_size.config(state="disable")

# clear = Button(frame1,text="CLear",borderwidth=2,bg="#545454",fg="#d9d9d9",highlightbackground="#121850",highlightthickness=2,command=clear)
# clear.config(font=("commicsansms","bold""bold"))
# clear.place(x=963,y=168,height=30,width=60)

txt_size.bind('<tab>',utf8len(txt_size.get()))



# function for sending data
def write():
    input_data = txt_data.get()
    input_ip = txt_destip.get()
    input_port = txt_port.get()
    method = cmb_quest.get()
    #crc
    if method =="TCP":
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((input_ip,int(input_port)))
        sock.send(input_data.encode('utf-8'))
        
    else:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        msg = str.encode(input_data)
        sock.sendto(msg,(input_ip,int(input_port)))


#function to calculate packet length

    
    





mybtn = Button(frame1,text="Send",borderwidth=2,bg="#ff691f",fg="black",highlightbackground="#121850",highlightthickness=2,command=write,)
mybtn.config(font=(data_font,11,"bold"))
# mybtn.place(x=963,y=270,height=30,width=60)
mybtn.grid(row=6,column=1,padx=1,pady=14)
mybtn.config(width=5)






#reciever frame
frame2=Frame(root,bg="#545454",highlightbackground="#121850",highlightthickness=2)
# frame2.place(x=48,y=430,width=1250,height=220)
frame2.grid(row=1,column=0,columnspan=2)


#footer region
bottom=Frame(root,bg="#121850",relief=SUNKEN)
bottom.place(y=752,width = 2000,height=20)


# start = Button(bottom,text="START",bg="#121850",fg="#545454", )
# start.config(font=("commicsansms","bold""bold"))
# start.place(x=12)

# stop = Button(bottom,text="STOP",bg="#121850",fg="#545454",)
# stop.config(font=("commicsansms","bold""bold"))
# stop.place(x=1280)

# tcpport=Label(bottom, text="TCP PORT:",font=("Monoton","bold""bold"),bg="#121850",fg="#545454").place(x=1200)
# tcpbtn = Button(bottom,text="9090",bg="#121850",fg="#545454", )
# tcpbtn.config(font=("commicsansms","bold""bold"))
# tcpbtn.place(x=1280)

# udpport=Label(bottom, text="UDP PORT:",font=("Monoton","bold""bold"),bg="#121850",fg="#545454").place(x=1260)
# udpbtn = Button(bottom,text="5005",bg="#121850",fg="#545454",)
# udpbtn.config(font=("commicsansms","bold""bold"))
# udpbtn.place(x=1350)




    
table = ttk.Treeview(frame2)
# table.pack(side=TOP,fill=X)
table.grid(row=0,column=0)
table["columns"] = ("Col2","Col3","Col4","Col5","Col6","Col7")



table.column("#0",width=5,minwidth=12)
table.column("Col2",width=5,minwidth=20)
table.column("Col3",width=5,minwidth=20)
table.column("Col4",width=5,minwidth=12)
table.column("Col5",width=5,minwidth=30)
table.column("Col6",width=5,minwidth=12)
table.column("Col7",width=5,minwidth=12)

table.heading("#0",text="",anchor=W)
table.heading("Col2",text="Source IP",anchor=W)
table.heading("Col3",text="Method",anchor=W)
table.heading("Col4",text="Error",anchor=W)
table.heading("Col5",text="Data",anchor=W)
table.heading("Col6",text="Packet Size",anchor=W)
table.heading("Col7",text="Port no.",anchor=W)



# i=1
# table.append("",'end',iid=i,
# 		values=(i,'Alex','Four',78,'Male'))


root.mainloop()



if __name__ == "__main__":

   
    root()