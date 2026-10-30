
# Multi-Stage ATM Transaction Audit System

balance = 10000
receiver_balance = 5000

successful = []
failed = []
withdrawal_history = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)

    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Transfer")

    choice = int(input("Enter transaction type: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")
        failed.append("Invalid amount")
        continue

    if choice == 1:
        balance += amount
        successful.append("Deposit: Rs." + str(amount))
        print("Deposit successful!")

    elif choice == 2:
        if amount <= balance:
            balance -= amount
            withdrawal_history.append(amount)
            successful.append("Withdrawal: Rs." + str(amount))
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
            failed.append("Withdrawal failed")

    elif choice == 3:
        if amount <= balance:
            balance -= amount
            receiver_balance += amount
            successful.append("Transfer: Rs." + str(amount))
            print("Transfer successful!")
        else:
            print("Insufficient balance!")
            failed.append("Transfer failed")

    else:
        print("Invalid transaction type!")
        failed.append("Invalid transaction type")

# Detect suspicious repeated withdrawals
suspicious = []

for amount in set(withdrawal_history):
    if withdrawal_history.count(amount) >= 3:
        suspicious.append(amount)

# Final Audit Report
print("\n========== ATM AUDIT REPORT ==========")

print("Final Account Balance: Rs.", balance)
print("Receiver Account Balance: Rs.", receiver_balance)

print("\nSuccessful Transactions:")
for transaction in successful:
    print(transaction)

print("\nFailed Transactions:")
for transaction in failed:
    print(transaction)

print("\nSuspicious Activities:")

if suspicious:
    for amount in suspicious:
        print("Repeated withdrawal detected: Rs.", amount)
else:
    print("No suspicious activities detected.")

print("\nTotal Successful Transactions:", len(successful))
print("Total Failed Transactions:", len(failed))

print("========== AUDIT COMPLETED ==========")

