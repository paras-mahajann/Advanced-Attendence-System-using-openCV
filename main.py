from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from chatbot import ChatBot



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("face Recognition System")

        # instance variables
        self.student_window = None
        self.train_window = None
        self.face_recognition_window = None
        self.attendance_window = None
        self.developer_window = None
        self.chatbot_window = None





        # first image

        img=Image.open(r"college_images\college_image.jpg")
        img=img.resize((1920,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=130)


        # second image

        # img1=Image.open(r"college_images\college_image.jpg")
        # img1=img1.resize((510,130),Image.Resampling.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)


        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=510,y=0,width=510,height=130)

        # #third image

        # img2=Image.open(r"college_images\college_image.jpg")
        # img2=img2.resize((510,130),Image.Resampling.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)


        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1020,y=0,width=520,height=130)

        # bg image

        img3=Image.open(r"college_images\bg_image.png")
        img3=img3.resize((1920,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1536,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("neuropolitical",35,""),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # ==========time==============4
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('neuropolitical',14),background='white',foreground='red')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button

        img4=Image.open(r"college_images\student.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2",bg="black")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)



        #Detect face button

        img5=Image.open(r"college_images\face_detector.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,bg="black")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)



        #Attendance
        img6=Image.open(r"college_images\Attendance.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,bg="black")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)


        #help Desk button

        # img7=Image.open(r"college_images\Help_desk.png")
        # img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        # self.photoimg7=ImageTk.PhotoImage(img7)


        # b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2",bg="black")
        # b1.place(x=1100,y=100,width=220,height=220)

        # b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("neuropolitical",15,"bold"),bg="white",fg="black")
        # b1_1.place(x=1100,y=300,width=220,height=40)

        # Chat button
        
        img_chat=Image.open(r"college_images\chatbot_main.png")
        img_chat=img_chat.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)


        bChat=Button(bg_img,image=self.photoimg_chat,command=self.chatbot,cursor="hand2",bg="black")
        bChat.place(x=1100,y=100,width=220,height=220)

        b1_Chat=Button(bg_img,text="ChatBot",command=self.chatbot,cursor="hand2",font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_Chat.place(x=1100,y=300,width=220,height=40)



        #Train  button

        img8=Image.open(r"college_images\Train_Data.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)


        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data,bg="black")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos button

        img9=Image.open(r"college_images\Photos.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)


        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,bg="black")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)



        #Developer  button

        img10=Image.open(r"college_images\Developer.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)


        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data,bg="black")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)



        #Exit  button

        img11=Image.open(r"college_images\exit.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)


        b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2",bg="black")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("neuropolitical",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


# ===============function buttons============
    def student_details(self):
        if self.student_window is None or not self.student_window.winfo_exists():
            self.student_window=Toplevel(self.root)
            self.app=Student(self.student_window)
        else:
            self.student_window.lift()

    def train_data(self):
        if self.train_window is None or not self.train_window.winfo_exists():
            self.train_window = Toplevel(self.root)
            self.app = Train(self.train_window)
        else:
            self.train_window.lift()
            

    def face_data(self):
        if self.face_recognition_window is None or not self.face_recognition_window.winfo_exists():
            self.face_recognition_window = Toplevel(self.root)
            self.app = Face_Recognition(self.face_recognition_window)
        else:
            self.face_recognition_window.lift()


    def attendance_data(self):
        if self.attendance_window is None or not self.attendance_window.winfo_exists():
            self.attendance_window = Toplevel(self.root)
            self.app = Attendance(self.attendance_window)
        else:
            self.attendance_window.lift()

    def developer_data(self):
        if self.developer_window is None or not self.developer_window.winfo_exists():
            self.developer_window = Toplevel(self.root)
            self.app = Developer(self.developer_window)
        else:
            self.developer_window.lift()
    # def help_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)

    def chatbot(self):
        if self.chatbot_window is None or not self.chatbot_window.winfo_exists():
            self.chatbot_window = Toplevel(self.root)
            self.app = ChatBot(self.chatbot_window)
        else:
            self.chatbot_window.lift()



if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
            