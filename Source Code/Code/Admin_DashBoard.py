#_________________________________________________________________________________________________________________
#-------------------------------------------Importing Required Package(API)---------------------------------------
#-----------------------------------------------------------------------------------------------------------------

import mysql
from PIL import ImageTk
import tkinter as tk
import mysql.connector
from tkinter import ttk, filedialog
from xlwt import Workbook

# _________________________________________________________________________________________________________________
# -----------------------------------------------------FRONT END CODE----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

class Admin_Dashboard_Class:

    #=====Admin_dashboard_Window Function===========
    def __init__(self,Admin_dashboard_Window):
        self.Admin_dashboard_Window=Admin_dashboard_Window
        self.Admin_dashboard_Window.title("ConsoleLancer")
        self.Admin_dashboard_Window.geometry("1350x740")

        # ________________________________________________________________
        # -------------------------Frame And Background-------------------
        # ----------------------------------------------------------------

        # ===========================Frames===============================

        # -------------------First Frame-----------------------------------
        self.topLeft = ImageTk.PhotoImage(file="Admin_TopLeft.png")
        topleft = tk.Label(self.Admin_dashboard_Window, image=self.topLeft)
        topleft.place(x=-2, y=0)

        # -------------------Second Frame----------------------------------
        self.left = ImageTk.PhotoImage(file="Admin_panel_Header.png")
        left = tk.Label(self.Admin_dashboard_Window, image=self.left)
        left.place(x=300, y=0, width=1050, height=195)

        # -------------------Third Frame----------------------------------
        frame3 = tk.Frame(self.Admin_dashboard_Window,bd=2,bg="#141F23")
        frame3.place(x=-5, y=250, width=310, height=547)

        # -------------------Fourth Frame----------------------------------
        self.frame4 = tk.Frame(self.Admin_dashboard_Window,bg="#3b3f42")
        self.frame4.place(x=300, y=195, width=1050, height=547)

        #=====================Blank Area [frame 1]=========================

        #-------Connecting To DataBase For Printing Admin Name-------------
        mydbadmin = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
        cursoradmin = mydbadmin.cursor()
        sql = "SELECT `admin` FROM `adminTab`"
        #-----------------------Fetching Admin Name-------------------------
        cursoradmin.execute(sql)
        adminName = cursoradmin.fetchone()
        for i in adminName:
            x = adminName

        #-----------------Printing Admin Name On Deshboard------------------
        self.admin_Name = tk.Label(self.Admin_dashboard_Window, text="%s"%adminName, font=("time new roman",15, "bold"), bg="#141F23",
                              fg="#838786")
        self.admin_Name.place(x=75,y=190)

        #-----------------------Sepration Line------------------------------
        self.line = ImageTk.PhotoImage(file="Line.png")
        line = tk.Label(self.Admin_dashboard_Window, image=self.line,bg="#293f4c", width=260)
        line.place(x=20, y=230)

        '''This frame is holding Admin Menu bar Title'''

        #=====================Admin Panel Heading [Frame 2]================
        '''This frame is containing Header. Which is already decleared & initialized in above code'''

        #=====================Button Area [Frame 3]========================

        #-------------Creating and placing  Show Feature Button---------------
        self.Feature_show_img = ImageTk.PhotoImage(file="Feature_show.png")
        self.Feature_show_Button = tk.Button(frame3,image=self.Feature_show_img,activebackground="#172637",width=400,bg="#1a262b", command=self.show_Feature, bd=0, cursor="hand2")
        self.Feature_show_Button.place(x=-100, y=25)

        # ----------------------Creating hide button---------------------------
        self.Feature_hide_img = ImageTk.PhotoImage(file="Feature_hide.png")
        self.Feature_hide_Button = tk.Button(frame3, image=self.Feature_hide_img, activebackground="#172637",
                              fg="white", width=400, bg="#1a262b",
                              command=self.hide_Feature, bd=0, cursor="hand2")

        # --------------------Creating Sign out button-------------------------
        self.admin_Sign_out_img = ImageTk.PhotoImage(file="Admin_sing_Out.png")
        self.admin_Sign_out_btt = tk.Button(frame3,image=self.admin_Sign_out_img, activebackground="#172637", bg="#1a262b",width=400,
                                            command=self.sign_out, bd=0, cursor="hand2")

        #------------------Creating User Information button-------------------
        self.user_info_img = ImageTk.PhotoImage(file="User_Info.png")
        self.user_Info_btt = tk.Button(frame3,image=self.user_info_img,activebackground="#172637",bg="#1a262b",width=400, command=self.user_Info, bd=0, cursor="hand2")

        #-----Creating Download button for Downloading user information-------
        self.Download_button_img = ImageTk.PhotoImage(file="Download_info.png")
        self.download_btt = tk.Button(frame3,image=self.Download_button_img,activebackground="#172637",bg="#1a262b",width=400, command=self.download, bd=0, cursor="hand2")

        #-------creating button for Hide Download Feature---------------------
        self.download1_btt = tk.Button(frame3,image=self.Download_button_img,activebackground="#172637",
                                      bg="#1a262b",width=400, command=self.download1, bd=0, cursor="hand2")



        #========================Download Info=================================

        #------------Creating button for downloading all details---------------
        self.All_info_img = ImageTk.PhotoImage(file="All_info.png")
        self.download_All_btt = tk.Button(frame3,image=self.All_info_img,activebackground="#172637",width=400,bg="#1a262b",command=self.user_All,
                                        bd=0, cursor="hand2")

        #-------------Creating button for downloading name of users-------------
        self.Name_info_img = ImageTk.PhotoImage(file="Name_info.png")
        self.download_Name_btt = tk.Button(frame3,image=self.Name_info_img,activebackground="#172637", width=400,bg="#1a262b", command=self.user_Name, bd=0, cursor="hand2")

        #------------Creating button for downloading number -------------------
        self.Number_info_img = ImageTk.PhotoImage(file="Number_Info.png")
        self.download_Number_btt = tk.Button(frame3,image=self.Number_info_img,activebackground="#172637", width=400,bg="#1a262b" ,command=self.user_Number, bd=0, cursor="hand2")

        #------------Creating button for downloading ID-------------------
        self.ID_info_img = ImageTk.PhotoImage(file="Email_Info.png")
        self.download_Id_btt = tk.Button(frame3,image=self.ID_info_img,activebackground="#172637",width=400,bg="#1a262b", command=self.user_ID, bd=0, cursor="hand2")


        # ====================Description Area [Frame 4]====================

        #---------------Placing Headig in frame 4 --------------------------
        self.title = tk.Label(self.frame4, text="USER INFORMATION",font=("time new roman", 20, "bold"), bg="#3b3f42" , fg="white")

        #----------------Placing default image in frame 4 --------------------
        self.welcomeimg = ImageTk.PhotoImage(file="Admin_Welcome.png")
        self.welcome = tk.Label(self.frame4, image=self.welcomeimg,bg="#3b3f42" )
        self.welcome.place(x=300, y=50)

        '''Form 4 code is working for Back End'''
