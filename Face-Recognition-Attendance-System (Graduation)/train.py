from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("camera.ico")
        
        width = int(root.winfo_screenwidth()/3)
        height = int(root.winfo_screenheight()/5)


        title_lbl= Label(self.root,text="Train Data Sets ",font =("times new roman",30,"bold"),bg="white",fg="#e84393")
        title_lbl.place(x=0,y=0,width=root.winfo_screenwidth(),height=root.winfo_screenheight()/20)


        img_top=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\large3.jpg")
        img_top=img_top.resize((root.winfo_screenwidth(),int(root.winfo_screenheight()/2)),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lb1=Label(self.root,image=self.photoimg_top,bg="#DDFFFD")
        f_lb1.place(x=0,y=root.winfo_screenheight()/20,width=root.winfo_screenwidth(),height=int(root.winfo_screenheight()/2))

        #button 

        b1_label=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",activebackground="cyan",border=0)
        b1_label.place(x=0,y=int(root.winfo_screenheight()/2),width=root.winfo_screenwidth() ,height=60)

        img_bottom=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\large2.jpg")
        img_bottom=img_bottom.resize((root.winfo_screenwidth(),int(root.winfo_screenheight()/2)),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lb1=Label(self.root,image=self.photoimg_bottom,bg="#DDFFFD")
        f_lb1.place(x=0,y=int((root.winfo_screenheight()/2+60)),width=root.winfo_screenwidth(),height=int(root.winfo_screenheight()/2))




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










if __name__== "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()