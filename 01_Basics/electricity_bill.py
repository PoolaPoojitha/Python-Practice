Electricity Bill Calculator

Description:
This program calculates the electricity bill
based on slab rates, fixed charges, meter rent,
and GST.

CODE:

print("=" * 60)
print("            ELECTRICITY BILL GENERATOR")
print("=" * 60)
consumer_name = input("Enter Consumer Name : ")
consumer_no = input("Enter Consumer Number : ")
previous_reading = int(input("Enter Previous Meter Reading : "))
current_reading = int(input("Enter Current Meter Reading : "))
units = current_reading - previous_reading
if units < 0:
    print("\nInvalid meter readings!")
    exit()
print("\nTotal Units Consumed :", units)

# -------------------------------
# Slab Calculation
# -------------------------------

bill = 0
if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = (100 * 1.50) + ((units - 100) * 2.50)
elif units <= 300:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
else:
    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.00)

# Additional Charges

fixed_charge = 100
meter_rent = 50
subtotal = bill + fixed_charge + meter_rent
gst = subtotal * 0.05
total_bill = subtotal + gst
print("\n" + "=" * 60)
print("              ELECTRICITY BILL")
print("=" * 60)
print(f"Consumer Name     : {consumer_name}")
print(f"Consumer Number   : {consumer_no}")
print(f"Previous Reading  : {previous_reading}")
print(f"Current Reading   : {current_reading}")
print(f"Units Consumed    : {units}")
print("-" * 60)
print(f"Energy Charges    : ₹ {bill:.2f}")
print(f"Fixed Charges     : ₹ {fixed_charge:.2f}")
print(f"Meter Rent        : ₹ {meter_rent:.2f}")
print(f"GST (5%)          : ₹ {gst:.2f}")
print("-" * 60)
print(f"TOTAL BILL        : ₹ {total_bill:.2f}")
print("=" * 60)
print("\nThank you for using the Electricity Bill Generator.")

Added electricity bill Program
