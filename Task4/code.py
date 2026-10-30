
# Attendance Recovery Computation System

def calculate_attendance(attended, total):
    """Calculate current attendance percentage."""
    return (attended / total) * 100


def minimum_classes_required(attended, total, threshold):
    """Calculate minimum consecutive classes to attend."""
    if attended / total * 100 >= threshold:
        return 0

    required = 0

    while True:
        required += 1

        new_attended = attended + required
        new_total = total + required

        percentage = (new_attended / new_total) * 100

        if percentage >= threshold:
            return required


def scenario_recovery(attended, total, threshold, pattern):
    """
    Calculate recovery for a repeating future attendance pattern.

    1 = Attend
    0 = Absent
    """

    if attended / total * 100 >= threshold:
        return 0, attended / total * 100

    new_attended = attended
    new_total = total

    # Check up to 100000 future classes
    for classes in range(1, 100001):

        # Repeat the given attendance pattern
        status = pattern[(classes - 1) % len(pattern)]

        new_total += 1

        if status == 1:
            new_attended += 1

        percentage = (new_attended / new_total) * 100

        if percentage >= threshold:
            return classes, percentage

    return None, percentage


def main():

    print("===== ATTENDANCE RECOVERY SYSTEM =====")

    try:
        total = int(input("Enter total classes conducted: "))
        attended = int(input("Enter classes attended: "))
        threshold = float(input("Enter eligibility threshold (%): "))

        # Input validation
        if total <= 0:
            print("Total classes must be greater than zero.")
            return

        if attended < 0 or attended > total:
            print("Invalid attended classes.")
            return

        if not 0 < threshold <= 100:
            print("Threshold must be greater than 0 and at most 100.")
            return

        # Calculate current attendance
        current = calculate_attendance(attended, total)

        print("\n===== CURRENT ATTENDANCE =====")
        print(f"Total Classes       : {total}")
        print(f"Classes Attended    : {attended}")
        print(f"Current Attendance : {current:.2f}%")
        print(f"Eligibility Target  : {threshold:.2f}%")

        if current >= threshold:
            print("\nStatus: ELIGIBLE")
            print("No additional classes are required.")

        else:
            print("\nStatus: NOT ELIGIBLE")

            # Calculate minimum classes if all future
            # classes are attended
            minimum = minimum_classes_required(
                attended, total, threshold
            )

            print("\n===== FULL ATTENDANCE RECOVERY =====")
            print(f"Minimum consecutive classes required: {minimum}")

            final_percentage = (
                (attended + minimum) / (total + minimum)
            ) * 100

            print(f"Expected attendance: {final_percentage:.2f}%")

        # Different future attendance scenarios
        scenarios = {
            "Attend every class": [1],
            "Attend 4 classes, miss 1": [1, 1, 1, 1, 0],
            "Attend alternate classes": [1, 0]
        }

        print("\n===== FUTURE ATTENDANCE SCENARIOS =====")

        for name, pattern in scenarios.items():

            classes, percentage = scenario_recovery(
                attended, total, threshold, pattern
            )

            print(f"\nScenario: {name}")

            if classes is None:
                print("Target not reached within 100000 classes.")
            elif classes == 0:
                print("Already eligible.")
            else:
                print(f"Additional classes required: {classes}")
                print(f"Expected attendance: {percentage:.2f}%")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()

