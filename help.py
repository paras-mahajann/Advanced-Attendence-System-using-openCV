from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        img=Image.open(r"college_images\help_desk_bg.png")
        img=img.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        help_label=Label(f_lbl,text="Email:mahajanparas912@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label.place(x=530,y=170)





if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
            