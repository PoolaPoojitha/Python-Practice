Scholarship Eligibility Checker

Description:
Checks whether a student is eligible for a scholarship
based on CGPA, family income, attendance, and backlogs.

CODE:

print("=" * 70)
print(" SCHOLARSHIP ELIGIBILITY CHECKER")
print("=" * 70)

# Student Details
name = input("Enter Student Name       : ")
roll_no = input("Enter Roll Number        : ")
branch = input("Enter Branch             : ")

cgpa = float(input("Enter CGPA (0 - 10)      : "))
attendance = float(input("Enter Attendance (%)     : "))
family_income = float(input("Enter Annual Family Income (₹): "))
backlogs = int(input("Enter Number of Backlogs : "))

# Validation
if cgpa < 0 or cgpa > 10:
    print("\nInvalid CGPA!")
    exit()

if attendance < 0 or attendance > 100:
    print("\nInvalid Attendance!")
    exit()

if family_income < 0:
    print("\nInvalid Family Income!")
    exit()

if backlogs < 0:
    print("\nInvalid Number of Backlogs!")
    exit()

print("\n" + "=" * 70)
print("SCHOLARSHIP RESULT")
print("=" * 70)

print(f"Student Name        : {name}")
print(f"Roll Number         : {roll_no}")
print(f"Branch              : {branch}")
print(f"CGPA                : {cgpa}")
print(f"Attendance          : {attendance}%")
print(f"Family Income       : ₹ {family_income:,.2f}")
print(f"Backlogs            : {backlogs}")

print("-" * 70)

# Eligibility Check
if cgpa >= 9.0 and attendance >= 90 and family_income <= 300000 and backlogs == 0:

    scholarship = "100% Scholarship"
    amount = 100000

elif cgpa >= 8.0 and attendance >= 85 and family_income <= 500000 and backlogs <= 1:

    scholarship = "75% Scholarship"
    amount = 75000

elif cgpa >= 7.0 and attendance >= 80 and family_income <= 700000 and backlogs <= 2:

    scholarship = "50% Scholarship"
    amount = 50000

else:

    scholarship = "Not Eligible"
    amount = 0

print(f"Scholarship Status  : {scholarship}")

if amount > 0:
    print(f"Scholarship Amount  : ₹ {amount:,}")
else:
    print("Scholarship Amount  : ₹ 0")

print("-" * 70)

# Reason / Suggestion
if scholarship == "Not Eligible":

    print("Reason(s):")

    if cgpa < 7:
        print("• CGPA is below the required minimum.")

    if attendance < 80:
        print("• Attendance is below 80%.")

    if family_income > 700000:
        print("• Family income exceeds the eligibility limit.")

    if backlogs > 2:
        print("• Too many backlogs.")

    print("\nSuggestion:")
    print("Improve your academic performance, attendance,")
    print("and clear backlogs before applying again.")

else:

    print("Congratulations!")
    print("You are eligible for the scholarship.")

print("=" * 70)
print("Thank you for using Scholarship Eligibility Checker.")

Added Scholarship eligibility Checker system
