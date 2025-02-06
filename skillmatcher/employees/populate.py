from employees.models import Employee
from datetime import date
import random

employees = [
    {"name": "Sameer", "age": 35, "productivity": 90.5, "skills": "Automobile Engineering, CAD, Manufacturing Processes",
     "years_of_experience": 10, "location": "Electronic City, Bangalore", "present_tasks": "Vehicle Prototyping", 
     "nearest_deadline": date(2025, 3, 10), "present_project": "Engine R&D"},

    {"name": "Allan", "age": 30, "productivity": 85.2, "skills": "Electric Vehicles, Battery Technology, MATLAB",
     "years_of_experience": 8, "location": "Whitefield, Bangalore", "present_tasks": "Battery Testing", 
     "nearest_deadline": date(2025, 2, 28), "present_project": "EV Truck"},

    {"name": "Syed", "age": 40, "productivity": 88.1, "skills": "Mechanical Engineering, Automotive Design, SolidWorks",
     "years_of_experience": 15, "location": "Koramangala, Bangalore", "present_tasks": "Chassis Design", 
     "nearest_deadline": date(2025, 4, 5), "present_project": "Engine R&D"},

    {"name": "Aadil", "age": 28, "productivity": 92.0, "skills": "Embedded Systems, CAN Protocol, AUTOSAR",
     "years_of_experience": 6, "location": "Indiranagar, Bangalore", "present_tasks": "ECU Programming", 
     "nearest_deadline": date(2025, 2, 18), "present_project": "Smart Dashboard"},

    {"name": "Adarsh", "age": 45, "productivity": 87.4, "skills": "Vehicle Dynamics, Suspension Design, NVH Analysis",
     "years_of_experience": 20, "location": "Marathahalli, Bangalore", "present_tasks": "Aerodynamics Optimization", 
     "nearest_deadline": date(2025, 3, 20), "present_project": "Smart Dashboard"},

    {"name": "Khader", "age": 33, "productivity": 91.8, "skills": "Artificial Intelligence in Automobiles, IoT, Python",
     "years_of_experience": 12, "location": "HSR Layout, Bangalore", "present_tasks": "AI Model Training", 
     "nearest_deadline": date(2025, 4, 12), "present_project": "Smart Dashboard"},

    {"name": "Anirudh", "age": 38, "productivity": 86.5, "skills": "ADAS, LiDAR, Sensor Fusion, Machine Learning",
     "years_of_experience": 14, "location": "BTM Layout, Bangalore", "present_tasks": "Sensor Calibration", 
     "nearest_deadline": date(2025, 3, 5), "present_project": "Engine R&D"},

    {"name": "Tejas", "age": 29, "productivity": 89.0, "skills": "Quality Control, Six Sigma, Lean Manufacturing",
     "years_of_experience": 7, "location": "Jayanagar, Bangalore", "present_tasks": "Production Quality Analysis", 
     "nearest_deadline": date(2025, 2, 25), "present_project": "Engine R&D"},

    {"name": "Nick", "age": 42, "productivity": 84.3, "skills": "Automotive Software Development, C++, ROS",
     "years_of_experience": 18, "location": "Hebbal, Bangalore", "present_tasks": "Software Debugging", 
     "nearest_deadline": date(2025, 4, 7), "present_project": "EV Truck"},

    {"name": "Kavya Raj", "age": 31, "productivity": 93.1, "skills": "Hybrid Vehicles, Powertrain Engineering, Simulink",
     "years_of_experience": 9, "location": "Yelahanka, Bangalore", "present_tasks": "Hybrid Powertrain Development", 
     "nearest_deadline": date(2025, 3, 30), "present_project": "EV Truck"}
]

for emp in employees:
    Employee.objects.create(
        name=emp["name"],
        age=emp["age"],
        productivity=emp["productivity"],
        skills=emp["skills"],
        years_of_experience=emp["years_of_experience"],
        location=emp["location"],
        present_tasks=emp["present_tasks"],
        present_project=emp["present_project"],  
        nearest_deadline=emp["nearest_deadline"],
    )

print("Employees added successfully!")
