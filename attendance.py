from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")


        # =======variables========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_subject = StringVar()


        # first image
        img=Image.open(r"college_images\college_image.jpg")
        img=img.resize((1920,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=130)


        img3=Image.open(r"college_images\bg_image.png")
        img3=img3.resize((1920,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1536,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("neuropolitical",35,""),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=58,width=1500,height=595)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("neuropolitical",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)

        img_left=Image.open(r"college_images\Train_Data.png")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=130,width=720,height=420)

        # Lables and entry
        # attendance id
        attendance_id_lable=Label(left_inside_frame,text="AttendanceID:",font=("times-new-roman",13,"bold"),bg="white")
        attendance_id_lable.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("neuropolitical",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        name_lable=Label(left_inside_frame,text="Name:",font=("times-new-roman",13,"bold"),bg="white")
        name_lable.grid(row=1,column=0,padx=10,sticky=W)

        atte_Name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("neuropolitical",13,"bold"))
        atte_Name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll
        Roll_lable=Label(left_inside_frame,text="Roll No:",font=("times-new-roman",13,"bold"),bg="white")
        Roll_lable.grid(row=0,column=2,padx=10,sticky=W)

        atte_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("neuropolitical",13,"bold"))
        atte_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # date
        date_lable=Label(left_inside_frame,text="Date:",font=("times-new-roman",13,"bold"),bg="white")
        date_lable.grid(row=2,column=2,padx=10,sticky=W)

        atte_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("neuropolitical",13,"bold"))
        atte_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # department
        att_dep_lable=Label(left_inside_frame,text="Department:",font=("times-new-roman",13,"bold"),bg="white")
        att_dep_lable.grid(row=1,column=2,padx=10,sticky=W)

        atte_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_department,font=("neuropolitical",13,"bold"))
        atte_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Time
        att_time_lable=Label(left_inside_frame,text="Time:",font=("times-new-roman",13,"bold"),bg="white")
        att_time_lable.grid(row=2,column=0,padx=10,sticky=W)

        atte_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("neuropolitical",13,"bold"))
        atte_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # attendance
        attendanceLable=Label(left_inside_frame,text="Attendance Status :",bg="white",font="comicsansns 11 bold")
        attendanceLable.grid(row=3,column=2)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=3,pady=8)
        self.atten_status.current(0)

        # Subject
        subject_label = Label(left_inside_frame, text="Subject:", font=("times-new-roman", 13, "bold"), bg="white")
        subject_label.grid(row=3, column=0, padx=10, sticky=W)

        atte_subject = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_subject, font=("neuropolitical", 13, "bold"))
        atte_subject.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=365,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="Export csv",command=self.exportCsv,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="Update",font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

    # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("neuropolitical",12,"bold"))
        Right_frame.place(x=755,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=705,height=455)

        # ========scroll bar table=========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","subject","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("subject", text="Subject")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("subject", width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ========fetch data===========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvRead=csv.reader(myfile,delimiter=",")
            for i in csvRead:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" succesfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    # show info in table
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_department.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_subject.set(rows[6])
            self.var_atten_attendance.set(rows[7])
            

        else:
            messagebox.showinfo("alert!","No data available in the selected row. ",parent=self.root)

    # ====reset data=====
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_subject.set("")
        self.var_atten_attendance.set("")
        


        


if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()