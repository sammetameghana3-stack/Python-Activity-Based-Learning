# Multi-Stage ATM Transaction Audit Using Python

## 1. Problem Statement
 Multi-Stage ATM Transaction Audit: Process a sequence of deposits, withdrawals, and transfers 
in a simulated account, maintain balances, detect invalid operations, and report suspicious repeated 
patterns.
## 2. Algorithm

1. Start the program.
2. Initialize the account balance.
3. Read the number of transactions.
4. For each transaction:
   - Read the transaction type.
   - Read the transaction amount.
5. Check the transaction type.
6. If the transaction is a deposit:
   - Check whether the amount is positive.
   - Add the amount to the balance.
7. If the transaction is a withdrawal:
   - Check whether the amount is positive.
   - Check whether sufficient balance is available.
   - Deduct the amount if valid.
8. If the transaction is a transfer:
   - Check whether the amount is positive.
   - Check whether sufficient balance is available.
   - Deduct the amount from the sender and add it to the receiver.
9. Record successful and failed transactions.
10. Detect repeated withdrawals of the same amount.
11. Display the final account balance.
12. Display the transaction audit report.
13. Stop.

## 3. Flowchart Using Mermaid
```mermaid
flowchart TD
    A([Start]) --> B[Initialize Account Balance]
    B --> C[Read Number of Transactions]
    C --> D[Read Transaction Details]
    D --> E{Transaction Type?}

    E -->|Deposit| F{Amount > 0?}
    F -->|Yes| G[Add Amount to Balance]
    F -->|No| H[Record Invalid Transaction]

    E -->|Withdrawal| I{Amount > 0?}
    I -->|Yes| J{Sufficient Balance?}
    I -->|No| H
    J -->|Yes| K[Deduct Amount]
    J -->|No| H

    E -->|Transfer| L{Valid Amount and Balance?}
    L -->|Yes| M[Deduct from Sender]
    M --> N[Add to Receiver]
    L -->|No| H

    E -->|Invalid Type| H

    G --> O[Record Transaction]
    K --> O
    N --> O
    H --> P[Record Failed Transaction]

    O --> Q{More Transactions?}
    P --> Q
    Q -->|Yes| D
    Q -->|No| R[Detect Suspicious Patterns]
    R --> S[Generate Audit Report]
    S --> T([Stop])
```

## 4. Sample Input

Assume the initial account balance is Rs. 10,000 and the receiver's balance is Rs. 5,000.

```
Enter number of transactions: 6

Transaction 1
Enter transaction type: 1
Enter amount: 2000

Transaction 2
Enter transaction type: 2
Enter amount: 1000

Transaction 3
Enter transaction type: 2
Enter amount: 1000

Transaction 4
Enter transaction type: 2
Enter amount: 1000

Transaction 5
Enter transaction type: 3
Enter amount: 3000

Transaction 6
Enter transaction type: 2
Enter amount: 20000
```

## 5. Sample Output

```
Deposit successful!

Withdrawal successful!

Withdrawal successful!

Withdrawal successful!

Transfer successful!

Insufficient balance!

========== ATM AUDIT REPORT ==========

Final Account Balance: Rs. 6000.0
Receiver Account Balance: Rs. 8000.0

Successful Transactions:
Deposit: Rs.2000.0
Withdrawal: Rs.1000.0
Withdrawal: Rs.1000.0
Withdrawal: Rs.1000.0
Transfer: Rs.3000.0

Failed Transactions:
Withdrawal failed

Suspicious Activities:
Repeated withdrawal detected: Rs. 1000.0

Total Successful Transactions: 5
Total Failed Transactions: 1

========== AUDIT COMPLETED ==========
```

## 8. Conclusion
