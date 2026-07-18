Employee Salary Management System

Description:
This program calculates an employee's salary
by considering HRA, DA, PF, and Income Tax,
then generates a formatted salary slip.

CODE:

print("=" * 65)
print("            EMPLOYEE SALARY MANAGEMENT SYSTEM")
print("=" * 65)

# Employee Details
emp_name = input("Enter Employee Name : ")
emp_id = input("Enter Employee ID   : ")
department = input("Enter Department    : ")
designation = input("Enter Designation   : ")

# Basic Salary
basic_salary = float(input("Enter Basic Salary (₹): "))

# Validate Salary
if basic_salary <= 0:
    print("\nInvalid Salary!")
    exit()

# Salary Components
hra = basic_salary * 0.20       # 20%
da = basic_salary * 0.15        # 15%
pf = basic_salary * 0.12        # 12%
tax = basic_salary * 0.05       # 5%

gross_salary = basic_salary + hra + da
net_salary = gross_salary - (pf + tax)

# Salary Slip
print("\n" + "=" * 65)
print("                    EMPLOYEE SALARY SLIP")
print("=" * 65)

print(f"Employee Name     : {emp_name}")
print(f"Employee ID       : {emp_id}")
print(f"Department        : {department}")
print(f"Designation       : {designation}")

print("-" * 65)

print(f"Basic Salary      : ₹ {basic_salary:,.2f}")
print(f"HRA (20%)         : ₹ {hra:,.2f}")
print(f"DA (15%)          : ₹ {da:,.2f}")

print("-" * 65)

print(f"Gross Salary      : ₹ {gross_salary:,.2f}")

print("-" * 65)

print(f"PF Deduction      : ₹ {pf:,.2f}")
print(f"Income Tax (5%)   : ₹ {tax:,.2f}")

print("-" * 65)

print(f"Net Salary        : ₹ {net_salary:,.2f}")

print("=" * 65)

# Salary Category
if net_salary >= 100000:
    category = "High Income"
elif net_salary >= 50000:
    category = "Medium Income"
else:
    category = "Standard Income"

print(f"Salary Category   : {category}")

print("=" * 65)
print("Thank you for using the Employee Salary Management System.

Added Employee Salary Management System
