#_________________________________________________________________________________________________________________
#-------------------------------------------Importing Required Package(API)---------------------------------------
#-----------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import pymysql
class Register:
# _________________________________________________________________________________________________________________
# -----------------------------------------------------FRONT END CODE----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

    def __init__(self,root):
        self.root=root
        self.root.title("ConsoleLancer")
        self.root.geometry("1600x750+0+0")
        # ________________________________________________________________
        # -------------------------Frame And Background-------------------
        # ----------------------------------------------------------------

        #main-Background
        self.bg=ImageTk.PhotoImage(file="bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Sub-Background
        self.left=ImageTk.PhotoImage(file="Sub_bg.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #===Register freame=====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=800,height=500)

        #=====Form Area =====
        title=Label(frame1,text="ADMIN REGISTRATION", font=("time new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # ________________________________________________________________
        # ---------------Entry feilds and Headings -----------------------
        # ----------------------------------------------------------------

        # =======First Name Text And Field===========
        f_name = Label(frame1, text="First Name", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.fname.place(x=50, y=130, width=250)

        # ==========Last Name Text And Field=========
        l_name = Label(frame1, text="Last Name", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=100)
        self.lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.lname.place(x=370, y=130, width=250)

        # =======Contact No.===========
        contact = Label(frame1, text="Contact No", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=170)
        self.contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.contact.place(x=50, y=200, width=250)

        # ==========E-Mail Id=========
        E_mail = Label(frame1, text="E-Mail ID", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=170)
        self.e_mail = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.e_mail.place(x=370, y=200, width=250)

        # =======Security Quistion.===========
        ques = Label(frame1, text="Security Question", font=("time new roman", 15, "bold"), bg="white",
                     fg="gray").place(x=50, y=240)
        # ======Combo Box===============
        self.select = ttk.Combobox(frame1, font=("times new roman", 15), state='readonly', justify=CENTER)
        self.select['values'] = ("select", "Your first place ", "Your Best friend Name ",)
        self.select.place(x=50, y=270, width=250)
        self.select.current(0)

        # ==========Asnwer =========
        ans = Label(frame1, text="Answer", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=240)
        self.ans = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.ans.place(x=370, y=270, width=250)

        # =====Password=====
        psw = Label(frame1, text="Password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.psw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.psw.place(x=370, y=340, width=250)

        # =======Confirm Password===========
        ques = Label(frame1, text="Comfirm Password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.cpsw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.cpsw.place(x=50, y=340, width=250)

        # =====Check Box===========
        self.check=IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Condition", variable=self.check, onvalue=1, offvalue=0, bg="white",font=("time new roman", 12)).place(x=50, y=380)

        # _________________________________________________________________
        # -----------------------Buttons-----------------------------------
        # -----------------------------------------------------------------

        # =====Regester button======
        #=======Singin Button======
        self.signin_btn = ImageTk.PhotoImage(file="signin.png")
        sigin = Button(self.root,image=self.signin_btn,command=self.sign_in,bd=0,bg="#013c74",cursor="hand2").place(x=120,y=500)

        #=======Singup Button======
        self.signup_btn = ImageTk.PhotoImage(file="singup.jpg")
        sigup = Button(frame1, image=self.signup_btn,cursor="hand2",bd=0, command=self.register_data).place(x=180, y=410)

        # =======Read More Button======
        self.read_more = ImageTk.PhotoImage(file="Read_More.png")
        read_more = Button(self.root, image=self.read_more, command=self.read_More_page,bg="#013c74", bd=0, cursor="hand2").place(x=220, y=455)

# ___________________________________________________________________________________________________________________
# -----------------------------------------------BACK END CODE-------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

    #==========Function for regestration form data insertion and fetch=========
    def register_data(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.contact.get()==""or self.e_mail.get()==""or self.select.get()==""or self.ans.get()==""or self.psw.get()==""or self.cpsw.get()=="":
            messagebox.showerror("Error","All fields are required ",parent=self.root)
        elif self.psw.get()!=self.cpsw.get():
            messagebox.showerror("Error", "Password must be same ", parent=self.root)
        elif self.check.get()==0:
            messagebox.showerror("Error", "agree check our tems and condition ", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="aug")
                cur=con.cursor()
                cur.execute("select * from user where phone_no=%s", self.contact.get())
                prow = cur.fetchone()
                cur.execute("select * from user where mail=%s", self.e_mail.get())
                row=cur.fetchone()
                if row!=None or prow!=None:
                    messagebox.showerror("Error", "Email or phone no already registered try with another one ", parent=self.root)
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
                    messagebox.showinfo("success", "Register Success",parent=self.root)
                    self.clear()
                    self.root.destroy()
                    from Data_Augmentation import User_DashBoard
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to {str(es)}", parent=self.root)

    # =======Function for going to sign in page======
    def sign_in(self):
        self.root.destroy()

# ==========function to clear the fields after success===============
    def clear(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.contact.delete(0, END)
        self.e_mail.delete(0, END)
        self.ans.delete(0, END)
        self.cpsw.delete(0, END)
        self.select.current(0)
        self.psw.delete(0, END)

    # ====Function to delete current page and jump on Read More Page========
    def read_More_page(self):
        self.root.destroy()


root=Tk()
obj=Register(root)
root.mainloop()