# ___________________________________________________________________________________________________________________
# -----------------------------------------------BACK END CODE-------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

    #========================Creating function for showing feature==================
    def show_Feature(self):
        self.Feature_show_Button.place_forget()
        self.Feature_hide_Button.place(x=-100, y=25)

        self.admin_Sign_out_btt.place(x=-95, y=65)
        self.user_Info_btt.place(x=-90, y=110)
        self.download_btt.place(x=-90, y=150)


    def download(self):
        self.download_btt.place_forget()
        self.download1_btt.place(x=-90, y=150)

        self.download_All_btt.place(x=-55,y=190)
        self.download_Name_btt.place(x=-50,y=230)
        self.download_Number_btt.place(x=-50, y=270)
        self.download_Id_btt.place(x=-55,y=308)



    def download1(self):
        self.download1_btt.place_forget()
        self.download_btt.place(x=-90, y=150)

        self.download_All_btt.place_forget()
        self.download_Name_btt.place_forget()
        self.download_Number_btt.place_forget()
        self.download_Id_btt.place_forget()

    def hide_Feature(self):
        self.Feature_hide_Button.place_forget()
        self.Feature_show_Button.place(x=-100, y=25)
        self.user_Info_btt.place_forget()
        self.download_btt.place_forget()
        self.admin_Sign_out_btt.place_forget()
        self.download1_btt.place_forget()
        self.download_All_btt.place_forget()
        self.download_Name_btt.place_forget()
        self.download_Number_btt.place_forget()
        self.download_Id_btt.place_forget()


