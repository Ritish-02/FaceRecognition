from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open(r"college_images\fce.jpeg")
        img1 = img1.resize((1530, 750), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_lbl = Label(self.root, image=self.photoimg1)
        bg_lbl.place(x=0, y=0, width=1530, height=750)

        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=120, width=1550, height=45)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=200, width=340, height=430)

        self.txtUser = StringVar()
        self.txtPass = StringVar()

        username = Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="black")
        username.place(x=70, y=125)

        txtUser = ttk.Entry(frame, textvariable=self.txtUser, font=("times new roman", 12, "bold"))
        txtUser.place(x=40, y=150, width=270)

        password = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        password.place(x=70, y=195)

        txtPass = ttk.Entry(frame, textvariable=self.txtPass, font=("times new roman", 12, "bold"), show="*")
        txtPass.place(x=40, y=220, width=270)

        btn_login = Button(frame, text="Login", borderwidth=3, relief=RAISED, command=self.login,
                           cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn_login.place(x=110, y=270, width=120, height=35)

        btn_register = Button(frame, text="New User Registration", command=self.reg_window,
                              cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn_register.place(x=15, y=320, width=200)

        btn_forget = Button(frame, text="Forgot Password", command=self.forgot_password,
                            cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn_forget.place(x=10, y=360, width=200)

    def reg_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtUser.get() == "" or self.txtPass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="020703", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s",(self.txtUser.get(), self.txtPass.get()))
                row = my_cursor.fetchone()
                conn.close()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password")
                else:
                    messagebox.showinfo("Success", "Login Successful!")

                    # Open the Main Window
                    self.root.destroy()  # Close the login window
                    self.new_window = Tk()
                    self.app = Face_Recognition(self.new_window)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

    def forgot_password(self):
        if self.txtUser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="020703", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.txtUser.get(),))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter a valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"))
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"))
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 13, "bold"), state="readonly", width=20)
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your First School")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50, y=110)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"))
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"))
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, cursor="hand2",
                             font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                btn.place(x=120, y=290, width=100)




class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_cnfpass = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"college_images\bg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=100, width=800, height=550)

        title = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        title.place(x=20, y=20)

        # Labels and Entry Fields
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=110, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=400, y=80)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        lname_entry.place(x=400, y=110, width=250)

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=160)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        contact_entry.place(x=50, y=190, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=400, y=160)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        email_entry.place(x=400, y=190, width=250)

        securityQ = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white")
        securityQ.place(x=50, y=240)
        self.combo_securityQ = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 13, "bold"), state="readonly")
        self.combo_securityQ["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your First School")
        self.combo_securityQ.current(0)
        self.combo_securityQ.place(x=50, y=270, width=250)

        securityA = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        securityA.place(x=400, y=240)
        securityA_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        securityA_entry.place(x=400, y=270, width=250)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=320)
        password_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        password_entry.place(x=50, y=350, width=250)

        cnfpassword = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        cnfpassword.place(x=400, y=320)
        cnfpassword_entry = ttk.Entry(frame, textvariable=self.var_cnfpass, font=("times new roman", 15), show="*")
        cnfpassword_entry.place(x=400, y=350, width=250)

        # Register Button
        btn_register = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="green", fg="white")
        btn_register.place(x=320, y=420, width=150)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_cnfpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="020703", database="face_recognition")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    query = "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    value = (self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(), self.var_pass.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully!")
                    self.root.destroy()  # Close register window after successful registration
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

if __name__ == "__main__":
    main()




        


        



