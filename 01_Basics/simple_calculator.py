Simple Calculator

This program performs:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power

CODE: 

print("=" * 50)
print("          SIMPLE CALCULATOR")
print("=" * 50)

while True:

    print("\nChoose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("\nThank you for using the Calculator.")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid Choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Please enter valid numeric values.")
        continue

    if choice == "1":
        result = num1 + num2
        print("\nAddition =", result)

    elif choice == "2":
        result = num1 - num2
        print("\nSubtraction =", result)

    elif choice == "3":
        result = num1 * num2
        print("\nMultiplication =", result)

    elif choice == "4":
        if num2 == 0:
            print("\nDivision by zero is not allowed.")
        else:
            result = num1 / num2
            print("\nDivision =", result)

    elif choice == "5":
        if num2 == 0:
            print("\nCannot perform modulus with zero.")
        else:
            result = num1 % num2
            print("\nModulus =", result)

    elif choice == "6":
        result = num1 ** num2
        print("\nPower =", result)

    print("-" * 50)

Added Simple Calculator Program
