Income Tax Calculator

Description:
Calculates the income tax based on annual income
and displays the tax amount and net income.

CODE

print("=" * 65)
print("              INCOME TAX CALCULATOR")
print("=" * 65)

# User Details
name = input("Enter Your Name          : ")
pan = input("Enter PAN Number         : ")
age = int(input("Enter Your Age           : "))
annual_income = float(input("Enter Annual Income (₹): "))

# Validation
if annual_income < 0:
    print("\nInvalid Income!")
    exit()

# Tax Calculation
if annual_income <= 300000:
    tax_rate = 0

elif annual_income <= 600000:
    tax_rate = 5

elif annual_income <= 900000:
    tax_rate = 10

elif annual_income <= 1200000:
    tax_rate = 15

elif annual_income <= 1500000:
    tax_rate = 20

else:
    tax_rate = 30

tax_amount = annual_income * tax_rate / 100
net_income = annual_income - tax_amount

# Tax Category
if tax_rate == 0:
    category = "No Tax"
elif tax_rate <= 10:
    category = "Low Tax"
elif tax_rate <= 20:
    category = "Moderate Tax"
else:
    category = "High Tax"

# Display Tax Report
print("\n" + "=" * 65)
print("                 INCOME TAX REPORT")
print("=" * 65)

print(f"Name             : {name}")
print(f"PAN Number       : {pan}")
print(f"Age              : {age}")
print(f"Annual Income    : ₹ {annual_income:,.2f}")

print("-" * 65)

print(f"Tax Rate         : {tax_rate}%")
print(f"Tax Amount       : ₹ {tax_amount:,.2f}")
print(f"Net Income       : ₹ {net_income:,.2f}")
print(f"Tax Category     : {category}")

print("-" * 65)

# Suggestions
if tax_rate == 0:
    print("Suggestion       : No income tax applicable.")
elif tax_rate <= 10:
    print("Suggestion       : Consider tax-saving investments.")
elif tax_rate <= 20:
    print("Suggestion       : Explore deductions under tax laws.")
else:
    print("Suggestion       : Consult a tax advisor for better tax planning.")

print("=" * 65)
print("Thank you for using the Income Tax Calculator.")

Added income tax calculator system 
