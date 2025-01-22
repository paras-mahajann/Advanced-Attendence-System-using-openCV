from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        # ==========variables=========
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        # first image

        img=Image.open(r"college_images\college_image.jpg")
        img=img.resize((1920,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=130)


        # #second image

        # img1=Image.open(r"college_images\Train_Data.png")
        # img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)


        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=650,y=0,width=300,height=130)

        # #third image

        # img2=Image.open(r"college_images\Train_Data.png")
        # img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)


        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=600,height=130)


        #bg image

        img3=Image.open(r"college_images\bg_image.png")
        img3=img3.resize((1920,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1536,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("neuropolitical",35,""),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=58,width=1500,height=595)


        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("neuropolitical",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"college_images\Train_Data.png")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)



        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("neuropolitical",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=125)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("neuropolitical",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("neuropolitical",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","computer","AIML","Data Science","Electrical","ENTC","civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=1)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("neuropolitical",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("neuropolitical",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year",font=("neuropolitical",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("neuropolitical",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("neuropolitical",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("neuropolitical",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        

        # Class student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("neuropolitical",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("neuropolitical",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("neuropolitical",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Division:",font=("neuropolitical",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("neuropolitical",13,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("neuropolitical",13,"bold"),width=18,state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Roll No
        roll_n0_label=Label(class_student_frame,text="Roll No:",font=("neuropolitical",13,"bold"),bg="white")
        roll_n0_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("neuropolitical",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("neuropolitical",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("neuropolitical",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Email
        email_label=Label(class_student_frame,text="Email:",font=("neuropolitical",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("neuropolitical",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phone_no_label=Label(class_student_frame,text="Phone no:",font=("neuropolitical",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("neuropolitical",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("neuropolitical",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("neuropolitical",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #  Teacher name
        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("neuropolitical",13,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("neuropolitical",13,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Student Name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("neuropolitical",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("neuropolitical",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("neuropolitical",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("neuropolitical",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1)
   
        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="Update",command=self.update_data,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="Delete",command=self.delete_data,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,width=35,text="Take photo Sample",font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,width=35,text="Update Photo Sample",font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        # Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("neuropolitical",12,"bold"))
        Right_frame.place(x=755,y=10,width=720,height=580)

        img_right=Image.open(r"college_images\student.png")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # ==========Search System=========
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("neuropolitical",12,"bold"))
        search_frame.place(x=5,y=135,width=708,height=70)

        search_label=Label(search_frame,text="Search By:",font=("neuropolitical",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("neuropolitical",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","StudentID","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("neuropolitical",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(search_frame,width=12,text="Search",font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(search_frame,width=12,text="Reset",font=("neuropolitical",13,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)

        # def search_function():
        #     search_by = search_combo.get()
        #     search_value = search_entry.get()
        #     # Add logic for searching based on selected option and entered value
        #     print(f"Searching by {search_by} for {search_value}")

        # def reset_function():
        #     search_combo.current(0)
        #     search_entry.delete(0, END)
            # Add logic to refresh or reset the search results

        # search_btn.config(command=search_function)
        # ShowAll_btn.config(command=reset_function)


        # ========table frame=========
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=708,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("department","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ================function declairation================
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='$pPmM7512',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_department.get(), 
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
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    

    # ===========fetch data==========
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='$pPmM7512',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ==========get cursor=======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0])
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


    # update function
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Confirm if the user wants to update
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    # Validate student ID
                    try:
                        student_id = int(self.var_std_id.get())
                    except ValueError:
                        messagebox.showerror("Error", "Invalid Student ID. Please enter a valid numeric ID.", parent=self.root)
                        return

                    # Connect to the database
                    conn = mysql.connector.connect(host='localhost', username='root', password='$pPmM7512', database='face_recognizer')
                    my_cursor = conn.cursor()

                    # Execute the update query
                    my_cursor.execute("""
                        UPDATE student 
                        SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, 
                            Gender=%s, DOB=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_Id=%s
                        """, (
                            self.var_department.get(),
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
                            student_id
                        ))

                    # Check if the update affected any rows
                    if my_cursor.rowcount == 0:
                        messagebox.showerror("Error", "No matching student found to update.", parent=self.root)
                    else:
                        messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                        conn.commit()  # Commit changes to the database

                    self.fetch_data()  # Refresh data from the database
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
            finally:
                # Ensure the connection is always closed
                if conn.is_connected():
                    conn.close()

    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='$pPmM7512',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # reset
    def reset_data(self):
        self.var_department.set("Select Department")
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



    # ==========Generate data set or Take photo samples============
    def generate_dataset(self):
        if self.var_department.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Capture student ID to ensure it's used in image saving
                student_id = self.var_std_id.get()
                
                # Database connection
                conn = mysql.connector.connect(host='localhost', username='root', password='$pPmM7512', database='face_recognizer')
                my_cursor = conn.cursor()
                
                # Update student information
                my_cursor.execute("""
                    UPDATE student 
                    SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, 
                        Gender=%s, DOB=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                    WHERE Student_Id=%s
                    """, (
                        self.var_department.get(),
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
                        student_id  # Use student_id captured from var_std_id
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            finally:
                my_cursor.close()
                conn.close()
            
            try:
                # Load face detection data
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    return [img[y:y+h, x:x+w] for (x, y, w, h) in faces]

                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Failed to access the webcam.", parent=self.root)
                    return

                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break

                    faces = face_cropped(my_frame)
                    if faces:
                        for face in faces:
                            img_id += 1
                            face_resized = cv2.resize(face, (450, 450))
                            face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"  # Use student_id in filename
                            cv2.imwrite(file_name_path, face_gray)
                            cv2.putText(face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face_resized)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Exit on 'Enter' or after 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating datasets completed", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()