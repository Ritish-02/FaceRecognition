# import requests
# from geopy.distance import geodesic
# from tkinter import messagebox
# CAMPUS_LOCATION = (28.4785615, 77.5178232624016)

# import requests
# from tkinter import messagebox

# API_KEY = "88458647e5944b39b4b85896708200a9"  
# CAMPUS_LOCATION = (28.4785615, 77.5178232624016)

# def get_student_location():
#     """Fetch student's location using OpenCage API with better error handling."""
#     try:
#         url = f"https://api.opencagedata.com/geocode/v1/json?q=YOUR_IP_ADDRESS&key={API_KEY}"
#         response = requests.get(url)
#         data = response.json()

#         if response.status_code != 200:
#             print(f"❌ API Error: {data}") 
#             messagebox.showerror("Error", f"API Error: {data['status']['message']}")
#             return None

#         if data["results"]:
#             lat = data["results"][0]["geometry"]["lat"]
#             lon = data["results"][0]["geometry"]["lng"]
#             print(f"📍 Student's Location: ({lat}, {lon})")  
#             return (lat, lon)
#         else:
#             print("❌ GPS Not Enabled or No Results Found")
#             messagebox.showerror("Error", "Could not fetch location. Ensure GPS is enabled.")
#             return None
#     except Exception as e:
#         print(f"❌ Location Fetch Error: {str(e)}")  
#         messagebox.showerror("Error", f"Location Error: {str(e)}")
#         return None

# def is_within_radius(student_location, radius=100):
#     """Check if student is within the allowed radius."""
#     if student_location:
#         distance = geodesic(CAMPUS_LOCATION, student_location).meters
#         print(f"📏 Distance to Campus: {distance} meters")  
        
#         if distance > radius:
#             print("⚠️ Student is outside the allowed location.")
#             return False  
#         return True
#     return False
from geopy.distance import geodesic
import geocoder
from tkinter import messagebox

# Set your college coordinates here
COLLEGE_LOCATION = (28.4785, 77.5178)  # Replace with your college latitude & longitude

def get_student_location():
    try:
        location = geocoder.ip("me")
        if location.latlng:
            return tuple(location.latlng)
        else:
            messagebox.showerror("Error", "❌ GPS not enabled or location unavailable.")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"❌ Location error: {str(e)}")
        return None

def is_within_radius(student_location, radius=100):
    """Returns True if student is within 'radius' meters of the campus."""
    if student_location:
        distance = geodesic(COLLEGE_LOCATION, student_location).meters
        return distance <= radius
    return False


