# FaceRecognition
#  Face Recognition Smart Attendance System

This is a Python-based intelligent attendance management system that uses **AI-powered face recognition** and **location verification (IP/GPS)** to ensure secure and tamper-proof student attendance. Built using `OpenCV`, `Tkinter`, `MySQL`, and `Geopy`, this system automates attendance processes and reduces human error and proxy attendance.

---

##  Features

-  **Real-time face recognition** using OpenCV and Haarcascade + LBPH
-  **Location verification** using IP-based geolocation (GPS optional)
-  GUI built using `Tkinter` with multiple navigation modules
-  Automatically logs attendance into CSV files and/or MySQL
-  Generates attendance reports
-  Developer & help sections for usability and documentation
-  Photo dataset folder for student face images
-  Prevents proxy attendance
-  Easy to use, clean interface

---

##  Technologies Used

| Layer         | Tools / Libraries                    |
|---------------|--------------------------------------|
| Frontend (GUI)| Tkinter, PIL                         |
| Backend       | Python, OpenCV, NumPy, CSV           |
| ML Algorithm  | LBPH (Local Binary Pattern Histogram)|
| Face Detection| Haarcascade Classifier               |
| Location      | Geopy, Geocoder                      |
| Database      | MySQL (can be replaced with SQLite)  |

---

##  Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
