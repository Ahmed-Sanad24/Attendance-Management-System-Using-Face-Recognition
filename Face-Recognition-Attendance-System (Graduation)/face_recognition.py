from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recgonition:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("camera.ico")
        
        left_img_width = root.winfo_screenwidth() - (root.winfo_screenwidth()/4)
        left_img_height = root.winfo_screenheight() - (root.winfo_screenheight()/4)


        # title_lbl= Label(self.root,text="Face Recognition ",font =("times new roman",40,"bold"),bg="#AEB5BF",fg="#00008B")
        # title_lbl.place(x=0,y=0,width=root.winfo_screenwidth(),height=root.winfo_screenheight()/15)

        #left image
        img_left=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\bg2.jpg")
        img_left=img_left.resize((int(left_img_width),int(left_img_height)),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lb1=Label(self.root,image=self.photoimg_left,bg="#242A36")
        f_lb1.place(x=0,y=root.winfo_screenheight()/15,width=int(left_img_width),height=int(left_img_height))



        






        #right image
        img_right=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\scan2.jpg")
        img_right=img_right.resize((int(root.winfo_screenwidth()/4),int(left_img_height)),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lb1=Label(self.root,image=self.photoimg_right,bg="#DDFFFD")
        f_lb1.place(x=left_img_width,y=root.winfo_screenheight()/15,width=int(root.winfo_screenwidth()/4),height=int(left_img_height))

         #button 

        b1_label=Button(self.root,text="Face Recognition",cursor="hand2",font =("times new roman",30,"bold"),bg="#AEB5BF",fg="#242A36",activebackground="#242A36",activeforeground="#AEB5BF",border=3 , command=self.face_recognition)
        b1_label.place(x=int(left_img_width/2),y=int(left_img_width/2),width=int(left_img_width/1.8) ,height=60)

#=============attendance============
    def mark_attendance(self,i,r,n,d):
        with open("omar.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


#================== Face recognition =====================

    def face_recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNighbors)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor =conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                separator="my_id"
                

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                

                if confidence> 77:
                    cv2.putText(img,f"ID:{i}",(x,y-90),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-65),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-15),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_ITALIC,0.9,(255,255,255),2)

                coord=[x,y,w,y]
            return coord
        


            
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img 
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img= video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release() 
        cv2.destroyAllWindows()





if __name__== "__main__":
    root=Tk()
    obj = Face_Recgonition(root)
    root.mainloop()