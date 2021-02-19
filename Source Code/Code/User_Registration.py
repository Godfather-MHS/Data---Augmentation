#_________________________________________________________________________________________________________________
#-------------------------------------------Importing Required Package(API)---------------------------------------
#-----------------------------------------------------------------------------------------------------------------
from tkinter import Label

from PIL import ImageTk
from tkinter import ttk, messagebox, Frame, Entry, CENTER, IntVar, Checkbutton, Button, END, Tk
import pymysql

# _________________________________________________________________________________________________________________
# -----------------------------------------------------FRONT END CODE----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

class User_registration_Class:

    def __init__(self,User_registration_Window):
        self.User_registration_Window=User_registration_Window
        self.User_registration_Window.title("ConsoleLancer")
        self.User_registration_Window.geometry("1350x740")
        # ________________________________________________________________
        # -------------------------Frame And Background-------------------
        # ----------------------------------------------------------------

        #main-Background
        self.bg=ImageTk.PhotoImage(file="bg.png")
        bg=Label(self.User_registration_Window,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Sub-Background
        self.left=ImageTk.PhotoImage(file="Sub_bg.png")
        left=Label(self.User_registration_Window,image=self.left).place(x=80,y=100,width=400,height=500)

        #===Register freame===
        frame1=Frame(self.User_registration_Window,bg="white")
        frame1.place(x=480,y=100,width=800,height=500)

        #=====Form Area =====
        title=Label(frame1,text="USER SIGN UP", font=("time new roman",20,"bold") ,bg="white" ,fg="#838786")
        title.place(x=300,y=50)

        # ________________________________________________________________
        # ---------------Entry feilds and Headings -----------------------
        # ----------------------------------------------------------------

        # =======First Name Text And Field===========
        f_name = Label(frame1, text="First Name", font=("time new roman", 15, "bold"), bg="white", fg="gray")
        f_name.place(x=120, y=100)
        self.fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.fname.place(x=120, y=130, width=250)

        # ==========Last Name Text And Field=========
        l_name = Label(frame1, text="Last Name", font=("time new roman", 15, "bold"), bg="white", fg="gray")
        l_name.place(x=440, y=100)
        self.lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.lname.place(x=440, y=130, width=250)

        # =======Contact No.===========
        contact = Label(frame1, text="Contact No", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=120, y=170)
        self.contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.contact.place(x=120, y=200, width=250)

        # ==========E-Mail Id=========
        E_mail = Label(frame1, text="E-Mail ID", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=440, y=170)
        self.e_mail = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.e_mail.place(x=440, y=200, width=250)

        # =======Security Quistion.===========
        ques = Label(frame1, text="Security Question", font=("time new roman", 15, "bold"), bg="white",
                     fg="gray").place(x=120, y=240)
        # ======Combo Box===============
        self.select = ttk.Combobox(frame1, font=("times new roman", 15), state='readonly', justify=CENTER)
        self.select['values'] = ("select", "Your first place ", "Your Best friend Name ",)
        self.select.place(x=120, y=270, width=250)
        self.select.current(0)

        # ==========Asnwer =========
        ans = Label(frame1, text="Answer", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=440, y=240)
        self.ans = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.ans.place(x=440, y=270, width=250)

        # =====Password=====
        psw = Label(frame1, text="Password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=440, y=310)
        self.psw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.psw.place(x=120, y=340, width=250)

        # =======Confirm Password===========
        cpsw = Label(frame1, text="Comfirm Password", font=("time new roman", 15, "bold"), bg="white", fg="gray")
        cpsw.place(x=120, y=310)
        self.cpsw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.cpsw.place(x=440, y=340, width=250)

        # =====Check Box===========
        self.check=IntVar()
        chk = Checkbutton(frame1, text="I Agree with details", variable=self.check, onvalue=1, offvalue=0, bg="white",font=("time new roman", 12))
        chk.place(x=120, y=380)

        # _________________________________________________________________
        # -----------------------Buttons-----------------------------------
        # -----------------------------------------------------------------

        # =====Regester button======

        #=======Singin Button======
        self.signin_btn = ImageTk.PhotoImage(file="Sign_In.png")
        sigin = Button(self.User_registration_Window,image=self.signin_btn,activebackground="#013a71",command=self.sign_in,bg="#013a71",bd=0,cursor="hand2").place(x=160,y=500)

        #=======Singup Button======
        self.signup_btn = ImageTk.PhotoImage(file="Sign_Up.png")
        sigup = Button(frame1, image=self.signup_btn,cursor="hand2",activebackground="#ffffff",bd=0,bg="#ffffff",command=self.register_data)
        sigup.place(x=280, y=420)

        # =======Read More Button======
        self.read_more = ImageTk.PhotoImage(file="Read_More.png")
        read_more = Button(self.User_registration_Window, text="Read More",activebackground="#013c74",image=self.read_more, command=self.read_More_page,bg="#013c74", bd=0, cursor="hand2").place(x=220, y=455)

# ___________________________________________________________________________________________________________________
# -----------------------------------------------BACK END CODE-------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

    #==========Function for regestration form data insertion and fetch=========
    def register_data(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.contact.get()==""or self.e_mail.get()==""or self.select.get()==""or self.ans.get()==""or self.psw.get()==""or self.cpsw.get()=="":
            messagebox.showerror("Error","All fields are required ",parent=self.User_registration_Window)
        elif self.psw.get()!=self.cpsw.get():
            messagebox.showerror("Error", "Password must be same ", parent=self.User_registration_Window)
        elif self.check.get()==0:
            messagebox.showerror("Error", "agree check our tems and condition ", parent=self.User_registration_Window)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="aug")
                cur=con.cursor()
                cur.execute("select * from user where phone_no=%s", self.contact.get())
                prow = cur.fetchone()
                cur.execute("select * from user where mail=%s", self.e_mail.get())
                row=cur.fetchone()
                if row!=None or prow!=None:
                    messagebox.showerror("Error", "Email or phone no already registered try with another one ", parent=self.User_registration_Window)
                else:
                    cur.execute("insert into user(first_name,last_name,phone_no,mail,Ques,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.fname.get(),
                                self.lname.get(),
                                self.contact.get(),
                                self.e_mail.get(),
                                self.select.get(),
                                self.ans.get(),
                                self.psw.get(),
                            ))
                    con.commit() #Data Inserted
                    con.close() #connection closed
                    messagebox.showinfo("success", "Register Success",parent=self.User_registration_Window)
                    self.clear()
                    self.User_registration_Window.destroy()
                    import User_DashBoard
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to {str(es)}", parent=self.User_registration_Window)

        # =======Function for going to sign in page======

    # =======Function for going to sign in page======
    def sign_in(self):
        self.User_registration_Window.destroy()

    # ==========function to clear the fields after success===============
    def clear(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.contact.delete(0, END)
        self.e_mail.delete(0, END)
        self.ans.delete(0,END)
        self.cpsw.delete(0,END)
        self.select.current(0)
        self.psw.delete(0, END)

    # ====Function to delete current page and jump on Read More Page========
    def read_More_page(self):
        self.User_registration_Window.destroy()


User_registration_Window=Tk()
User_registration_Object=User_registration_Class(User_registration_Window)
User_registration_Window.resizable(False, False)
User_registration_Window.mainloop()

