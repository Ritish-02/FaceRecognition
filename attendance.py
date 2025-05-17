from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition")

        #Variables 
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()



        #first image
        img = Image.open(r"college_images\att1.jpeg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1 = Image.open(r"college_images\att2.jpeg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg image
        img3 = Image.open(r"college_images\bg_image.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg = "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame = LabelFrame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #Left Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        img_left = Image.open(r"college_images\att.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #Labels and entry

        #Attendance ID
        attendance_id_label = Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label = Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)
        atten_roll_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        atten_roll_entry.grid(row=0,column=3,pady=8,sticky=W)

        #Name
        nameLabel = Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        depLabel = Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        timeLabel = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        dateLabel = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance
        attendanceLabel = Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",13,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.atten_status = ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #Button frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        import_btn = Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export CSV",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,text="Update",command=self.update_attendance,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #Right Frame
        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        img_right = Image.open(r"college_images\s1.jpeg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #Scroll Bar & Table
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance ")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #Function
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],parent=self.root)
        if not fln:  
            return
        try:
            with open(fln, newline="") as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                mydata.clear() 
                for row in csvread:
                    mydata.append(row)
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file.\n{str(e)}")

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Erorr",f"Due To: {str(es)}",parent=self.root)
    
    #Getcursor
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    def update_attendance(self):
        if self.var_atten_id.get() == "" or self.var_atten_roll.get() == "" or self.var_atten_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return  # Stop function execution if validation fails

        try:
            Update = messagebox.askyesno("Update", "Do you want to update this attendance record?", parent=self.root)
            if not Update:
                return  # Exit if user selects 'No'

            file_path = "attendance_report/present.csv"
            updated_data = []
            record_found = False

            # Read existing data
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                header = next(reader)  # Read the header
                updated_data.append(header)  # Keep header unchanged

                for row in reader:
                    if row[0] == self.var_atten_id.get():  # Match Attendance_ID (first column)
                        updated_data.append([
                            self.var_atten_id.get(),
                            self.var_atten_roll.get(),
                            self.var_atten_name.get(),
                            self.var_atten_dep.get(),
                            self.var_atten_time.get(),
                            self.var_atten_date.get(),
                            self.var_atten_attendance.get()
                        ])
                        record_found = True
                    else:
                        updated_data.append(row)  # Keep other records unchanged

            if not record_found:
                messagebox.showerror("Error", "Attendance record not found", parent=self.root)
                return

            # Write updated data back to the CSV
            with open("attendance_report/present.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)

            messagebox.showinfo("Success", "Attendance record successfully updated", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
