from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("camera.ico")
        

        width = int(root.winfo_screenwidth()/3)

        height = int(root.winfo_screenheight()/5)





        #============================ Variables ================

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



     



        #First image

        img=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\1.jpg")
        img=img.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=width,height=height)

        #Second image

        img1=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\3.jpg")
        img1=img1.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=width,y=0,width=width,height=height)

        #Third image

        img2=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
        img2=img2.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=width*2,y=0,width=width,height=height)

         #Background image

        img3=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\5.jpg")
        img3=img3.resize((root.winfo_screenwidth(),root.winfo_screenheight()-height),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3,padx=10,pady=10)
        bg_img.place(x=0,y=int(width/3),width=root.winfo_screenwidth(),height=root.winfo_screenheight()-height)


        bg_img.columnconfigure(0,weight=1)
        bg_img.columnconfigure(1,weight=1)

        bg_img.rowconfigure(0,weight=1)
        bg_img.rowconfigure(1,weight=99)



        title_lbl= Label(bg_img,text="STUDENT MANEGEMENT SYSTEM",font =("times new roman",30,"bold"),bg="white",fg="#00008B")
        title_lbl.grid(row=0,column=0,columnspan=2,sticky='WENS')
        font1=('Times',14,'normal')
        

        #================= LEFT FRAME =====================

        right_frame=LabelFrame(bg_img, bd=4,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        right_frame.grid(row=1,column=0,sticky='WENS',padx=5,pady=5)
        
        # right_frame.rowconfigure(0,weight=1)
        # right_frame.rowconfigure(1,weight=3)
        # right_frame.rowconfigure(2,weight=3)


        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)

        img_left=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
        
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(right_frame,image=self.photoimg_left,bg="#DDFFFD")
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

        current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


        # Department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select department","Computer","IT","Civil","Medical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")

        # Course
        dep_label=Label(current_course_frame,text="Course:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select course","Data structure","Computer networks","Embedded system","Computer vision")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=4,pady=10,sticky="W")

        # Year
        dep_label=Label(current_course_frame,text="Year:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2022-2023","2023-2024","2024-2025","2025-2026")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=4,pady=10)

        # Semester
        dep_label=Label(current_course_frame,text="Semester:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","2022-2023","2023-2024","2024-2025","2025-2026")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=4,pady=10,sticky="W")

        #=========================== Class Student information=============================

        class_student_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        class_student_frame.grid(row=2,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)



        #student ID
        student_frame=Label(class_student_frame,text="StudentID:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=0,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky="W")

        #student name
        student_frame=Label(class_student_frame,text="Student name:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=0,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=0,column=3,padx=10,pady=5,sticky="W")


        #Roll number
        student_frame=Label(class_student_frame,text="Roll number:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=1,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=1,column=1,padx=10,pady=5,sticky="W")


        #Gender
        student_frame=Label(class_student_frame,text="Gender:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=1,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=4,pady=10)


        #Email
        student_frame=Label(class_student_frame,text="Email:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=2,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=2,column=1,padx=10,pady=5,sticky="W")

        #Phone number
        student_frame=Label(class_student_frame,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=2,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=2,column=3,padx=10,pady=5,sticky="W")


        #Adress
        student_frame=Label(class_student_frame,text="Adress:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=3,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")


        #Date of birth
        student_frame=Label(class_student_frame,text="Date of birth:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=3,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=3,column=3,padx=10,pady=5,sticky="W")


        #Class division
        student_frame=Label(class_student_frame,text="Class division:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=4,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=4,column=3,padx=10,pady=5,sticky="W")
        Div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",14,"bold"),width=18,state="readonly")
        Div_combo["values"]=("Select div","A","B","C","D")
        Div_combo.current(0)
        Div_combo.grid(row=4,column=3,padx=4,pady=10)


        #Teacher
        student_frame=Label(class_student_frame,text="Teacher:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=4,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=4,column=1,padx=10,pady=5,sticky="W")


#===================================== Radio buttons ======================================
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0)

        # self.var_radio2 = StringVar()

        Radiobutton2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        Radiobutton2.grid(row=5,column=1)

#=====================================  buttons frame ======================================

        # buttons_frame = Frame(class_student_frame,bd=2 , relief= RIDGE)
        # buttons_frame.grid(row=6 , column=0)

        buttons_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B" )
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























        # #================= RIGHT FRAME =====================


        # right_frame=LabelFrame(bg_img, bd=4,font=("times new roman",14,"bold"),text="hehe frame",bg='white',pady=10 ,padx=10,relief=RIDGE,fg="#00008B")
        # right_frame.grid(row=1,column=1,sticky='WENS',padx=5,pady=5) 
        # right_frame.rowconfigure(0,weight=1)
        # right_frame.rowconfigure(1,weight=6)
        # right_frame.rowconfigure(2,weight=6)

        # right_frame.rowconfigure(3,weight=6)


        # right_frame.columnconfigure(0,weight=1)
        # right_frame.columnconfigure(1,weight=1)
        
        # img_right=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
        
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lb1=Label(right_frame,image=self.photoimg_right,bg="#D2FFFD")
        # f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

        
        

        # #========================== Search system ============

        # search_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Search system",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        # search_frame.grid(row=1,column=0,columnspan=2,sticky='WEN',padx=5,pady=5)

        # search_label=Label(search_frame,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
        # search_label.grid(row=0,column=0,padx=10,sticky="W")

        






        # test=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Search system",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        # test.grid(row=2,column=0,columnspan=2,sticky='WEN',padx=5,pady=5)

        # search_label=Label(test,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
        # search_label.grid(row=0,column=0,padx=10,sticky="W")


        # test1=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Search system",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        # test1.grid(row=3,column=0,columnspan=2,sticky='WEN',padx=5,pady=5)

        # search_label=Label(test1,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
        # search_label.grid(row=0,column=0,padx=10,sticky="W")













 #================= RIGHT FRAME =====================

        right_frame=LabelFrame(bg_img, bd=4,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        right_frame.grid(row=1,column=1,sticky='WENS',padx=5,pady=5)
        
        # right_frame.rowconfigure(0,weight=1)
        # right_frame.rowconfigure(1,weight=3)
        # right_frame.rowconfigure(2,weight=3)


        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)

        img_right=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
        
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(right_frame,image=self.photoimg_right,bg="#DDFFFD")
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

        current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


        # Department
        dep_label=Label(current_course_frame,text="Search by:",font=("times new roman",14,"bold"),bg="red")
        dep_label.grid(row=0,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select","Roll number","Phone number")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")

        search_entnry = ttk.Entry(current_course_frame,width=30,font=("times new roman",14,"bold"))
        search_entnry.grid(row=0,column=2,padx=10)

        save_button = Button(current_course_frame,text="Search",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        save_button.grid(row=0,column=3,sticky="WENS",pady=0 ,padx=2 ,ipady=0 , ipadx=10)

        showall_button = Button(current_course_frame,text="Show all",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        showall_button.grid(row=0,column=4,sticky="WENS",pady=0,padx=2 ,ipady=0 ,ipadx=10)






#=================================== TABLE FRAME ==============================


    
        



        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=300,width=960,height=350)

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
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
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



#============================================ get cursor ================

    def get_cursor(self,event=""):
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

        

#================== delete funtion 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                    my_cursor =conn.cursor()
                    sql="delete from student where Student_id= %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details deleted successfully",parent=self.root)
                
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

        







if __name__== "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()