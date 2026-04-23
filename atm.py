# This is an ATM machine
print("Welcome to the ATM machine!")
print("---------------------------")
balance = 1000
while True:
    operation = str(input("Please choose your operation (check balance, deposit, withdraw or exit): "))
    if operation == "check balance":
        print(f"Your balance is ${balance}")
    elif operation == "deposit":
        depo = float(input("Please input the amount you want to deposit: $"))
        if depo <= 0:
            print("Invalid amount!")
        else:
            balance += depo
        print("Deposit successfully!")
        print(f"Your balance is now ${balance}")
    elif operation == "withdraw":
        wthdrw = float(input("Please input the amount you want to withdraw: "))
        if wthdrw > balance:
            print("Error: You cannot withdraw more than your balance!")
        else:
            balance -= wthdrw
            print("Withdraw successfully!")
            print(f"Your balance is now ${balance}")
    elif operation == "exit":
        print("Thank you for using our ATM! Goodbye!")
        break
    else:
        print("Invalid operation. Please try again.")