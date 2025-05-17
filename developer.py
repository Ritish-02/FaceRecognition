from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System - Developer Team")

        # Title
        title_lbl = Label(self.root, text="DEVELOPERS", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        bg_img = Image.open(r"college_images\dev.jpeg")
        bg_img = bg_img.resize((1530, 720), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photo_bg)
        bg_label.place(x=0, y=55, width=1530, height=720)

        # Frame
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=930, y=70, width=580, height=620)

        Label(main_frame, text="👨‍💻 Project Team", font=("times new roman", 20, "bold"), bg="white", fg="black").place(x=180, y=10)

        # Member 1
        Label(main_frame, text="Name: Ritish Raj", font=("times new roman", 14), bg="white").place(x=20, y=60)
        Label(main_frame, text="Role: Backend Developer", font=("times new roman", 13), bg="white").place(x=20, y=90)
        Label(main_frame, text="Email: rajritish6@gmail.com", font=("times new roman", 13), bg="white").place(x=20, y=115)
        Button(main_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/Ritish-02"), bg="black", fg="white", font=("times new roman", 11)).place(x=40, y=145)
        Button(main_frame, text="LinkedIn", command=lambda: webbrowser.open("https://www.linkedin.com/in/ritish-raj-0b6b99240"), bg="blue", fg="white", font=("times new roman", 11)).place(x=110, y=145)

        # Member 2
        Label(main_frame, text="Name: Sona Rani", font=("times new roman", 14), bg="white").place(x=20, y=190)
        Label(main_frame, text="Role: Frontend Developer", font=("times new roman", 13), bg="white").place(x=20, y=220)
        Label(main_frame, text="Email: sonrich066@gmail.com", font=("times new roman", 13), bg="white").place(x=20, y=245)
        Button(main_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/ayesha456"), bg="black", fg="white", font=("times new roman", 11)).place(x=40, y=275)
        Button(main_frame, text="LinkedIn", command=lambda: webbrowser.open("https://linkedin.com/in/ayesha456"), bg="blue", fg="white", font=("times new roman", 11)).place(x=110, y=275)

        # Project Summary
        Label(main_frame, text="📌 Project Overview", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=20, y=320)

        overview = Text(main_frame, width=66, height=5, font=("times new roman", 12), wrap=WORD)
        overview.place(x=20, y=350)
        overview.insert(END, "This project is a smart attendance system using AI-powered face recognition. It uses real-time face detection, MySQL for record-keeping, and GPS/IP-based verification to ensure secure and accurate attendance marking.")
        overview.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
