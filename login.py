from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):

        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800")

        img=Image.open(r"college_images\login_bg.png")
        img=img.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"college_images\loginIcon.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",28,"bold"),fg="white",bg="black")
        get_str.place(x=85,y=100)

        # lablel
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # =========Icon Image===========
        img2=Image.open(r"college_images\loginIcon.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"college_images\lock.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)


        # login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # forget button
        forgotbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="paras" and self.txtpass.get()=="mahajan":
            messagebox.showinfo("Success","Welcome to Our Attendance system made by Paras Mahajan")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="$pPmM7512",database="face_recognizer")
            my_cur=conn.cursor()
            my_cur.execute("select * from register where email=%s and password=%s",(
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get()
                                                                                    ))

            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()



    # ==================reset password function=========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="$pPmM7512",database="face_recognizer")
            my_cur=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login new password",parent=self.root2)
                self.root2.destroy()




    # ===============forgot password function==========
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="$pPmM7512",database="face_recognizer")
            my_cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=110,y=290,width=125)














class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900")


        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ============bg image============
        bg_img=Image.open(r"college_images\login_bg.png")
        bg_img=bg_img.resize((1600,900),Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)

        bg_lbl=Label(self.root,image=self.photoimg_bg)
        bg_lbl.place(x=0,y=0,width=1600,height=900)

        
        # ===========left image===============
        img_left=Image.open(r"college_images\register-now.jpg")
        img_left=img_left.resize((470,550),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=50,y=100,width=470,height=550)

        # ================main frame=================
        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ================label and entry====================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #--------------row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # ----------row 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # ----------row 4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ============check button==============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # ==========buttons=============
        img=Image.open(r"college_images\register_icon.png")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=450,width=200)


        img1=Image.open(r"college_images\login1.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=370,y=450,width=200)



    # ==========function declaration==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required!")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="$pPmM7512",database="face_recognizer")
            my_cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try another email")
            else:
                my_cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get(),
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()





if __name__=="__main__":
    main()