
# Smart Electricity Billing for Multiple Apartments

FIXED_CHARGE = 50
REBATE_RATE = 0.10
DISCREPANCY_LIMIT = 1.00

# Function to calculate progressive electricity charges
def calculate_electricity_charge(units):

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    else:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    return charge


# Read apartment details
apartments = []

n = int(input("Enter number of apartments: "))

for i in range(n):
    print("\nApartment", i + 1)

    apartment_id = input("Enter Apartment ID: ")
    units = float(input("Enter electricity units consumed: "))
    recorded_bill = float(input("Enter recorded bill amount: "))

    if units < 0 or recorded_bill < 0:
        print("Invalid input. Units and bill cannot be negative.")
        continue

    apartments.append(
        (apartment_id, units, recorded_bill)
    )


# Calculate bills and identify discrepancies
billing_report = []
discrepancies = []

for apartment in apartments:

    apartment_id, units, recorded_bill = apartment

    # Calculate progressive charge
    electricity_charge = calculate_electricity_charge(units)

    # Add fixed charge
    total_before_rebate = electricity_charge + FIXED_CHARGE

    # Calculate rebate
    if units < 100:
        rebate = electricity_charge * REBATE_RATE
    else:
        rebate = 0

    # Calculate final bill
    final_bill = total_before_rebate - rebate

    # Find difference between recorded and calculated bill
    difference = abs(recorded_bill - final_bill)

    # Store billing details
    report = (
        apartment_id,
        units,
        electricity_charge,
        FIXED_CHARGE,
        rebate,
        final_bill,
        recorded_bill,
        difference
    )

    billing_report.append(report)

    # Identify billing discrepancies
    if difference > DISCREPANCY_LIMIT:
        discrepancies.append(report)


# Rank apartments by electricity consumption
ranked_apartments = sorted(
    billing_report,
    key=lambda x: x[1],
    reverse=True
)


# Display billing report
print("\n========== ELECTRICITY BILLING REPORT ==========")

for report in billing_report:

    (apartment_id, units, electricity_charge,
     fixed_charge, rebate, final_bill,
     recorded_bill, difference) = report

    print("\nApartment ID:", apartment_id)
    print("Units Consumed:", units)
    print("Electricity Charge: Rs.", round(electricity_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Rebate: Rs.", round(rebate, 2))
    print("Calculated Bill: Rs.", round(final_bill, 2))
    print("Recorded Bill: Rs.", round(recorded_bill, 2))
    print("Difference: Rs.", round(difference, 2))


# Display discrepancies
print("\n========== BILLING DISCREPANCIES ==========")

if discrepancies:
    for report in discrepancies:
        print(
            report[0],
            "- Calculated: Rs.", round(report[5], 2),
            "| Recorded: Rs.", round(report[6], 2),
            "| Difference: Rs.", round(report[7], 2)
        )
else:
    print("No billing discrepancies found.")


# Display consumption ranking
print("\n========== APARTMENT CONSUMPTION RANKING ==========")

for rank, apartment in enumerate(ranked_apartments, start=1):
    print(
        rank,
        apartment[0],
        "-",
        apartment[1],
        "units"
    )

print("\nElectricity Billing Analysis Completed.")

