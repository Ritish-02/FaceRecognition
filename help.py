from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Smart Attendance System - Help Desk")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background image
        img_top = Image.open(r"college_images\lap.jpeg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Project description
        project_desc = """Welcome to the Face Recognition Smart Attendance System!

This system automates student attendance using real-time face detection and recognition technology.
It ensures accuracy, prevents proxy attendance, and reduces manual effort.

Key Features:
- Real-time face recognition to mark attendance automatically
- User-friendly interface for both students and instructors
- Secure and reliable attendance logging

How to Use:
1. Ensure the webcam is connected and working.
2. Run the attendance system.
3. Students should face the camera when prompted.
4. Attendance will be marked automatically and recorded.

Common Issues:
- Ensure proper lighting for accurate face detection.
- Make sure your face is clearly visible to the camera.
- If attendance is not marked, please notify the administrator.

For further assistance, please contact:

Ritish Raj
Email: rajritish6@gmail.com"""

        # Display the text in a Label or Text widget
        help_label = Label(f_lbl, text=project_desc, font=("times new roman", 16), bg="white", justify=LEFT)
        help_label.place(x=50, y=50, width=900, height=600)

        # Contact info at the bottom right
        contact_label = Label(f_lbl, text="Contact: rajritish6@gmail.com", font=("times new roman", 18, "bold"), bg="white", fg="blue")
        contact_label.place(x=1150, y=650)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
