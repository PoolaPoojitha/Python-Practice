ATM Simulation System

Description:
A menu-driven ATM program that allows the user to:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Exit

CODE:

print("=" * 60)
print("              WELCOME TO PYTHON ATM")
print("=" * 60)

account_holder = input("Enter Account Holder Name : ")
account_number = input("Enter Account Number      : ")

pin = "1234"
balance = 10000

entered_pin = input("\nEnter 4-Digit ATM PIN : ")

if entered_pin != pin:
    print("\nIncorrect PIN!")
    print("Transaction Cancelled.")
    exit()

print("\nLogin Successful!")
print(f"Welcome, {account_holder}")

while True:

    print("\n" + "=" * 60)
    print("ATM MENU")
    print("=" * 60)

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Account Details")
    print("6. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":

        print("\nCurrent Balance : ₹", balance)

    elif choice == "2":

        amount = float(input("Enter Deposit Amount : ₹"))

        if amount <= 0:
            print("Invalid Amount!")

        else:
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance : ₹", balance)

    elif choice == "3":

        amount = float(input("Enter Withdrawal Amount : ₹"))

        if amount <= 0:
            print("Invalid Amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print("Please Collect Your Cash")
            print("Remaining Balance : ₹", balance)

    elif choice == "4":

        old_pin = input("Enter Current PIN : ")

        if old_pin == pin:

            new_pin = input("Enter New PIN : ")
            confirm_pin = input("Confirm New PIN : ")

            if new_pin == confirm_pin:
                pin = new_pin
                print("PIN Changed Successfully!")

            else:
                print("PIN Mismatch!")

        else:
            print("Incorrect Current PIN!")

    elif choice == "5":

        print("\nAccount Holder :", account_holder)
        print("Account Number :", account_number)
        print("Available Balance : ₹", balance)

    elif choice == "6":

        print("\nThank You for Using Python ATM")
        print("Visit Again!")
        break

    else:

        print("Invalid Choice! Please Try Again.")

Added ATM Simulation System 
