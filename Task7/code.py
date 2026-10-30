
# Tuple-Based Transaction Audit

transactions = []

# Read transaction details
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)

    transaction_id = input("Enter Transaction ID: ")
    amount = float(input("Enter Amount: "))
    transaction_type = input(
        "Enter Transaction Type (DEPOSIT/WITHDRAWAL): "
    ).upper()

    # Store transaction as a tuple
    transaction = (transaction_id, amount, transaction_type)
    transactions.append(transaction)

# Audit variables
seen_ids = set()
duplicate_ids = []
invalid_amounts = []
invalid_types = []
valid_transactions = []

# Check duplicate IDs, amounts and types
for transaction in transactions:
    tid, amount, ttype = transaction

    if tid in seen_ids:
        duplicate_ids.append(tid)
    else:
        seen_ids.add(tid)

    if amount <= 0:
        invalid_amounts.append(transaction)
    elif ttype not in ("DEPOSIT", "WITHDRAWAL"):
        invalid_types.append(transaction)
    else:
        # Only valid transactions are used for sequence checking
        if tid not in duplicate_ids:
            valid_transactions.append(transaction)

# Detect three or more consecutive withdrawals
suspicious_sequences = []
withdrawal_count = 0
current_sequence = []

for transaction in valid_transactions:
    if transaction[2] == "WITHDRAWAL":
        withdrawal_count += 1
        current_sequence.append(transaction)
    else:
        if withdrawal_count >= 3:
            suspicious_sequences.append(current_sequence)

        withdrawal_count = 0
        current_sequence = []

# Check the final sequence
if withdrawal_count >= 3:
    suspicious_sequences.append(current_sequence)

# Display audit report
print("\n========== TRANSACTION AUDIT REPORT ==========")

print("\nAll Transactions:")
for transaction in transactions:
    print(transaction)

print("\nValid Transactions:")
for transaction in valid_transactions:
    print(transaction)

print("\nDuplicate Transaction IDs:")
if duplicate_ids:
    for tid in sorted(set(duplicate_ids)):
        print(tid)
else:
    print("None")

print("\nInvalid Amount Transactions:")
if invalid_amounts:
    for transaction in invalid_amounts:
        print(transaction)
else:
    print("None")

print("\nInvalid Transaction Types:")
if invalid_types:
    for transaction in invalid_types:
        print(transaction)
else:
    print("None")

print("\nSuspicious Withdrawal Sequences:")
if suspicious_sequences:
    for sequence in suspicious_sequences:
        print(sequence)
else:
    print("None")

print("\nAudit Completed.")