#=========================Function for User Registration================
    def user_Info(self):
        self.welcome.place_forget()
        self.title.place(x=400, y=80)
        mydb = mysql.connector.connect(user="root", password ="", database="aug", host="localhost")
        cursor = mydb.cursor()
        sql = "SELECT `first_name`, `last_name`, `phone_no`, `mail` FROM `user`"

        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount

        tv = ttk.Treeview(self.frame4, columns = (1,2,3,4), show = "headings", height ="8")
        tv.place(x=120,y=150)

        tv.heading(1, text="First Name")
        tv.heading(2, text="Last Name")
        tv.heading(3, text="Phone Number")
        tv.heading(4, text="Email Id")

        for i in rows:
            tv.insert('', 'end', values = i)

        cursor.close()
        mydb.close

    def user_All(self):
        nameFilePath = filedialog.askdirectory(parent=Admin_dashboard_Window,initialdir="/path/to/start/",title='Please select a directory')

        if nameFilePath=="":
            pass
        else:
            #=============================Fetching First Name================================
            mydb1 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor1 = mydb1.cursor()
            sql = "SELECT `first_name` FROM `user`"

            cursor1.execute(sql)
            rows1 = cursor1.fetchall()
            #total = cursor1.rowcount
            wb = Workbook()

            sheet1 = wb.add_sheet('Sheet 1')
            sheet1.write(0, 0,'First Name')
            sheet1.write(0, 1, 'Last Name')
            sheet1.write(0, 2, 'Phone Number')
            sheet1.write(0, 3, 'Gmail ID')

            row_no1 = 1
            for i in rows1:
                sheet1.write(row_no1, 0, "%s" % i)  # 1 is used for rows
                row_no1 = row_no1 + 1
            cursor1.close()
            mydb1.close()

            #=========================Fetching  Last Name ===============================
            mydb2 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor2 = mydb2.cursor()
            sql = "SELECT `last_name` FROM `user`"

            cursor2.execute(sql)
            rows2 = cursor2.fetchall()

            row_no2 = 1
            for j in rows2:
                sheet1.write(row_no2, 1, "%s" % j)  # 1 is used for rows
                row_no2 = row_no2 + 1
            cursor2.close()
            mydb2.close()

            #==========================Fetching Number========================================
            mydb3 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor3 = mydb3.cursor()
            sql = "SELECT `phone_no` FROM `user`"

            cursor3.execute(sql)
            rows3 = cursor3.fetchall()

            row_no3 = 1
            for j in rows3:
                sheet1.write(row_no3, 2, "%s" % j)  # 1 is used for rows
                row_no3 = row_no3 + 1
            cursor3.close()
            mydb3.close()

            #=============================Fetching Gmail ID====================================

            mydb4 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor4 = mydb4.cursor()
            sql = "SELECT `mail` FROM `user`"

            cursor4.execute(sql)
            rows4 = cursor4.fetchall()

            row_no4 = 1
            for j in rows4:
                sheet1.write(row_no4, 3, "%s" % j)  # 1 is used for rows
                row_no4 = row_no4 + 1
            cursor4.close()
            mydb4.close()
            wb.save('%s/All Information.xls' % nameFilePath)

    def user_Name(self):
        nameFilePath = filedialog.askdirectory(parent=Admin_dashboard_Window,initialdir="/path/to/start/",title='Please select a directory')

        if nameFilePath=="":
            pass
        else:
            mydb1 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor1 = mydb1.cursor()
            sql = "SELECT `first_name` FROM `user`"

            cursor1.execute(sql)
            rows = cursor1.fetchall()
            total = cursor1.rowcount
            wb = Workbook()

            sheet1 = wb.add_sheet('Sheet 1')
            row_no =1
            for i in rows:
                sheet1.write(row_no,0,"%s"% i)  # 1 is used for rows
                row_no = row_no + 1
            cursor1.close()
            mydb1.close()

            mydb2 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor2 = mydb2.cursor()
            sql = "SELECT `last_name` FROM `user`"

            cursor2.execute(sql)
            rows2 = cursor2.fetchall()

            row_no1 = 1
            for j in rows2:
                sheet1.write(row_no1,1, "%s" % j)  # 1 is used for rows
                row_no1 = row_no1 + 1
            cursor2.close()
            mydb2.close()
            wb.save('%s/User_Name.xls' % nameFilePath)

    def user_Number(self):

        numberFilePath = filedialog.askdirectory(parent=Admin_dashboard_Window,initialdir="/path/to/start/",title='Please select a directory')

        if numberFilePath=="":
            pass
        else:

            mydb3 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor3 = mydb3.cursor()
            sql = "SELECT `phone_no` FROM `user`"

            cursor3.execute(sql)
            rows3 = cursor3.fetchall()
            total = cursor3.rowcount
            wb = Workbook()

            sheet3 = wb.add_sheet('Sheet 1')
            row_no = 1
            for i in rows3:
                sheet3.write(row_no, 0, "%s" % i)  # 1 is used for rows
                row_no = row_no + 1
            cursor3.close()
            mydb3.close()
            wb.save('%s/User_Number.xls' % numberFilePath)

    def user_ID(self):

        idFilePath = filedialog.askdirectory(parent=Admin_dashboard_Window,initialdir="/path/to/start/",title='Please select a directory')

        if idFilePath == "":
            pass
        else:

            mydb4 = mysql.connector.connect(user="root", password="", database="aug", host="localhost")
            cursor4 = mydb4.cursor()
            sql = "SELECT `mail` FROM `user`"

            cursor4.execute(sql)
            rows4 = cursor4.fetchall()
            total = cursor4.rowcount
            wb = Workbook()

            sheet1 = wb.add_sheet('Sheet 1')
            row_no = 1
            for i in rows4:
                sheet1.write(row_no, 0, "%s" % i)  # 1 is used for rows
                row_no = row_no + 1
            cursor4.close()
            mydb4.close()

            wb.save('%s/User_ID.xls' % idFilePath)

#==================This function is working for achiving Logout Functionality==================
    def sign_out(self):
        self.Admin_dashboard_Window.destroy()
        from Data_Augmentation import Admin_login


Admin_dashboard_Window= tk.Tk()
Admin_dashboard_Object=Admin_Dashboard_Class(Admin_dashboard_Window)
Admin_dashboard_Window.resizable(False, False)
Admin_dashboard_Window.mainloop()