# Student Information System

print("=" * 40)
print("      STUDENT INFORMATION SYSTEM")
print("=" * 40)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
year = input("Enter Year: ")
cgpa = float(input("Enter CGPA: "))

print("\n--------- STUDENT DETAILS ---------")
print(f"Name   : {name}")
print(f"Roll No: {roll}")
print(f"Branch : {branch}")
print(f"Year   : {year}")
print(f"CGPA   : {cgpa}")

if cgpa >= 9:
    grade = "Excellent"
elif cgpa >= 8:
    grade = "Very Good"
elif cgpa >= 7:
    grade = "Good"
else:
    grade = "Needs Improvement"

print(f"Performance : {grade}")

Added Student Information System 
