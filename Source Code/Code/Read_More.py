#_________________________________________________________________________________________________________________
#-------------------------------------------Importing Required Package(API)---------------------------------------
#-----------------------------------------------------------------------------------------------------------------

from PIL import ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, END


# _________________________________________________________________________________________________________________
# -----------------------------------------------------FRONT END CODE----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

class ReadMe_Class:

    #=====ReadMe_Window Function===========
    def __init__(self,ReadMe_Window):
        self.ReadMe_Window=ReadMe_Window
        self.ReadMe_Window.title("ConsoleLancer")
        self.ReadMe_Window.geometry("1350x740")
        # ________________________________________________________________
        # -------------------------Frame And Background-------------------
        # ----------------------------------------------------------------

        # ===========================Frames===============================

        #-------------------First Frame-----------------------------------
        self.left = ImageTk.PhotoImage(file="Augmentation.png")
        left = tk.Label(self.ReadMe_Window, image=self.left)
        left.place(x=0, y=0, width=1350, height=195)

        #-------------------Second Frame----------------------------------
        frame2 = tk.Frame(self.ReadMe_Window, bd=2, bg="#111d20")
        frame2.place(x=0, y=195, width=300, height=547)

        #-------------------Third Frame----------------------------------
        frame3 = tk.Frame(self.ReadMe_Window,bg="#eeeef0")
        frame3.place(x=300, y=195,width=1050, height=547)


        # _________________________________________________________________
        # -----------------------Buttons-----------------------------------
        # -----------------------------------------------------------------

        #=====================Frame 1======================================
        '''This frame is containing Header. Which is already decleared & initialized in above code'''

        #=====================Button Area [Frame 2]========================

        #==========This button will throw you on user login page===========
        self.User_Login = ImageTk.PhotoImage(file="User.png")
        User = tk.Button(frame2,image=self.User_Login,activebackground="#111d20",font=("time new roman", 20, "bold"),command=self.user_page,bd=0,bg="#111d20",fg="#eeeef0", cursor="hand2")
        User.place(x=5,y=100)

        #==========This page will throw you on Admin login page===========
        self.Admin_Login = ImageTk.PhotoImage(file="Admin.png")
        Admin = tk.Button(frame2,image=self.Admin_Login,activebackground="#111d20",font=("time new roman", 20, "bold"),command=self.admin_page ,bd=0,bg="#111d20",fg="#eeeef0", cursor="hand2")
        Admin.place(x=5,y=200)

        #====================Description Area [Frame 3]====================
        ttk.Label(frame3,

                  text="DESCRIPTION",

                  font=("time new roman", 20, "bold"),

                  background='#eeeef0',

                  foreground="gray").place(x=400,y=50)

        #=================Creating scrolled Area===========================
        text_area = scrolledtext.ScrolledText(frame3,

                                              wrap=tk.WORD,

                                              width=80,

                                              height=16,

                                              font=("Times New Roman",

                                                    15))

        text_area.place(x=100,y=100)
        #========Inserting Product Description In Text Area===============

        file = open("product_Description.txt", "r")          #   Reading Product Description from file

        for line in file:
            x = line                    #   Passing Each line in x to insert in in text area
            text_area.insert(END,x)     #   Inserting Each Line in text area

                                        #   Placing cursor in the text area
        text_area.focus()


#___________________________________________________________________________________________________________________
#-----------------------------------------------BACK END CODE-------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    #=========Function to jump on Admin login page==============
    def admin_page(self):
        self.ReadMe_Window.destroy()

    #=========Function to jump on User login page===============
    def user_page(self):
        self.ReadMe_Window.destroy()


ReadMe_Window= tk.Tk()
ReadMe_Object=ReadMe_Class(ReadMe_Window)
ReadMe_Window.resizable(False, False)
ReadMe_Window.mainloop()