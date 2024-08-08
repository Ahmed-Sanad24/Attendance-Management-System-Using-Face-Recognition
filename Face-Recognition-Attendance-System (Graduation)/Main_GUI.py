#======== Import Liberaries ========
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import csv
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import tkinter as tk
from mtcnn import MTCNN
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


mydata=[]

class Face_Recognition_System:
    def __init__(self,root):
        self.graph_frame = None  # Global variable to hold the graph frame
        self.root=root
        self.root.geometry("1800x780+0+0")
        self.root.state('zoomed')
        self.root.title("Face Recognition System")
        root.config(bg="red")
        #root.overrideredirect(True)

        self.root.wm_iconbitmap("camera.ico")
        self.screenwidth = int(root.winfo_screenwidth())
        self.screenheight = int(root.winfo_screenheight())



        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        #variables
        self.var_dep = StringVar()
        self.var_std_id = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()


        self.var_radio1 = StringVar()

        self.present_students = []
        self.absent_students = []
        original_image = Image.open("images/login.jpg")

        # Resize the image
        resized_image = original_image.resize((self.screenwidth, self.screenheight), Image.Resampling.LANCZOS)

        # Create a PhotoImage object from the resized image
        self.bg = ImageTk.PhotoImage(resized_image)

        # self.bg=ImageTk.PhotoImage(file=r"images\login.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#E5E0DA")
        frame1.place(x=int(self.screenwidth/8),y=int(self.screenheight/4),width=int(self.screenwidth/4),height=int(self.screenheight/1.4))
        frame1.columnconfigure(0,weight=1)
        frame1.columnconfigure(1,weight=1)

        img1=Image.open(r"images\log2.png")
        img1=img1.resize((int(self.screenheight/12),int(self.screenheight/12)),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(frame1,image=self.photoimage1,bg="#E5E0DA")
        lb1img1.grid(row=0,column=0,columnspan=2,pady=int(self.screenheight/100))

        get_str = Label(frame1,text="Login",font=("times new roman",25,"bold"),fg="#1D120E",bg="#E5E0DA")
        get_str.grid(row=1,column=0,columnspan=2,pady=int(self.screenheight/100))

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",20,"bold"),fg="#1D120E",bg="#E5E0DA")
        username.grid(row=2,column=0,columnspan=2,pady=(int(self.screenheight/100),0))

        #entry1 



    
        self.txtuser=Entry(frame1,font=("times new roman",20,"bold"),bg="#b5a29b")

        self.txtuser.grid(row=3,column=0,columnspan=2,pady=(0,int(self.screenheight/100)))


        #label2 
        pwd = Label(frame1,text="Password:",font=("times new roman",20,"bold"),fg="#1D120E",bg="#E5E0DA")
        pwd.grid(row=4,column=0,columnspan=2,pady=(int(self.screenheight/100),0))

        #entry2 
        self.txtpwd=Entry(frame1,font=("times new roman",20,"bold"),bg="#b5a29b")
        self.txtpwd.grid(row=5,column=0,columnspan=2,pady=(0,int(self.screenheight/100)))


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",20,"bold"),bd=0,relief=RIDGE,fg="#E5E0DA",bg="#1D120E",activeforeground="#1D120E",activebackground="#007ACC")
        loginbtn.grid(row=6,column=0,columnspan=2,pady=int(self.screenheight/100))


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.regcommand,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#1D120E",bg="#E5E0DA",activeforeground="orange",activebackground="#E5E0DA")
        loginbtn.grid(row=7,column=0,pady=int(self.screenheight/100))


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#1D120E",bg="#E5E0DA",activeforeground="orange",activebackground="#E5E0DA")
        loginbtn.grid(row=7,column=1,pady=int(self.screenheight/100))

    #  THis function is for open register window
    def regcommand(self):
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()
        original_image = Image.open("images/register.jpg")
        # Resize the image
        resized_image = original_image.resize((self.screenwidth, self.screenheight), Image.Resampling.LANCZOS)
        # Create a PhotoImage object from the resized image
        self.bg = ImageTk.PhotoImage(resized_image)
        # self.bg=ImageTk.PhotoImage(file=r"images\register.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)
        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)
        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)
        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)
        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)
        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)
        # ==================== section 2 -------- 2nd Columan===================
        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)
        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)
        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)
        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)
        # ========================= Section 3 --- 1 Columan=================
        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=350)
        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)
        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=420)
        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)
        # ========================= Section 4-----Column 2=============================
        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)
        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)
        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)
        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)
        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)
        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)
        # Creating Button Login
        loginbtn=Button(frame,command=self.testf,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=533,y=510,width=270,height=35)

    def testf(self):
        self.__init__(root)



    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Passwords are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    def login(self):
        # if (self.txtuser.get()=="" or self.txtpwd.get()==""):
        #     messagebox.showerror("Error","All Field Required!")
        # elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
        #     messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        # else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            # conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
            # mycursor = conn.cursor()
            # mycursor.execute("select * from regteach where email=%s and pwd=%s",(
            #     self.txtuser.get(),
            #     self.txtpwd.get()
            # ))
            # row=mycursor.fetchone()
            # if row==None:
            #     messagebox.showerror("Error","Invalid Username and Password!")
            # else:
                self.options_frame = tk.Frame(root,bg='#c3c3c3')
                w = root.winfo_screenheight()/18
                # print(w)
                global college_img
                img=Image.open(r"images\2.png")
                img=img.resize((int(self.screenwidth/10),int(self.screenheight/8)),Image.Resampling.LANCZOS)
                college_img=ImageTk.PhotoImage(img)

                self.college_label=Label(self.options_frame,image=college_img, background = '#c3c3c3')
                self.college_label.place(x=0,y=0,width=self.screenwidth/10,height=self.screenheight/8)

                home_btn = tk.Button (self.options_frame, text="Home", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.home_page))
                home_btn.place(x=10,y=self.screenheight/3)
                self.home_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.home_indicate.place(x=4,y=self.screenheight/3,width=5,height=43)

                menu_btn = tk.Button (self.options_frame, text="Recognition", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.menu_indicate,self.recognition_page))
                menu_btn.place(x=10,y=self.screenheight/3+w)
                self.menu_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.menu_indicate.place(x=4,y=self.screenheight/3+w,width=5,height=43)

                contact_btn = tk.Button (self.options_frame, text="Count Students", font=('Bold ', 14),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.contact_indicate,self.count_page))
                contact_btn.place(x=10,y=self.screenheight/3+2*w)
                self.contact_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.contact_indicate.place(x=4,y=self.screenheight/3+2*w,width=5,height=43)

                exit_btn = tk.Button (self.options_frame, text="EXIT", font=('Bold ', 18),fg= '#158aff', bd=0,relief=RIDGE, bg='#c3c3c3',command=self.IExit)
                exit_btn.place(x=50,y=self.screenheight/3+7*w)
                self.exit_btn_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.exit_btn_indicate.place(x=4,y=self.screenheight/3+7*w,width=5,height=43)



                global exit_image
                original_image = Image.open("images\exiticon.png")
                # Resize the image
                resized_image = original_image.resize((40, 40))  # Adjust the size as needed
                # Convert the resized image to a Tkinter-compatible format
                exit_image = ImageTk.PhotoImage(resized_image)
                # Create the button with the resized icon image
                button = tk.Button(self.options_frame, image=exit_image, command=self.IExit , bg ="#c2c2c2" , relief=FLAT)
                button.place(x=10,y=self.screenheight/3+7*w)
















                statics_btn = tk.Button (self.options_frame, text="Statics", font=('Bold ', 18),fg= '#158aff', bd=0,relief=RIDGE, bg='#c3c3c3',command=lambda :self.indicate(self.statics_btn_indicate,self.statics_page))
                statics_btn.place(x=10,y=self.screenheight/3+3*w)
                self.statics_btn_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.statics_btn_indicate.place(x=4,y=self.screenheight/3+3*w,width=5,height=43)


                Data_btn = tk.Button (self.options_frame, text="Photos", font=('Bold ', 18),fg= '#158aff', bd=0,relief=RIDGE, bg='#c3c3c3',command=lambda :self.indicate(self.Data_btn_indicate,self.data_page))
                Data_btn.place(x=50,y=self.screenheight/3+6*w)
                self.Data_btn_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
                self.Data_btn_indicate.place(x=4,y=self.screenheight/3+6*w,width=5,height=43)


                global icon_image
                original_image = Image.open("images\photosicon.png")
                # Resize the image
                resized_image = original_image.resize((40, 40))  # Adjust the size as needed
                # Convert the resized image to a Tkinter-compatible format
                icon_image = ImageTk.PhotoImage(resized_image)
                # Create the button with the resized icon image
                button = tk.Button(self.options_frame, image=icon_image, command=lambda :self.indicate(self.Data_btn_indicate,self.data_page) , bg ="#c2c2c2" , relief=FLAT)
                button.place(x=10,y=self.screenheight/3+6*w)


                self.options_frame.pack(side=tk.LEFT)
                self.options_frame.pack_propagate(False)
                self.options_frame.configure(width=self.screenwidth/10,height=self.screenheight)


                self.main_frame = tk.Frame(root,highlightbackground='#c3c3c3',highlightthickness=0)
                self.main_frame.pack(side=tk.LEFT)
                self.main_frame.pack_propagate(False)
                self.main_frame.configure(width=self.screenwidth-self.screenwidth/10,height=self.screenheight)

                self.home_page()

                #========================= Display time =========================
                def time():
                        string = strftime('%H:%M:%S %p')
                        Ibl.config(text=string)
                        Ibl.after(1000, time)

                Ibl = Label(self.options_frame, font =('Bold',16),background='#c3c3c3',foreground='#158aff',padx=0)
                Ibl.place(x=0,y=self.screenheight-self.screenheight/10,width=160,height=50)
                time()        
                #========================= END Display time =========================
                self.home_page()
              
            # conn.commit()
            # conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)
























        # print(screenheight)
        # print(screenwidth)


        

        
        

    def home_page(self):
        global photoimg
               
        photowidth = int(self.screenwidth-self.screenwidth/10)
        photoheight = int(self.screenheight)
        img=Image.open(r"images\bg.jpg")
        img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
        photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.main_frame,image=photoimg)
        bg_img.place(x=0,y=0,width=self.screenwidth-self.screenwidth/10,height=self.screenheight)
    
        

        buttons_frame = tk.Frame(self.main_frame,bg="#c3c3c3",highlightbackground='white',highlightthickness=0)
        buttons_frame.pack(side=tk.TOP,anchor=E,pady=(20,0))
        buttons_frame.grid_propagate(False)
        buttons_frame.configure(width=self.screenwidth-self.screenwidth/10,height=self.screenheight/25)

        buttons_frame.columnconfigure(0,weight=99)
        buttons_frame.columnconfigure(1,weight=1)
        buttons_frame.columnconfigure(2,weight=1)
        buttons_frame.columnconfigure(3,weight=1)
        buttons_frame.columnconfigure(4,weight=99)

        buttons_frame.rowconfigure(0,weight=3)
        buttons_frame.rowconfigure(1,weight=8)




        self.student_button = tk.Button (buttons_frame, text="Student Details", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.student_page))
        self.student_button.grid(row=0,column=1,padx=0)
        # self.student_indicate = tk.Label(buttons_frame, text='',bg='#158aff',width=22,pady=4)
        # self.student_indicate.grid(row=1,column=1,pady=3)

        self.attendance_button = tk.Button (buttons_frame, text="Attendance panel", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.attendance_page))
        self.attendance_button.grid(row=0,column=2)
        # self.attendance_indicate = tk.Label(buttons_frame, text='',bg='#158aff',width=16,pady=4)
        # self.attendance_indicate.grid(row=1,column=2,pady=3)
       





    def recognition_page(self):
        global photoimg
               
        photowidth = int(self.screenwidth-self.screenwidth/10)
        photoheight = int(self.screenheight)
        img=Image.open(r"images\bg.jpg")
        img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
        photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.main_frame,image=photoimg)
        bg_img.place(x=0,y=0,width=self.screenwidth-self.screenwidth/10,height=self.screenheight)


         #FaceDetector button

        img5=Image.open(r"images\student.jpg")
        img5=img5.resize((int(self.screenwidth/6),int(self.screenwidth/6)),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition,bd=3 , background="#c3c3c3")
        b1.place(x=self.screenwidth/20,y=self.screenwidth/20,width = int(self.screenwidth/6), height=int(self.screenwidth/6))
        b1_label=Button(bg_img,text="Face Detector",cursor="hand2",font =('Bold ', 16),bg="#c3c3c3",fg="#158aff",bd=3,command=self.face_recognition)
        b1_label.place(x=self.screenwidth/20,y=self.screenwidth/20+int(self.screenwidth/6),width = int(self.screenwidth/6), height=int(self.screenwidth/60))


         #Train databutton

        img7=Image.open(r"images\train.jpg")
        img7=img7.resize((int(self.screenwidth/6),int(self.screenwidth/6)),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_classifier,bd=3 , background="#c3c3c3")
        b1.place(x=self.screenwidth/20,y=(self.screenwidth/20)*1.5+int(self.screenwidth/6)+int(self.screenwidth/40),width = int(self.screenwidth/6), height=int(self.screenwidth/6))

        b1_label=Button(bg_img,text="Train Data",cursor="hand2",font =('Bold ', 16),bg="#c3c3c3",fg="#158aff",bd=3 ,command=self.train_classifier)
        b1_label.place(x=self.screenwidth/20,y=(self.screenwidth/20)*1.5+int(self.screenwidth/6)*2+int(self.screenwidth/40),width = int(self.screenwidth/6), height=int(self.screenwidth/60))
        

    def statics_page(self):

        # Connect to the MySQL database
        # conn = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password='Test@123',
        #     database='face_recognizer'
        # )
        # cursor = conn.cursor()

        # # Fetch student data from the 'students' table
        # cursor.execute("SELECT  Dep, count(*) FROM student GROUP BY Dep")
        # student_data = cursor.fetchall()

        # # Fetch class data from the 'students' table
        # cursor.execute("SELECT Division, count(*) FROM student GROUP BY Division")
        # class_data = cursor.fetchall()

        # # Fetch photosample data from the 'student' table
        # cursor.execute("SELECT PhotoSample, count(*) FROM student GROUP BY PhotoSample")
        # photosample_data = cursor.fetchall()

        # # Fetch teacher data from the 'student' table
        # cursor.execute("SELECT Teacher, count(*) FROM student GROUP BY Teacher")
        # teacher_data = cursor.fetchall()

        # # Close the database connection
        # conn.close()

        # Prepare the data for plotting
        student_data=[]
        class_data=[]
        photosample_data=[]
        teacher_data=[]
        departments = [row[0] for row in student_data]
        student_counts = [row[1] for row in student_data]

        classes = [row[0] for row in class_data]
        class_counts = [row[1] for row in class_data]

        photosamples = [row[0] for row in photosample_data]
        photosample_counts = [row[1] for row in photosample_data]

        teachers = [row[0] for row in teacher_data]
        teacher_counts = [row[1] for row in teacher_data]

        # Frame to contain the graphs
        frame = tk.Frame(self.main_frame)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Create a Figure object from matplotlib
        fig = Figure(figsize=(12, 8), dpi=100)

        # Subplot for student statistics by department
        ax_student_dept = fig.add_subplot(221, facecolor='lightgray')
        ax_student_dept.bar(departments, student_counts, color='skyblue')
        ax_student_dept.set_xlabel("Department")
        ax_student_dept.set_ylabel("Number of Students")
        ax_student_dept.set_title("Student Statistics by Department")

        # Subplot for class distribution
        ax_class_dist = fig.add_subplot(222, facecolor='lightgray')
        ax_class_dist.pie(class_counts, labels=classes, autopct='%1.1f%%', colors=['lightgreen', 'lightblue', 'lightyellow', 'pink'])
        ax_class_dist.set_title("Class Distribution")

        # Subplot for photosample distribution
        ax_photosample = fig.add_subplot(223, facecolor='lightgray')
        ax_photosample.pie(photosample_counts, labels=photosamples, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
        ax_photosample.set_title("Photosample Distribution")

        # Subplot for teacher statistics
        ax_teacher = fig.add_subplot(224, facecolor='lightgray')
        colors = plt.cm.get_cmap('rainbow', len(teachers))  # Generate a colormap based on the number of teachers
        ax_teacher.bar(teachers, teacher_counts, color=colors(np.arange(len(teachers))))
        ax_teacher.set_xlabel("Teacher")
        ax_teacher.set_ylabel("Number of Students")
        ax_teacher.set_title("Teacher Statistics")
        ax_teacher.tick_params(axis='x', labelrotation=45)  # Rotate x-axis labels for better visibility

        # Adjust spacing between subplots
        fig.subplots_adjust(hspace=0.4)

        # Create a Tkinter canvas to display the graph
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
    def data_page(self):
        self.home_page()
        os.startfile("data")

        
     
            
    def count_page(self):

        def resize_image(image, max_width, max_height):
            """
            Resize the image while maintaining aspect ratio to fit within the specified dimensions.
            """

            width, height = image.size

            # Calculate aspect ratios
            aspect_ratio = width / height
            target_aspect_ratio = max_width / max_height

            if aspect_ratio > target_aspect_ratio:
                # Image is wider, resize based on width
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
            else:
                # Image is taller or square, resize based on height
                new_height = max_height
                new_width = int(new_height * aspect_ratio)

            # Resize the image
            resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            return resized_image


        def browse_image():
            # Prompt the user to select an image file
            filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
            
            # Load the selected image
            image = cv2.imread(filepath)
            
            # Convert the image to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Perform face detection
            faces = detector.detect_faces(image_rgb)
            face_count = len(faces)
            
            # Update the face count label
            face_count_label.config(text=f"Number of faces found: {face_count}")
            
            # Draw rectangles around the detected faces
            for face in faces:
                x, y, w, h = face['box']
                cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Convert the image to PIL format
            image_pil = Image.fromarray(image_rgb)
            
            # Create a Tkinter-compatible photo image
            resized_image = resize_image(image_pil , 1000 ,1000)

            photo = ImageTk.PhotoImage(resized_image)
            
            # Update the image in the GUI
            image_label.config(image=photo)
            image_label.image = photo


        
        
        global photoimg
               
        photowidth = int(self.screenwidth-self.screenwidth/10)
        photoheight = int(self.screenheight)
        img=Image.open(r"images\data_bg.jpg")
        img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
        photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.main_frame,image=photoimg)
        bg_img.place(x=0,y=0,width=self.screenwidth-self.screenwidth/10,height=self.screenheight)

        


        home_frame = tk.Frame(self.main_frame)
        browse_button = tk.Button(self.main_frame, text="Browse", command=browse_image, font=('bold',20),bg="#c3c3c3")
        browse_button.pack(pady=(10,0))

        # Create a label to display the face count
        face_count_label = tk.Label(self.main_frame, text="Number of students found: 0" , font=('bold',30) , foreground="black",bg="#c3c3c3")
        face_count_label.pack(pady=(0,20))

        # Create a label to display the image
        image_label = tk.Label(self.main_frame,bg="#c3c3c3")
        image_label.config(text="the image with detected faces will appear here ..")
        image_label.pack()

        # Load the MTCNN model
        detector = MTCNN(steps_threshold=[0.6, 0.7, 0.7], min_face_size=40)


        home_frame.pack()
    def exit_btn_page(self):
        home_frame = tk.Frame(self.main_frame)
        lb= tk.Label(home_frame,text='aaaaaaaaaa Frame\n\nPage: 1',font=('bold',50))
        lb.pack()
        home_frame.pack()
    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
    def indicate(self,lb,page):
        self.home_indicate.config(bg="#c3c3c3")
        self.menu_indicate.config(bg="#c3c3c3")
        self.contact_indicate.config(bg="#c3c3c3")
        self.exit_btn_indicate.config(bg="#c3c3c3")
        self.Data_btn_indicate.config(bg="#c3c3c3")
        self.statics_btn_indicate.config(bg="#c3c3c3")

        self.delete_page()
        page()
        

        lb.config(bg='#158aff')
    def student_page(self):
        self.home_page()
        self.student_button.configure(bd=1,relief=SUNKEN)
        main_student_frame = tk.Frame(self.main_frame,bg="#243641",highlightbackground='red',highlightthickness=0)
        main_student_frame.pack(side=tk.TOP,anchor=CENTER,pady=0)
        main_student_frame.grid_propagate(False)
        main_student_frame.configure(width=(self.screenwidth-self.screenwidth/10),height=self.screenheight-self.screenheight/25)
        #============================ Variables ================

        

        
        left_frame=LabelFrame(main_student_frame, bd=1,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        left_frame.grid(row=1,column=0,sticky='WENS',padx=0,pady=5)

        left_frame.grid_propagate(False)
        left_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=(self.screenheight-self.screenheight/25)/2)
        
        # left_frame.rowconfigure(0,weight=1)
        # left_frame.rowconfigure(1,weight=3)
        # left_frame.rowconfigure(2,weight=3)


        left_frame.columnconfigure(0,weight=1)
        left_frame.columnconfigure(1,weight=1)

        img_left=Image.open(r"images\2.png")
        global photoimg_left
        photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(left_frame,image=photoimg_left,bg="#DDFFFD",height= 125)
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

        current_course_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


        # Department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select department","Computer science","Control Engineering","Communication Engineering","Medical Engineering" , "Mechatronics Engineering","Automation")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")


    # Course
        dep_label=Label(current_course_frame,text="Course:",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select course","Data structure","Computer networks","Embedded system","Computer vision")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=4,pady=10,sticky="W")

        # Year
        dep_label=Label(current_course_frame,text="Year:",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","Preparatory year","First year","Second year","Third year","Forth year")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=4,pady=10)

        # Semester
        dep_label=Label(current_course_frame,text="Semester:",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","2022-2023","2023-2024","2024-2025","2025-2026")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=4,pady=10,sticky="W")


    #=========================== Class Student information=============================

        class_student_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        class_student_frame.grid(row=2,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)



        #student ID
        student_frame=Label(class_student_frame,text="StudentID:",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=0,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=0,column=1,padx=5,pady=5,sticky="W")

        #student name
        student_frame=Label(class_student_frame,text="Student name:",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=0,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=0,column=3,padx=5,pady=5,sticky="W")


        #Roll number
        student_frame=Label(class_student_frame,text="Roll number:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=1,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=1,column=1,padx=5,pady=5,sticky="W")


        #Gender
        student_frame=Label(class_student_frame,text="Gender:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=1,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=var_gender,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),width=13,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=4,pady=10)


        #Email
        student_frame=Label(class_student_frame,text="Email:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=2,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=2,column=1,padx=5,pady=5,sticky="W")

        #Phone number
        student_frame=Label(class_student_frame,text="Phone number:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=2,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=2,column=3,padx=5,pady=5,sticky="W")


        #Adress
        student_frame=Label(class_student_frame,text="Adress:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=3,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=3,column=1,padx=5,pady=5,sticky="W")


        #Date of birth
        student_frame=Label(class_student_frame,text="Date of birth:-",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=3,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=3,column=3,padx=5,pady=5,sticky="W")


        #Class division
        student_frame=Label(class_student_frame,text="Class division:",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=4,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=var_div,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=4,column=3,padx=10,pady=5,sticky="W")
        Div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),width=13,state="readonly")
        Div_combo["values"]=("Select div","A","B","C","D")
        Div_combo.current(0)
        Div_combo.grid(row=4,column=3,padx=4,pady=10)


        #Teacher
        student_frame=Label(class_student_frame,text="Teacher:",font=("times new roman",11,"bold"),bg="white")
        student_frame.grid(row=4,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",11,"bold"))
        student_entry.grid(row=4,column=1,padx=5,pady=5,sticky="W")



    #===================================== Radio buttons ======================================
        Radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0)

        # var_radio2 = StringVar()

        Radiobutton2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        Radiobutton2.grid(row=5,column=1)

    #=====================================  buttons frame ======================================

        # buttons_frame = Frame(class_student_frame,bd=2 , relief= RIDGE)
        # buttons_frame.grid(row=6 , column=0)

        buttons_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="",bg='white',padx=10, relief=RIDGE,fg="#00008B" )
        buttons_frame.grid(row=3,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)

        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)
        buttons_frame.columnconfigure(3, weight=1)


        save_button = Button(buttons_frame,command =self.add_data,text="Save",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        save_button.grid(row=6,column=0,sticky="WENS",pady=2 ,padx=2)

        update_button = Button(buttons_frame,command=self.update_data,text="Update",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        update_button.grid(row=6,column=1,sticky="WENS",pady=2,padx=2)

        delete_button = Button(buttons_frame,command=self.delete_data,text="Delete",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        delete_button.grid(row=6,column=2,sticky="WENS",pady=2,padx=2)

        Reset_button = Button(buttons_frame,command=self.reset_data,text="Reset",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        Reset_button.grid(row=6,column=3,sticky="WENS",pady=2,padx=2)

        take_photo_button = Button(buttons_frame,command=self.generate_dataset,text="Take photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        take_photo_button.grid(row=7,column=0, columnspan=2,sticky="WENS",pady=2,padx=2)

        update_photo_button = Button(buttons_frame,text="Update photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        update_photo_button.grid(row=7,column=2 ,columnspan=2,sticky="WENS",pady=2,padx=2)


    #================= RIGHT FRAME =====================

        right_frame=LabelFrame(main_student_frame, bd=1,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        right_frame.grid(row=1,column=1,sticky='W',padx=0,pady=5)

        right_frame.grid_propagate(False)
        right_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)
        
        
        # right_frame.rowconfigure(0,weight=1)
        # right_frame.rowconfigure(1,weight=3)
        # right_frame.rowconfigure(2,weight=3)


        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)

        img_right=Image.open(r"images\2.png")
        global photoimg_right
        photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(right_frame,image=photoimg_right,bg="#DDFFFD",height=125)
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="We")

        current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='W',padx=5,pady=5,ipadx=5,ipady=5)
        current_course_frame.grid_propagate(False)
        current_course_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2 , height= self.screenheight/14)
        current_course_frame.columnconfigure(0,weight=1)
        current_course_frame.columnconfigure(1,weight=1)
        current_course_frame.columnconfigure(2,weight=1)
        current_course_frame.columnconfigure(3,weight=1)
        current_course_frame.columnconfigure(4,weight=1)

        # Department
        dep_label=Label(current_course_frame,text="Search by:",font=("times new roman",10,"bold"),bg="red")
        dep_label.grid(row=0,column=0,padx=1,pady=4,sticky="wens")
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",10,"bold"),width=13,state="readonly")
        dep_combo["values"]=("Select","Roll number","Phone number")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=4,sticky="wens")

        search_entnry = ttk.Entry(current_course_frame,width=15,font=("times new roman",10,"bold"))
        search_entnry.grid(row=0,column=2,padx=1,pady=4,sticky="wens")

        save_button = Button(current_course_frame,text="Search",font=("times new roman",10,"bold"),bg="blue",fg="white",padx=1)
        save_button.grid(row=0,column=3,sticky="wens",pady=4 ,padx=2 ,ipady=0 , ipadx=1)

        showall_button = Button(current_course_frame,text="Show all",font=("times new roman",10,"bold"),bg="blue",fg="white",padx=1)
        showall_button.grid(row=0,column=4,sticky="wens",pady=4,padx=2 ,ipady=0 ,ipadx=1)


    #=================================== TABLE FRAME ==============================
        table_frame = Frame(right_frame,bd=0,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=self.screenheight/3.5,width=(self.screenwidth-self.screenwidth/10)/2.08)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("adress",text="Adress")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_studentdetails_cursor)
        self.fetch_data()

     #=============================== function decleration ====================
    def add_data(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succeffully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error" , f"Due to : {str(es)}",parent=self.root)
    def attendance_page(self):
        self.home_page()
        self.attendance_button.configure(bd=1,relief=SUNKEN)

        self.main_attendance_frame = tk.Frame(self.main_frame,bg="#111111",highlightbackground='red',highlightthickness=0)
        self.main_attendance_frame.pack(side=tk.TOP,anchor=CENTER,pady=0)
        self.main_attendance_frame.grid_propagate(False)
        self.main_attendance_frame.configure(width=(self.screenwidth-self.screenwidth/10),height=self.screenheight-self.screenheight/25)
        #===========variables=============
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # first header image  
        


        #========================Section Creating==================================
        
        # Creating Frame 
        

        # Left Label Frame 
        left_frame = LabelFrame(self.main_attendance_frame,bd=2,bg="white",relief=RIDGE,text="Attendance records",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.grid(row=1,column=0,sticky='WENS',padx=0,pady=5)
        left_frame.grid_propagate(False)
        left_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)
        left_frame.columnconfigure(0,weight=1)
        left_frame.columnconfigure(1,weight=1)
        left_frame.columnconfigure(2,weight=1)
        left_frame.columnconfigure(3,weight=1)

        left_frame.rowconfigure(0,weight=1)
        left_frame.rowconfigure(1,weight=1)
        left_frame.rowconfigure(2,weight=1)
        left_frame.rowconfigure(3,weight=2)
        left_frame.rowconfigure(4,weight=2)
        left_frame.rowconfigure(5,weight=2)
        left_frame.rowconfigure(6,weight=1)
        left_frame.rowconfigure(7,weight=1)
        left_frame.rowconfigure(8,weight=1)


        
        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(left_frame,text="Std-ID:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky="we")

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky="we")

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll.No:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky="we")

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky="we")

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky="we")

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky="we")

        #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky="we")

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky="we")

        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky="we")

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky="we")

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky="we")

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky="we")

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky="we")

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",10,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky="we")

        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.grid(row=3,rowspan=3,column=0,columnspan=4,padx=5,pady=5,sticky="wens")

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,height=4)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="Std-ID")
        self.attendanceReport_left.heading("Roll_No",text="Roll.No")
        self.attendanceReport_left.heading("Name",text="Std-Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend-status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Roll_No",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.grid(row=6,column=0,columnspan=4,padx=5,pady=5,sticky="we")
        btn_frame.columnconfigure(0,weight=1)
        btn_frame.columnconfigure(1,weight=1)
        btn_frame.columnconfigure(2,weight=1)
        btn_frame.columnconfigure(3,weight=1)
        #Improt button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky="we")

        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky="we")

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky="we")

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_attendance_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky="we")



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(self.main_attendance_frame,bd=2,bg="white",relief=RIDGE,text="ALL records",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.grid(row=1,column=1,sticky='w',padx=0,pady=5)
        right_frame.grid_propagate(False)
        right_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)
        right_frame.rowconfigure(0,weight=1)
        right_frame.rowconfigure(1,weight=1)

        right_frame.rowconfigure(2,weight=10)

        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.grid(row=2,column=0,columnspan=4,padx=5,pady=5,sticky="wens")
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,height=1)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_attendance_data()
    # =================================update for mysql button================
    #Update button
        del_btn=Button(right_frame,command=self.update_attendance_data,text="Alter table",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=0,padx=3,pady=10,sticky="we")
    #Update button
        del_btn=Button(right_frame,command=self.delete_attendance_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=1,column=0,padx=3,pady=10,sticky="we")

    #Update button
        #Graph
        global photoimg4
        img4=Image.open(r"images\visualization-icon-3.jpg")
        img4=img4.resize((int(self.screenwidth/9),int(self.screenwidth/18)),Image.Resampling.LANCZOS)
        photoimg4=ImageTk.PhotoImage(img4)
        B2=Button(right_frame,image=photoimg4,cursor="hand2" ,command=self.display_attendance_statistics)
        B2.grid(row=0, column=1,rowspan=2)
        B2 = Label(right_frame,bg="white",fg="#114579", text = " Make a Statistic Graph ",font=("Constantia", 10),pady=0)  # Button
        B2.grid(row=0, column=1,sticky="",pady=0 , ipady=0)








    def display_attendance_statistics(self):
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Test@123',
            database='face_recognition'
        )
        cursor = conn.cursor()

        # Fetch attendance data from the table
        cursor.execute("SELECT std_attendance, count(*) FROM stdattendance GROUP BY std_attendance")
        attendance_data = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Prepare the data for plotting
        statuses = [row[0] for row in attendance_data]
        counts = [row[1] for row in attendance_data]

        # Calculate the percentage of attendance and absence
        total_students = sum(counts)
        attendance_count = counts[statuses.index('Present')]
        attendance_percentage = (attendance_count / total_students) * 100
        absence_percentage = 100 - attendance_percentage

        # Create a new Toplevel window for displaying the graph
        graph_window = Toplevel(root)
        graph_window.title("Attendance Statistics")

        # Create a Figure object from matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)

        # Subplot for attendance and absence
        ax = fig.add_subplot(111)
        ax.pie([attendance_percentage, absence_percentage], labels=['Attendance', 'Absence'], autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
        ax.set_title("Attendance vs Absence")

        # Create a Tkinter canvas to display the graph
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

















    # ===============================update function for mysql database=================
    def update_attendance_data(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.main_attendance_frame)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.main_attendance_frame)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.main_attendance_frame)
                conn.commit()
                self.fetch_attendance_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.main_attendance_frame)
    # =============================Delete Attendance form my sql============================
    def delete_attendance_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_attendance_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

