from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System - Developer Info")

        # Title Label
        title_lbl = Label(self.root, text="DEVELOPER PAGE", font=("Helvetica", 35, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1535, height=50)

        # Background Image
        bg_img = Image.open(r"college_images\dev_bg.jpg")  # Use a background image relevant to development
        bg_img = bg_img.resize((1535, 1030), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.bg_photo)
        bg_lbl.place(x=0, y=50, width=1535, height=1030)

        # Frame for Developer Info
        dev_frame = Frame(self.root, bd=5, bg="white", relief=RIDGE)
        dev_frame.place(x=835, y=75, width=670, height=700)

        # Profile Picture
        profile_img = Image.open(r"college_images\photo (1).png")  # Use an image for developer profile
        profile_img = profile_img.resize((150, 150), Image.Resampling.LANCZOS)
        self.profile_photo = ImageTk.PhotoImage(profile_img)
        profile_img_lbl = Label(dev_frame, image=self.profile_photo, bg="white")
        profile_img_lbl.place(x=235, y=10, width=150, height=150)

        # Developer Name
        dev_name_lbl = Label(dev_frame, text="Paras", font=("Helvetica", 25, "bold"), bg="white", fg="dark blue")
        dev_name_lbl.place(x=260, y=170)

        # Role
        dev_role_lbl = Label(dev_frame, text="Full Stack Developer", font=("Helvetica", 18, "italic"), bg="white", fg="black")
        dev_role_lbl.place(x=190, y=210)

        # About Me Section
        about_lbl = Label(dev_frame, text="About Me", font=("Helvetica", 20, "bold", "underline"), bg="white", fg="dark blue")
        about_lbl.place(x=240, y=260)

        about_text = Text(dev_frame, font=("Helvetica", 14), bg="light yellow", wrap=WORD, height=4, width=50)
        about_text.insert(END, "Hello! I’m Paras, a dedicated Full Stack Developer passionate about technology and innovative solutions. I specialize in creating efficient applications with a focus on user experience and functionality.")
        about_text.config(state=DISABLED)
        about_text.place(x=55, y=300)

        # Skills Section
        skills_lbl = Label(dev_frame, text="Skills", font=("Helvetica", 20, "bold", "underline"), bg="white", fg="dark blue")
        skills_lbl.place(x=270, y=405)

        skills_text = Text(dev_frame, font=("Helvetica", 14), bg="light cyan", wrap=WORD, height=4, width=50)
        skills_text.insert(END, "• Proficient in Python, JavaScript, HTML, CSS\n• Experience with MySQL, Tkinter, and OpenCV\n• Skilled in Database Management and Frontend Design\n• Passionate about AI and Automation")
        skills_text.config(state=DISABLED)
        skills_text.place(x=55, y=444)

        # Contact Information
        contact_lbl = Label(dev_frame, text="Contact Information", font=("Helvetica", 20, "bold", "underline"), bg="white", fg="dark blue")
        contact_lbl.place(x=180, y=560)

        contact_text = Text(dev_frame, font=("Helvetica", 14), bg="light green", wrap=WORD, height=3, width=50)
        contact_text.insert(END, "Email: mahajanparas912@gmail.com\nLinkedIn: https://www.linkedin.com/in/paras-mahajan-developer/\nGitHub: https://github.com/paras-mahajann")
        contact_text.config(state=DISABLED)
        contact_text.place(x=55, y=600)

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
