#ATM Transaction Simulation
balance = 5000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("New Balance:", balance)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("New Balance:", balance)
    else:
        print("Insufficient Balance")

elif choice == 3:
    print("Current Balance:", balance)

else:
    print("Invalid Choice")

