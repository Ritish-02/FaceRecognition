from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from datetime import datetime
import numpy as np
from geopy.distance import geodesic
import geocoder

# Set your institution's coordinates here
#COLLEGE_LOCATION = (25.572999, 85.166347) 
COLLEGE_LOCATION = (28.46071083651987, 77.49331470400942)

def get_student_location():
    try:
        location = geocoder.ip("me")
        if location.latlng:
            return tuple(location.latlng)
        else:
            print("❌ Could not fetch location.")
            return None
    except Exception as e:
        print(f"❌ Location Error: {e}")
        return None

def is_within_radius(student_location, radius=5000):
    if student_location:
        distance = geodesic(COLLEGE_LOCATION, student_location).meters
        print(f"📍 Your location: {student_location}")
        print(f"🎯 College location: {COLLEGE_LOCATION}")
        print(f"📏 Distance: {distance:.2f} meters")
        return distance <= radius
    return False

class Face_Recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_left = Image.open(r"college_images\face_reg.jpeg").resize((650, 700), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_right = Image.open(r"college_images\device.jpg").resize((950, 700), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="FACE RECOGNIZER", command=self.face_detect, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=335, y=640, width=300, height=40)

#Automatically Marks Attendance
    def mark_attendance(self, student_id, roll, name, department):
        student_location = get_student_location()

        if student_location and is_within_radius(student_location):
            file_path = "attendance_report/present.csv"

            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("ID,Roll,Name,Department,Time,Date,Status\n")

            with open(file_path, "r+", newline="\n") as f:
                myDataList = f.readlines()
                id_list = [line.split(",")[0] for line in myDataList]

                if student_id not in id_list:
                    now = datetime.now()
                    dtString = now.strftime("%H:%M:%S")
                    d1 = now.strftime("%d/%m/%Y")
                    f.write(f"{student_id},{roll},{name},{department},{dtString},{d1},Present\n")
                    print(f"✅ Attendance marked for {name}.")
                else:
                    print(f"⚠️ {name} already marked present.")
        else:
            messagebox.showwarning("Location Alert", "❌ You are outside the allowed location!")


    # Face Recognition
    def face_detect(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="020703", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_Id=%s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_Id=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_Id=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"
                if predict < 70:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(str(id), r, n, d)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier file not found. Train the model first!")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog(root)
    root.mainloop()
