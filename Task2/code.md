
# Hospital Billing and Patient Classification System

SENIOR_CONCESSION = 10
HIGH_BILL_CONCESSION = 5
BILL_LIMIT = 10000
SENIOR_AGE = 60


def calculate_bill(consultation, diagnostic, treatment, age):
    # Calculate total charges
    total = consultation + diagnostic + treatment

    # Calculate conditional concessions
    concession_rate = 0

    if age >= SENIOR_AGE:
        concession_rate += SENIOR_CONCESSION

    if total > BILL_LIMIT:
        concession_rate += HIGH_BILL_CONCESSION

    # Calculate concession and final bill
    concession = total * concession_rate / 100
    final_bill = total - concession

    return total, concession, final_bill, concession_rate


def classify_patient(paid, final_bill):
    # Classify patient according to payment policy
    if paid == final_bill:
        return "Fully Paid"
    elif paid == 0:
        return "Unpaid"
    else:
        return "Partially Paid"


def main():
    print("===== HOSPITAL BILLING SYSTEM =====")

    try:
        # Get patient details
        name = input("Enter patient name: ").strip()

        if not name:
            print("Patient name cannot be empty.")
            return

        age = int(input("Enter patient age: "))

        if age < 0:
            print("Age cannot be negative.")
            return

        # Get hospital charges
        consultation = float(
            input("Enter consultation charges: Rs.")
        )

        diagnostic = float(
            input("Enter diagnostic charges: Rs.")
        )

        treatment = float(
            input("Enter treatment charges: Rs.")
        )

        # Validate charges
        if min(consultation, diagnostic, treatment) < 0:
            print("Charges cannot be negative.")
            return

        # Calculate hospital bill
        total, concession, final_bill, rate = calculate_bill(
            consultation, diagnostic, treatment, age
        )

        print("\n===== BILL SUMMARY =====")
        print(f"Patient Name       : {name}")
        print(f"Patient Age        : {age}")
        print(f"Consultation       : Rs.{consultation:.2f}")
        print(f"Diagnostic         : Rs.{diagnostic:.2f}")
        print(f"Treatment          : Rs.{treatment:.2f}")
        print(f"Total Bill         : Rs.{total:.2f}")
        print(f"Concession Rate    : {rate}%")
        print(f"Concession Amount  : Rs.{concession:.2f}")
        print(f"Final Bill         : Rs.{final_bill:.2f}")

        # Get payment details
        paid = float(input("\nEnter amount paid: Rs."))

        # Validate payment
        if paid < 0 or paid > final_bill:
            print("Invalid payment amount!")
            print("Payment must be between 0 and final bill.")
            return

        # Calculate balance
        balance = final_bill - paid

        # Classify patient
        status = classify_patient(paid, final_bill)

        # Display final details
        print("\n===== PAYMENT DETAILS =====")
        print(f"Amount Paid        : Rs.{paid:.2f}")
        print(f"Outstanding Balance: Rs.{balance:.2f}")
        print(f"Patient Category   : {status}")

        print("\n===== BILL GENERATED SUCCESSFULLY =====")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


if __name__ == "__main__":
    main()

