#----------------------------------------MODULES IMPORT---------------------------------------------------------------------------#
import socket
import sys
import threading
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import time
from threading import Event
#----------------------------------------------------------------------------------------------------------------------------------#




#----------------------------------Global Variables----------------------------#
BUFFER_SIZE = 65535
tcplist=[]
udplist=[]
tcpmainlist =[]
udpmainlist =[]
hostname = socket.gethostname()
server_ip =socket.gethostbyname(hostname)
#-------------------------------------------------------------------------------------------------------------------------------------#



#--------------------------------------------------------------SERVER FUNCTIONS--------------------------------------------------------#
def tcpserverstart():
    
    
    HOST = server_ip
    PORT =9090
    try:
        global tcpserver
        tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
    
    try:


        tcpserver.bind((HOST, PORT))
        tcpserver.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" )
       
    
   

    while TRUE:
        for items in tcplist:
            table.insert('','end',values=items)
            tcplist.clear()
        try:
            
            tcpconn, tcpaddress = tcpserver.accept()
            tcpmessinput_port =tcpconn.recv(BUFFER_SIZE)
            tcpserver.setblocking(1)  # prevents timeout
            
            tcpmainlist.append(tcpaddress[0])
            tcpmainlist.append("TCP")
            tcpmainlist.append("")
            tcpmainlist.append(tcpmessinput_port.decode('utf-8'))
            tcpmainlist.append(len(tcpmessinput_port))
            tcpmainlist.append(tcpaddress[1])
            
    
            print("Connection has been established :" + tcpaddress[0])

            tcplist.append(tcpmainlist)
            
            

            

        except:
             
             print("Error accepting connections")
    
        

    
    

tcpthread = threading.Thread(target=tcpserverstart)
tcpthread.daemon = True
tcpthread.start()





def udpserverstart():
    HOST = server_ip
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
    
   


    while TRUE:
        
        for items in udplist:
            table.insert('','end',values=items)
            udplist.clear()
        try:
            

            udpmessinput_port, udpaddress = udpserver.recvfrom(BUFFER_SIZE)
            
            udpserver.setblocking(1)  # prevents timeout
            
            udpmainlist.append(udpaddress[0])
            udpmainlist.append("UDP")
            udpmainlist.append("")
            udpmainlist.append(udpmessinput_port.decode('utf-8'))
            udpmainlist.append(len(udpmessinput_port))
            udpmainlist.append(udpaddress[1])

            print("Connection has been established :" + udpaddress[0])
       
            udplist.append(udpmainlist)
            

        except:
            print("Error accepting connections")

    
udpthread = threading.Thread(target=udpserverstart)
udpthread.daemon=True
udpthread.start()

#-------------------------------------------------------------------------------------------------------------------------------#



#----------------------------------------GUI LOOP STARTS HERE--------------------------------------------------------------------#
root = Tk()
root.title("Packet Sender")

root.geometry('650x200')
root.maxsize(950,700)
root.minsize(950,700)

mainIcon = PhotoImage(file="hotspot.png")
root.iconphoto(False, mainIcon)

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



#-----------------------------------------------CLIENT SIDE GUI + FUNCTIONS-------------------------------------------------------------#
frame1=Frame(root,bg="#545454",highlightbackground="#545454", highlightthickness=1)
frame1.grid(row=0,column=1,padx=10,pady=13,ipady=5)

data_font = font.Font(family="Times") 


def utf8len():
    
    length =len(txt_data.get().encode('utf-8'))
    
    txt_size.config(state="normal")
    txt_size.delete(0,END)
    txt_size.insert('end',str(length))
    txt_size.config(state="disable")

def validate():
    validation()
    write()
    

    
