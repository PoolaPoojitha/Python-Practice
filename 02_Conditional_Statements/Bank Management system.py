Bank Management System

Features:
- Create Account
- Deposit Money
- Withdraw Money
- Balance Enquiry
- Account Details
- Exit

CODE:

print("=" * 60)
print("          BANK MANAGEMENT SYSTEM")
print("=" * 60)

account = {}

while True:

    print("\n========= MAIN MENU =========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Balance Enquiry")
    print("5. Account Details")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # -----------------------------
    # Create Account
    # -----------------------------
    if choice == "1":

        if account:
            print("\nAccount already exists!")
            continue

        print("\n------ Create Account ------")

        account["name"] = input("Enter Name: ")
        account["account_no"] = input("Enter Account Number: ")
        account["mobile"] = input("Enter Mobile Number: ")

        while True:
            try:
                amount = float(input("Enter Initial Deposit: ₹"))
                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    account["balance"] = amount
                    break
            except ValueError:
                print("Please enter a valid amount.")

        print("\nAccount Created Successfully!")

    # -----------------------------
    # Deposit
    # -----------------------------
    elif choice == "2":

        if not account:
            print("\nPlease create an account first.")
            continue

        try:
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")

            else:
                account["balance"] += amount
                print("Deposit Successful!")
                print("Current Balance: ₹", account["balance"])

        except ValueError:
            print("Invalid Input!")

    # -----------------------------
    # Withdraw
    # -----------------------------
    elif choice == "3":

        if not account:
            print("\nPlease create an account first.")
            continue

        try:
            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > account["balance"]:
                print("Insufficient Balance!")

            else:
                account["balance"] -= amount
                print("Please Collect Your Cash")
                print("Remaining Balance: ₹", account["balance"])

        except ValueError:
            print("Invalid Input!")

    # -----------------------------
    # Balance
    # -----------------------------
    elif choice == "4":

        if not account:
            print("\nPlease create an account first.")
        else:
            print("\nCurrent Balance: ₹", account["balance"])

    # -----------------------------
    # Account Details
    # -----------------------------
    elif choice == "5":

        if not account:
            print("\nNo Account Found!")

        else:

            print("\n========== ACCOUNT DETAILS ==========")
            print("Account Holder :", account["name"])
            print("Account Number :", account["account_no"])
            print("Mobile Number  :", account["mobile"])
            print("Balance        : ₹", account["balance"])
            print("=====================================")

    # -----------------------------
    # Exit
    # -----------------------------
    elif choice == "6":

        print("\nThank you for using Bank Management System.")
        break

    else:
        print("\nInvalid Choice! Please try again.")

Added Bank Management System Program
