Student Grade Management System

Description:
This program accepts student details and marks,
calculates total, percentage, grade, and
displays a formatted report card.

CODE:

print("=" * 60)
print("           STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 60)

# Student Details
name = input("Enter Student Name : ")
roll_no = input("Enter Roll Number  : ")
branch = input("Enter Branch       : ")

print("\nEnter Marks (Out of 100)")

python = float(input("Python             : "))
java = float(input("Java               : "))
dbms = float(input("DBMS               : "))
os = float(input("Operating System   : "))
cn = float(input("Computer Networks  : "))

# Validate Marks
subjects = [python, java, dbms, os, cn]

for mark in subjects:
    if mark < 0 or mark > 100:
        print("\nInvalid Marks Entered!")
        exit()

# Calculations
total = sum(subjects)
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
result = "PASS"

for mark in subjects:
    if mark < 35:
        result = "FAIL"
        break

# Display Report
print("\n" + "=" * 60)
print("                 STUDENT REPORT CARD")
print("=" * 60)

print(f"Student Name      : {name}")
print(f"Roll Number       : {roll_no}")
print(f"Branch            : {branch}")

print("-" * 60)

print(f"Python            : {python}")
print(f"Java              : {java}")
print(f"DBMS              : {dbms}")
print(f"Operating System  : {os}")
print(f"Computer Networks : {cn}")

print("-" * 60)

print(f"Total Marks       : {total}/500")
print(f"Percentage        : {percentage:.2f}%")
print(f"Grade             : {grade}")
print(f"Result            : {result}")

print("=" * 60)

if result == "PASS":
    if grade == "A+":
        print("Outstanding Performance!")
    elif grade == "A":
        print("Excellent Work!")
    elif grade == "B":
        print("Very Good!")
    elif grade == "C":

  Added Student Grade Management System