def validation():
    input_data = txt_data.get()
    input_ip = txt_destip.get()
    input_port = txt_port.get()
    
    msg = ''
    
    

    if len(input_data) == 0:
        
        msg = "field cannot not be empty)"
    
    
    if len(input_port)==0:
        
        msg='Field can\'t be empty'
    else:
        try:
            if int(input_port) < 0 and int(input_port) > 65535:
                
                msg='Port Number Value out of range'
        except:
            
            msg='Port number must be integer value only'
    def in_range(n):   #check if every split is in range 0-255
        if n >= 0 and n<=255:
            return True
        return False
        
    def has_leading_zero(n): # check if eery split has leading zero or not.
        if len(n)>1:
            if n[0] == "0":
                return True
        return False
    def isValid(s):
            
        s = s.split(".")
        if len(s) != 4:  #if number of splitting element is not 4 it is not a valid ip address
            return 0
        for n in s:
                
            if has_leading_zero(n):
                return 0
            if len(n) == 0:
                return 0
            try:  #if int(n) is not an integer it raises an error
                n = int(n)
        
                if not in_range(n):
                    return 0
            except:
                return 0
        return 1
    ip = isValid(input_ip)
    if ip == 0:
        
        
        msg='Destination IP Address is Invalid'



    if msg == "":
        return  
    else: 
        messagebox.showerror('Invalid Entry', msg)
    

data=Label(frame1, text="Data :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9",justify=LEFT,).grid(row=0,column=0,columnspan=2,padx=5,pady=3)
txt_data = Entry(frame1,font=(data_font,11),bg="#9a9a9a",borderwidth=2,validate="focusout",validatecommand=utf8len)
txt_data.grid(row=1,column=0,columnspan=2,padx=5,pady=3)
txt_data.config(width=44)



data_size=Label(frame1, text="Packet Size :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9").grid(row=2,column=0,padx=5,pady=3)
txt_size = Entry(frame1,font= (data_font,11) ,bg="#9a9a9a",borderwidth=2)
txt_size.grid(row=3,column=0,padx=5,pady=3)




destip=Label(frame1, text="Address :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9").grid(row=2,column=1,padx=5,pady=3)
txt_destip = Entry(frame1,font=(data_font,11),bg="#9a9a9a",borderwidth=2)
txt_destip.grid(row=3,column=1,padx=5,pady=3)


port=Label(frame1, text="Port :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9").grid(row=4,column=0,padx=5,pady=3)
txt_port = Entry(frame1,font=(data_font,11),bg="#9a9a9a",borderwidth=2)
txt_port.grid(row=5,column=0,padx=5,pady=3)


question=Label(frame1, text="Method :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9").grid(row=4,column=1,padx=5,pady=2)
cmb_quest = ttk.Combobox(frame1,font=(data_font,11),state="readonly",justify="center")
cmb_quest['values']= ( "Select Method","TCP","UDP")
cmb_quest.grid(row=5,column=1,padx=5,pady=2)
cmb_quest.current(0)

delay=Label(frame1, text="Periodicity :",font=(data_font,11,"bold"),bg="#545454",fg="#d9d9d9").grid(row=6,column=0,padx=5)
txt_delay = Entry(frame1,font=(data_font,11),bg="#9a9a9a",borderwidth=2)
txt_delay.grid(row=7,column=0,padx=5)



def write():
    
        
        input_data = txt_data.get()
        input_ip = txt_destip.get()
        input_port = txt_port.get()
        method = cmb_quest.get()
        
        
            
        if input_data == "":
            pass

        else:
            if method =="TCP":
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect((input_ip,int(input_port)))
                sock.send(input_data.encode('utf-8'))
                            
                            
            else:
                sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
                msg = str.encode(input_data)
                sock.sendto(msg,(input_ip,int(input_port)))
    
    


def periodicity(start):
        
        input_data = txt_data.get()
        input_ip = txt_destip.get()
        input_port = txt_port.get()
        method = cmb_quest.get()
        resend = txt_delay.get()
        count = int(resend)
        
        
        while start:
            if method =="TCP":
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect((input_ip,int(input_port)))
                sock.send(input_data.encode('utf-8'))
                                
                                
            else:
                sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
                msg = str.encode(input_data)
                sock.sendto(msg,(input_ip,int(input_port)))
            time.sleep(count)
            global exit_flag
            if not exit_flag:
                break

