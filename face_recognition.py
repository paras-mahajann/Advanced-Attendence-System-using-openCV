import collections
import mysql.connector
import cv2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recognition System")

        # Background Image
        img_top = Image.open(r"college_images\face_detector.png")
        img_top = img_top.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_lbl = Label(self.root, image=self.photoimg_top)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

        # Title Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Transparent Frame for Subject Selection
        subject_frame = Frame(self.root, bg="white", padx=5)
        subject_frame.place(x=615, y=100, width=380, height=50)

        # Subject Label and ComboBox
        subject_label = Label(subject_frame, text="Select Subject", font=("times new roman", 20, "bold"), bg="white", fg="black")
        subject_label.grid(row=0, column=0, padx=5)

        self.subject = StringVar()
        self.subject_combo = ttk.Combobox(subject_frame, textvariable=self.subject, font=("times new roman", 15), state="readonly", width=15)
        self.subject_combo['values'] = ("select subject", "DS", "DBMS", "DE", "UHV", "CM")  # Add more subjects as needed
        self.subject_combo.grid(row=0, column=1, padx=5)
        self.subject_combo.current(0)  # Set default subject

        # Face Recognition Button
        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=665, y=620, width=200, height=40)

        self.marked_students_today = set()

    def mark_attendance(self, i, r, n, d, subject):
        today = datetime.now().strftime("%d/%m/%Y")  # Get today's date
        filename = f"Attendance_files/{subject}_attendance.csv"

        # Open the file to read and check attendance
        with open(filename, "a+", newline="\n") as f:
            f.seek(0)
            myDataList = f.readlines()

            # Create a set of (student_id, date, subject) tuples to track attendance
            attendance_today = set()
            for line in myDataList:
                data = line.strip().split(",")
                if len(data) > 5:  # Ensure the line has enough data
                    attendance_today.add((data[0], data[5], data[6]))  # (Student_ID, Date, Subject)
            
            # Check if the student has already been marked present for the selected subject today
            if (i, today, subject) in attendance_today or i in self.marked_students_today:
                print(f"Attendance already marked for Student {i} in {subject} on {today}")
                return  # Exit the function if attendance is already recorded

            # If attendance is not already marked, mark it
            dtString = datetime.now().strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},{today},{subject},Present")
            self.marked_students_today.add(i)  # Add student to the marked list
            print(f"Attendance marked for Student {i} in {subject} on {today}")


    def face_recog(self):
        selected_subject = self.subject.get()
        if selected_subject == "select subject":
            messagebox.showerror("Selection Error", "Please select a valid subject", parent=self.root)
            return 

        prediction_buffer = collections.deque(maxlen=5)

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                # Predict the face
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Add prediction to buffer
                prediction_buffer.append((id, confidence))

                stable_id = None
                if sum(1 for _, conf in prediction_buffer if conf > 77) > (len(prediction_buffer) // 2):
                    stable_id = id

                if stable_id is not None:
                    conn = None  # Initialize conn to None
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="$pPmM7512",
                            database="face_recognizer"
                        )
                        cursor = conn.cursor()

                        cursor.execute("SELECT Student_Id, Name, Roll, Department FROM student WHERE Student_Id=%s", (stable_id,))
                        result = cursor.fetchone()

                        if result:
                            i, n, r, d = result
                            cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            self.mark_attendance(i, r, n, d, selected_subject)
                    except mysql.connector.Error as err:
                        print(f"Database error: {err}")
                    finally:
                        if conn is not None and conn.is_connected():
                            cursor.close()
                            conn.close()
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

            return img


        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        
        try:
            clf.read("classifier.xml")
        except Exception as e:
            print("Error loading model:", e)
            return

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = draw_boundary(img,faceCascade,1.3,5,(0,255,0),"Face",clf)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
