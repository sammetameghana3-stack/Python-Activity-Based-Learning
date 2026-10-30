
# Library Borrowing and Fine Reconciliation

FINE_PER_DAY = 5

borrowing_records = []

# Read borrowing details
n = int(input("Enter number of borrowing records: "))

for i in range(n):
    print("\nBook Record", i + 1)

    book_id = input("Enter Book ID: ")
    allowed_days = int(input("Enter allowed borrowing days: "))
    actual_days = int(input("Enter actual borrowing days: "))

    return_status = input(
        "Has the book been returned? (YES/NO): "
    ).upper()

    # Validate input
    if allowed_days <= 0 or actual_days < 0:
        print("Invalid borrowing period. Enter again.")
        continue

    if return_status not in ("YES", "NO"):
        print("Invalid return status. Enter YES or NO.")
        continue

    # Store details as a tuple
    record = (book_id, allowed_days, actual_days, return_status)
    borrowing_records.append(record)

# Initialize audit variables
overdue_records = []
total_fine = 0
available_books = []
borrowed_books = []

# Analyse borrowing records
for record in borrowing_records:
    book_id, allowed_days, actual_days, status = record

    delayed_days = max(0, actual_days - allowed_days)
    fine = delayed_days * FINE_PER_DAY

    total_fine += fine

    if delayed_days > 0:
        overdue_records.append((book_id, delayed_days, fine))

    # Reconcile book availability
    if status == "YES":
        available_books.append(book_id)
    else:
        borrowed_books.append(book_id)

# Display all borrowing records
print("\n========== LIBRARY AUDIT REPORT ==========")

print("\nBorrowing Records:")
for record in borrowing_records:
    print(record)

# Display overdue records
print("\nOverdue Records:")
if overdue_records:
    for book_id, delayed_days, fine in overdue_records:
        print("Book ID:", book_id)
        print("Delayed Days:", delayed_days)
        print("Fine: Rs.", fine)
        print("----------------------")
else:
    print("No overdue books.")

# Display fine summary
print("\nTotal Fine: Rs.", total_fine)

# Display availability
print("\nBook Availability:")

print("Available Books:")
if available_books:
    for book_id in available_books:
        print(book_id)
else:
    print("None")

print("\nCurrently Borrowed Books:")
if borrowed_books:
    for book_id in borrowed_books:
        print(book_id)
else:
    print("None")

print("\nTotal Records:", len(borrowing_records))
print("Available Books Count:", len(available_books))
print("Borrowed Books Count:", len(borrowed_books))

print("\nLibrary Reconciliation Completed.")