#================== delete funtion 
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Test@123", database="face_recognizer"
                    )
                    mycursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_ID=%s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                    
                    # Delete images from the folder
                    folder_path = "data"  # Replace with the actual path to the folder
                    file_prefix = f"user.{self.var_std_id.get()}."
                    file_extension = ".jpg"
                    for filename in os.listdir(folder_path):
                        if filename.startswith(file_prefix) and filename.endswith(file_extension):
                            os.remove(os.path.join(folder_path, filename))
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



#===============================================================================
    def fetch_attendance_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
        mycursor = conn.cursor()

        mycursor.execute("select * from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============================================================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
        my_cursor =conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END , values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_attendance_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #============export csv================        
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    


    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.main_attendance_frame)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_attendance_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.main_attendance_frame)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.main_attendance_frame)



   
    #=============attendance============
    def mark_attendance(self, i, r, n, status):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):

                if status == "Present":
                    f.writelines(f"\n{i},{r},{n},{dtString},{d1},{status}")
                    self.present_students.append(i)
                elif status == "Absent":
                    f.writelines(f"\n{i},{r},{n},{dtString},{d1},{status}")
                    self.absent_students.append(i)





    def check_absentees(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Student_id, Roll, Name FROM student")
        student_data = my_cursor.fetchall()
        conn.close()

        absentees = list(set(student_data) - set(self.present_students))
        print("---------------------------")
        print(absentees)
        print("---------------------------")
        for sid in absentees:
            student_id = sid[0]
            roll_number = sid[1]
            name = sid[2]
            self.mark_attendance(student_id, roll_number, name, "Absent")
#================== Face recognition =====================

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 90), cv2.FONT_ITALIC, 0.9, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 65), cv2.FONT_ITALIC, 0.9, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 40), cv2.FONT_ITALIC, 0.9, (255, 255, 255), 2)
                    self.mark_attendance(i, r, n, "Present")
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_ITALIC, 0.9, (255, 255, 255), 2)
                    self.mark_attendance(i, r, n,  "Absent")

                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        self.check_absentees()
    
    
    


    
    def train_classifier(self):
            data_dir=("data" )
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            faces=[] 
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') #Gray scale image 
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            #============= Train the Classifier And save ========
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed !") 
                
        


