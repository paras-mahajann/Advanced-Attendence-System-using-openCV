from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename="training_log.log", level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

class Train:
    def __init__(self, root, on_close_callback=None):
        self.root = root
        self.on_close_callback = on_close_callback
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"college_images\Train_dataset.png").resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"college_images\people_img.png").resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' not found!", parent=self.root)
            return

        # Fetch image paths
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]
        if len(path) == 0:
            messagebox.showerror("Error", "No images found in the data directory.", parent=self.root)
            return

        faces = []
        ids = []
        skipped_images = []

        # Progress bar
        progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=600, mode='determinate')
        progress.place(x=465, y=450)
        progress["maximum"] = len(path)

        for i, image in enumerate(path):
            try:
                # Load image and convert to grayscale
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')

                # Extract student ID
                student_id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(student_id)

                # Display image for training
                cv2.imshow("Training on image", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                logging.error(f"Error processing image {image}: {e}")
                skipped_images.append(image)
                continue

            # Update progress bar
            progress["value"] = i + 1
            self.root.update_idletasks()

        # Training the classifier
        ids = np.array(ids)
        try:
            clf = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
            clf.train(faces, ids)
            clf.write("classifier.xml")

            cv2.destroyAllWindows()
            messagebox.showinfo("Result", f"Training completed! {len(ids)} images processed, {len(skipped_images)} images skipped.", parent=self.root)
            self.root.destroy()

            if skipped_images:
                logging.info(f"Skipped images: {skipped_images}")

        except Exception as e:
            cv2.destroyAllWindows()
            messagebox.showerror("Training Error", f"Training failed: {e}", parent=self.root)

        finally:
            progress.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
