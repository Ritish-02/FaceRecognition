from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition")

        title_lbl = Label(self.root,text="TRAIN DATA SET ",font=("times new roman",35,"bold"),bg="white",fg = "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        

        img_top = Image.open(r"college_images\t.jpeg")
        img_top=img_top.resize((1530,325),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        #Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",50,"bold"),bg="darkblue",fg = "white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"college_images\u.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)
    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            filename = os.path.split(image)[1]  # Get filename
            try:
                id = int(filename.split('.')[1])  # Extract ID correctly
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                faces.append(imageNp)
                ids.append(id)
                print(f"Processed: {filename}, ID: {id}")  # Debugging print
            except Exception as e:
                print(f"Error processing {filename}: {e}")  # Catch errors

        if len(faces) == 0:
            print("No valid images found for training!")
            return

        ids = np.array(ids)

        # Train Classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Completed Successfully!")

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()