#============================================ get cursor ================

    def get_studentdetails_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        # print(data)
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


        #=========== update function ===========


    def update_data(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Are you sure you want to Update this student details",parent=self.root)

                if Update>0:

                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                    my_cursor =conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        



#========================= Reset funtion

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#======= Generate data set or Take photo Samples =========

    def generate_dataset(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                                                    self.var_dep.get(),
                                                    self.var_course.get(),

                                                    self.var_year.get(),
                                                    self.var_semester.get(),

                                                    self.var_std_name.get(),

                                                    self.var_div.get(),

                                                    self.var_roll.get(),

                                                    self.var_gender.get(),

                                                    self.var_dob.get(),

                                                    self.var_email.get(),

                                                    self.var_phone.get(),

                                                    self.var_address.get(),

                                                    self.var_teacher.get(),
                                                    self.var_radio1.get(),

                                                    self.var_std_id.get()==id+1



                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ======== load predifiend data on face frontals from opencv =========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbour = 5
                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def IExit(self):
                self.home_indicate.config(bg="#c3c3c3")
                self.menu_indicate.config(bg="#c3c3c3")
                self.contact_indicate.config(bg="#c3c3c3")
                self.exit_btn_indicate.config(bg="#c3c3c3")

                self.IExit=tkinter.messagebox.askyesno("Face Recognitin","Are you sure you want to close the app!",parent=self.root)
                if  self.IExit >0:
                    self.root.destroy()
                else:
                    return  

    

        
if __name__== "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()