def start_func():
    global t1
    global exit_flag
    exit_flag = TRUE
    t1 = threading.Thread(target=periodicity, args=(exit_flag,))
    t1.daemon = True
    t1.start()

def stop():
    global exit_flag
    exit_flag = False
    t1.join()






mybtn = Button(frame1,text="Send",borderwidth=2,bg="#ff691f",fg="black",highlightbackground="#121850",highlightthickness=2,command=validate,)
mybtn.config(font=(data_font,10,"bold"))
# mybtn.place(x=963,y=270,height=30,width=60)
mybtn.grid(row=6,column=1,padx=1,pady=4)
mybtn.config(width=5)

start = Button(frame1,text="Start",borderwidth=2,bg="#ff691f",fg="black",highlightbackground="#121850",highlightthickness=2,command=start_func,)
start.config(font=(data_font,10,"bold"))
# mybtn.place(x=963,y=270,height=30,width=60)
start.grid(row=7,column=1,padx=1,pady=4)
start.config(width=5)

stop_btn = Button(frame1,text="Stop",borderwidth=2,bg="#ff691f",fg="black",highlightbackground="#121850",highlightthickness=2,command=stop,)
stop_btn.config(font=(data_font,10,"bold"))
# mybtn.place(x=963,y=270,height=30,width=60)
stop_btn.grid(row=8,column=1,padx=1,pady=4)
stop_btn.config(width=5)

#-----------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------Footer----------------------------------------------------------------------------#
bottom=Frame(root,bg="black",relief=SUNKEN)
bottom.grid(row=2,column=1)

tcpport=Label(bottom, text="TCP PORT:",font=("Monoton",10),bg="#696969",fg="#c0c0c0").grid(row=0,column=0)
tcpbtn = Button(bottom,text="9090",bg="#ff691f",fg="black", )
tcpbtn.config(font=("commicsansms",10))
tcpbtn.grid(row=0,column=1)

udpport=Label(bottom, text="UDP PORT:",font=("Monoton",10),bg="#696969",fg="#c0c0c0").grid(row=0,column=2)
udpbtn = Button(bottom,text="5005",bg="#ff691f",fg="black",)
udpbtn.config(font=("commicsansms",10))
udpbtn.grid(row=0,column=3)

udpport=Label(bottom, text="SERVER_IP:",font=("Monoton",10),bg="#696969",fg="#c0c0c0").grid(row=0,column=4)
udpbtn = Button(bottom,text=server_ip,bg="#ff691f",fg="black",)
udpbtn.config(font=("commicsansms",10))
udpbtn.grid(row=0,column=5)


#-----------------------------------------RECIEVER END------------------------------------------------------------------------------#
table = ttk.Treeview(root)
table.grid(row=1,column=0,columnspan=4,padx=20,pady=20)
table["columns"] = ("Col2","Col3","Col4","Col5","Col6","Col7")



table.column("#0",width=50,minwidth=50)
table.column("Col2",width=140,minwidth=150)
table.column("Col3",width=140,minwidth=150)
table.column("Col4",width=140,minwidth=150)
table.column("Col5",width=140,minwidth=150)
table.column("Col6",width=140,minwidth=150)
table.column("Col7",width=140,minwidth=150)

table.heading("#0",text="",anchor=W)
table.heading("Col2",text="Source IP",anchor=W)
table.heading("Col3",text="Method",anchor=W)
table.heading("Col4",text="Error",anchor=W)
table.heading("Col5",text="Data",anchor=W)
table.heading("Col6",text="Packet Size",anchor=W)
table.heading("Col7",text="Port no.",anchor=W)

#-----------------------------------------------------------------------------------------------------------------------#

def on_closing():
    
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
exit(0)



    
    