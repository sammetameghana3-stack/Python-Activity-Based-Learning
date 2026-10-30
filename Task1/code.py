
# University Scholarship Allocation System

MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75.0
MAX_FAMILY_INCOME = 250000


def evaluate_applicant(applicant):
    """Check eligibility and calculate aggregate percentage."""
    marks = applicant["marks"]
    aggregate = sum(marks) / len(marks)
    applicant["aggregate"] = aggregate

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if any(mark < MIN_SUBJECT_MARKS for mark in marks):
        reasons.append("Subject mark below 40")

    if applicant["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if applicant["income"] > MAX_FAMILY_INCOME:
        reasons.append("Family income exceeds Rs. 2,50,000")

    applicant["eligible"] = len(reasons) == 0
    applicant["reasons"] = reasons

    return applicant


def allocate_scholarships(applicants):
    """Rank eligible applicants using predefined tie-breakers."""
    eligible = [a for a in applicants if a["eligible"]]
    ineligible = [a for a in applicants if not a["eligible"]]

    # Priority:
    # 1. Higher aggregate marks
    # 2. Higher attendance
    # 3. Lower family income
    # 4. Alphabetical order of name
    eligible.sort(
        key=lambda a: (
            -a["aggregate"],
            -a["attendance"],
            a["income"],
            a["name"].casefold()
        )
    )

    for rank, applicant in enumerate(eligible, start=1):
        applicant["rank"] = rank

    return eligible, ineligible


def main():
    applicants = []

    try:
        n = int(input("Enter number of applicants: "))

        if n <= 0:
            print("Number of applicants must be positive.")
            return

        for i in range(n):
            print(f"\nEnter details for applicant {i + 1}")

            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty. Try again.")
                return

            subjects = int(input("Number of subjects: "))
            if subjects <= 0:
                print("Number of subjects must be positive.")
                return

            marks = []
            for j in range(subjects):
                mark = float(input(f"Marks in subject {j + 1} (0-100): "))
                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100.")
                    return
                marks.append(mark)

            attendance = float(input("Attendance percentage (0-100): "))
            if not 0 <= attendance <= 100:
                print("Attendance must be between 0 and 100.")
                return

            income = float(input("Annual family income (Rs.): "))
            if income < 0:
                print("Income cannot be negative.")
                return

            applicant = {
                "name": name,
                "marks": marks,
                "attendance": attendance,
                "income": income
            }

            applicants.append(evaluate_applicant(applicant))

        eligible, ineligible = allocate_scholarships(applicants)

        print("\n===== SCHOLARSHIP MERIT LIST =====")
        if eligible:
            print("Rank | Name | Aggregate | Attendance | Income (Rs.)")
            for a in eligible:
                print(
                    f"{a['rank']:>4} | {a['name']} | "
                    f"{a['aggregate']:.2f}% | "
                    f"{a['attendance']:.2f}% | {a['income']:.2f}"
                )
        else:
            print("No eligible applicants.")

        print("\n===== INELIGIBLE APPLICANTS =====")
        if ineligible:
            for a in ineligible:
                print(f"\nName: {a['name']}")
                print(f"Aggregate: {a['aggregate']:.2f}%")
                print("Reasons: " + ", ".join(a["reasons"]))
        else:
            print("No ineligible applicants.")

    except ValueError:
        print("Invalid input. Enter numeric values where required.")


if __name__ == "__main__":
    main()

