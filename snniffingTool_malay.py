
  
import tkinter
from tkinter import *
from scapy.all import *
import socket
from tkinter import messagebox
from time import sleep
from socket import gethostbyname

def sniff_packets(count = 1):
    packets = sniff(count = count )
    return str(packets.summary())

def dns_query(domain_name):
    try:
        return gethostbyname(domain_name)
    except Exception:
        messagebox.showerror('error' , "invaild domain name!")

    
def check_ipv4():
    ipv4_win = Tk()
    ipv4_win.title('ipv4')
    ipv4_win.overrideredirect(1)
    label_background = Label(ipv4_win , bg = 'black')
    label_background.place(x = 0 , y = 0 , width = ipv4_win.winfo_screenwidth() , height = ipv4_win.winfo_screenheight())
    ipv4_win.geometry('300x100+400+250')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80 ))
        IP = s.getsockname()[0]
    except:
        pass
    finally:
        s.close()
    label = Label(ipv4_win , text= IP , font = ('Arial Black', '18') , fg = '#13a10e' , bg = 'black')
    label.pack(side = 'top' , fill = 'x' , pady = 10 )
    close = Button(ipv4_win , text = "close" , command = ipv4_win.destroy , font = ('Arial Black', '14') ,bg = 'black' , fg ='#13a10e')
    close.config(width = 4 , height = 1)
    close.pack()
    ipv4_win.mainloop()

def sniffed_packed():
    packet_win = Tk()
    packet_win.title("packet details")
    packet_win.overrideredirect(1)
    packet_win.geometry("900x100+400+250")
    label_background = Label(packet_win , bg = 'black')
    label_background.place(x = 0 , y = 0 , width = packet_win.winfo_screenwidth() , height = packet_win.winfo_screenheight())
    packets = sniff(count = 1 )
    details = str(packets[0].summary())
    lab = Label(packet_win , text = details , fg = '#13a10e' , bg = 'black' , font = ('Arial Black', '15'))
    close = Button(packet_win , text ='close' , command = packet_win.destroy , font = ('Arial Black', '15') , bg = 'black' , fg = '#13a10e')
    close.place(x = 300 , y = 50)
    lab.place(x = 10 , y = 5)
    packet_win.mainloop()

def get_domain_name():
    
    global entry
    global dn_win
    response_win = Tk()
    response_win.overrideredirect(1)
    response_win.title('domain ipv4')
    response_win.geometry('350x100+400+250')
    label_background = Label(response_win , bg = 'black')
    label_background.place(x = 0 , y = 0 , width = response_win.winfo_screenwidth() , height = response_win.winfo_screenheight())
    info = entry.get()
    if len(info) > 1:
        msg = dns_query(info)
    lab = Label(response_win , text = msg , bg = 'black' , fg = '#13a10e' , font = ('Arial Black' , '15'))
    if len(str(msg)) > 5:
        lab.place(x = 10 , y = 5)  
    else:    
        messagebox.showerror("error" ,  'invaild domain!')
    close = Button(response_win , text ='close' , command = response_win.destroy , font = ('Arial Black', '15') , bg = 'black' , fg = '#13a10e')
    close.place(x = 150 , y = 50)
    entry.delete(0 , 'end')

def domain_enter():
    global entry
    global dn_win
    dn_win = Tk()
    label_background = Label(dn_win , bg = '#ccff99')
    label_background.place(x = 0 , y = 0 , width = dn_win.winfo_screenwidth() , height = (dn_win.winfo_screenheight() + 400))
    dn_win.geometry('350x350')
    dn_win.title('dns query')
    hint = Label(dn_win , text = 'enter the domain name in the box \n and than click submit' , font = ('Arial Black', '10') , bg ='#ccff99' , fg = 'black')
    hint.place(x = 60 , y = 70 )
    entry = Entry(dn_win)
    entry.place(x = 100 , y = 140)   
    button_submit = Button(dn_win , text = "submit" , command = get_domain_name  , font = ('Arial Black' , '12') , bg = '#ccff99' , fg = 'black')
    button_submit.config( width = 6 , height = 1 )
    button_submit.place(x = 130 , y = 200)

