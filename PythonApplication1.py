from tkinter import *
import os
from tkinter import messagebox
 
def qeydiyyat_pencere():
    global register_screen
    register_screen = Toplevel()
    register_screen.title("Qeydiyyat")
    register_screen.attributes("-fullscreen",True)

    qeydiyyat_f=Frame(register_screen,bg="black")
    qeydiyyat_f.place(x=610,y=170,width=340,height=450)    
 
    global username
    global password
    global username_entry
    global password_entry
    global txtpassword1
    username = StringVar()
    password = StringVar()

    qeydiyyat_l=Label(qeydiyyat_f,text="Qeydiyyat Ol",font=("times new roman",20,"bold"),fg="white",bg="black")
    qeydiyyat_l.place(x=80,y=15) 
                
    username_lbl=lbl=Label(qeydiyyat_f,text="İstifadəçi adı",font=("times new roman",20,"bold"),fg="white",bg="black")
    username_lbl.place(x=60,y=80)
                
    username_entry=Entry(qeydiyyat_f,font=("times new roman",15,"bold"),textvariable=username)
    username_entry.place(x=40,y=125,width=270) 
             
    password_L=lbl=Label(qeydiyyat_f,text="Parol",font=("times new roman",20,"bold"),fg="white",bg="black")
    password_L.place(x=60,y=175)

    password_entry=Entry(qeydiyyat_f,font=("times new roman",15,"bold"),textvariable=password,show="*")
    password_entry.place(x=40,y=220,width=270)

    password1=lbl=Label(qeydiyyat_f,text="Parol tekrarla",font=("times new roman",20,"bold"),fg="white",bg="black")
    password1.place(x=60,y=260)
               
    txtpassword1=Entry(qeydiyyat_f,font=("times new roman",15,"bold"),show="*",textvariable=password1)
    txtpassword1.place(x=40,y=310,width=270)


    qeydiyyat_b=Button(qeydiyyat_f,text="Qeydiyyat",font=("times new roman",15,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="black",activebackground="black",command=register_user)
    qeydiyyat_b.place(x=110,y=350,width=120,height=35)  

    login_b=Button(qeydiyyat_f,text="Login",font=("times new roman",15,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="black",activebackground="black",command=register_screen.destroy)
    login_b.place(x=110,y=400,width=120,height=35) 


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(register_screen)
    password_not_recog_screen.title("Eror")
    password_not_recog_screen.resizable(False,False)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x80+700+300")
    Label(password_not_recog_screen, text="Şifrənin təkrarı eyni deyil").pack()
    Button(password_not_recog_screen, text="OK",command=cixis).pack()

def eror():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(register_screen)
    password_not_recog_screen.title("Eror")
    password_not_recog_screen.resizable(False,False)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x80+700+300")
    Label(password_not_recog_screen, text="Tam Alan doldurlmayıb").pack()
    Button(password_not_recog_screen, text="OK",command=cixis).pack()

def ugurlu():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(register_screen)
    password_not_recog_screen.title("Uğurlu")
    password_not_recog_screen.resizable(False,False)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x80+700+300")
    Label(password_not_recog_screen, text="Qeydiyyat Uğurlu").pack()
    Button(password_not_recog_screen, text="OK",command=cixis).pack()   

def cixis():
    password_not_recog_screen.destroy()

def register_user():
 
    username_info = username.get()
    password_info = password.get()
    password_info1= txtpassword1.get()

    if username.get()=="" and password.get()=="" and txtpassword1.get()=="":
        eror() 
    elif password_info=="":
        eror()    
    elif password_info==password_info1:    
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()
            ugurlu()
    elif password_info!=password_info1:
            password_not_recognised()        
 
 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            messagebox.showinfo("Daxil","Daxil Olursuz")        
        else:
            messagebox.showerror("Eror","Yalnıs Parol")        
    elif username1=="" and password1=="":
        messagebox.showerror("Eror","Tam Alan doldurlmayıb")
    else:
        messagebox.showerror("Eror"," Yalnıs İstifadəçi Adı")

 
def login_pencere():
    global loginekran
    loginekran = Tk()
    loginekran.attributes("-fullscreen",True)
    loginekran.title("Login")

    login_f=Frame(loginekran,bg="black")
    login_f.place(x=610,y=170,width=340,height=450)


    global username_verify
    global password_verify
 
    username_verify = StringVar()           
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry

    daxil_ol_l=Label(login_f,text="Daxil Ol",font=("times new roman",20,"bold"),fg="white",bg="black")
    daxil_ol_l.place(x=120,y=15) 

    Label(login_f,text="istifadəçi adı",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=60,y=80)
    username_login_entry =Entry(login_f,font=("times new roman",15,"bold"),textvariable=username_verify)
    username_login_entry.place(x=40,y=125,width=270) 

    Label(login_f,text="Parol",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=60,y=175)
    password_login_entry = Entry(login_f,font=("times new roman",15,"bold"),show="*",textvariable=password_verify)
    password_login_entry.place(x=40,y=220,width=270) 

    Button(login_f,text="Login",command=login_verify,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red").place(x=110,y=270,width=120,height=35)
  
    qeydiyyat_b=Button(login_f,text="Qeydiyyat",command=qeydiyyat_pencere,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
    qeydiyyat_b.place(x=110,y=315,width=120,height=35)  

    cixis_b=Button(login_f,text="Çıxış",command=loginekran.destroy,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
    cixis_b.place(x=110,y=365,width=120,height=35)  


    loginekran.mainloop()


login_pencere()