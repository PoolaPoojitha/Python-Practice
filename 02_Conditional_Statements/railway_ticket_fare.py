Railway Ticket Fare Calculator

Description:
Calculates railway ticket fare based on:
- Distance
- Travel Class
- Age
- Gender
- Senior Citizen Discount

CODE:

print("=" * 70)
print("             RAILWAY TICKET FARE CALCULATOR")
print("=" * 70)

# Passenger Details
name = input("Enter Passenger Name : ")
age = int(input("Enter Age            : "))
gender = input("Enter Gender (M/F)   : ").upper()
distance = float(input("Enter Distance (km)  : "))

print("\nTravel Classes")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
print("4. First Class")

choice = int(input("Select Travel Class (1-4): "))

# Fare per km
if choice == 1:
    rate = 1.5
    travel_class = "Sleeper"

elif choice == 2:
    rate = 2.5
    travel_class = "AC 3 Tier"

elif choice == 3:
    rate = 3.5
    travel_class = "AC 2 Tier"

elif choice == 4:
    rate = 5.0
    travel_class = "First Class"

else:
    print("Invalid Travel Class!")
    exit()

# Base Fare
base_fare = distance * rate

# Senior Citizen Discount
discount = 0

if gender == "M" and age >= 60:
    discount = base_fare * 0.40

elif gender == "F" and age >= 58:
    discount = base_fare * 0.50

# GST
gst = (base_fare - discount) * 0.05

# Total Fare
total_fare = base_fare - discount + gst

print("\n" + "=" * 70)
print("                   TICKET DETAILS")
print("=" * 70)

print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"Gender         : {gender}")
print(f"Distance       : {distance} km")
print(f"Travel Class   : {travel_class}")

print("-" * 70)

print(f"Base Fare      : ₹ {base_fare:.2f}")
print(f"Discount       : ₹ {discount:.2f}")
print(f"GST (5%)       : ₹ {gst:.2f}")

print("-" * 70)

print(f"Total Fare     : ₹ {total_fare:.2f}")

print("=" * 70)

if discount > 0:
    print("Senior Citizen Discount Applied.")
else:
    print("No Discount Applied.")

print("Thank You! Have a Safe Journey.")
print("=" * 70)

Added Railway Ticket Fare Calculator