def main():
    
    global window
    window = Tk()
    label_background = Label(window , bg = '#009999')
    label_background.place(x = 0 , y = 0 , width = window.winfo_screenwidth() , height = (window.winfo_screenheight() + 400))    
    window.geometry("800x800")
    l = Label(window , text = "Welcome to network pannel!" , font = ('Arial Black', '24') , fg = 'black' , bg = '#009999')
    l.place(x = 200 , y = 50)
    button_ipv4 = Button(window, text = "ipv4" , command = check_ipv4 , bg  = 'black' , fg = '#009999' , font = ('Arial Black', '20'))
    button_ipv4.place(x = 100 , y = 130)
    button_ipv4.config( width = 7 , height = 2)
    button_sniff = Button(window , text = "sniffing" , command = sniffed_packed , bg  = 'black' , fg = '#009999' , font = ('Arial Black', '20') )
    button_sniff.config(width = 7 , height = 2)
    button_sniff.place(x = 100 , y = 270)
    button_dns = Button(window , text = " dns query ",command = domain_enter, font = ('Arial Black', '20') , bg ='black' , fg = '#009999')
    button_dns.config(width =8 , height =2)
    button_dns.place(x =100 , y= 400)
    window.title("network control panel")  
    window.mainloop()

def submit_login():
    
    username_entered = un_entry.get()
    password_entered = pass_entry.get()
    details = open('passwords.txt' , 'r')
    for d in details.readlines():
        username , password = d.split(':')
        if username_entered == username and password_entered == password.strip('\n'):
            login.destroy()
            main()
            details.close()
            break
def write_user_details():
    
    is_exist = False
    username_ent = entry_user.get()
    password_ent = entry_password.get()
    details = open('passwords.txt' , 'r+')
    for d in details.readlines():
        username , password = d.split(':')
        if username == username_ent:
            messagebox.showerror('error' , 'username is already exists')
            is_exist = True
            break
    if not is_exist:
        details.write(username_ent+':'+password_ent+'\n')
        details.close()
        signup_win.destroy()
        main()
            
    
def signup():
    global entry_user, entry_password ,signup_win
    
    login.destroy()
    signup_win = Tk()
    signup_win.geometry('500x500')
    signup_win.title('signup')
    background = Label(signup_win , bg = '#ff9900')
    background.place(x = 0, y= 0 ,width = signup_win.winfo_screenwidth() , height = signup_win.winfo_screenheight()) 
    label1 = Label(signup_win , text = "enter the username: " , bg = '#ff9900' , fg = 'black' , font =('Arial Black','17'))
    label1.place(x = 10 , y = 10) 
    entry_user = Entry(signup_win)
    entry_user.place(x = 30 , y = 60)
    label2 = Label(signup_win , text = "enter the password: " , bg = '#ff9900' , fg = 'black' , font =('Arial Black','17'))
    label2.place(x = 10 , y = 110) 
    entry_password = Entry(signup_win)
    entry_password.place(x = 30 , y = 160)
    submit = Button(signup_win , text ='submit' , command = write_user_details , font = ('Arial Black' , '15'))
    submit.place(x = 30 , y = 220)
    signup_win.mainloop()

def login():
    global  un_entry , pass_entry , login
    
    login = Tk()
    login.geometry("500x500")
    login.title("login")
    background = Label(login , bg = 'blue')
    background.place(x = 0, y= 0 ,width = login.winfo_screenwidth() , height = login.winfo_screenheight())
    un_label = Label(login , text = "enter the username: " , bg = 'blue' , fg = 'white' , font =('Arial Black','17'))
    un_label.place(x = 10 , y = 10) 
    un_entry = Entry(login)
    un_entry.place(x = 30 , y = 60)
    pass_label = Label(login , text = "enter the password: " , bg = 'blue' , fg = 'white' , font =('Arial Black','17'))
    pass_label.place(x = 10 , y = 110) 
    pass_entry = Entry(login)
    pass_entry.place(x = 30 , y = 160)
    submit = Button(login , text ='submit' , command = submit_login , font = ('Arial Black' , '15'))
    submit.place(x = 30 , y = 220)
    btn_signup = Button(login , text = 'signup' , command = signup , font = ('Arial Black' , '15'))
    btn_signup.place(x =30 , y = 280)
    login.mainloop()

login()    
f = open('passwords.txt' , 'r')
print (f.readlines())