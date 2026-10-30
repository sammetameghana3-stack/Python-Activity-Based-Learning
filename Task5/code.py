
# Student Marks Matrix Analysis System

def calculate_row_statistics(marks):
    """Calculate student-wise statistics."""
    row_results = []

    for row in marks:
        total = sum(row)
        average = total / len(row)
        highest = max(row)
        lowest = min(row)

        row_results.append({
            "total": total,
            "average": average,
            "highest": highest,
            "lowest": lowest
        })

    return row_results


def calculate_column_statistics(marks, subjects):
    """Calculate subject-wise statistics."""
    column_results = []

    for j in range(len(subjects)):
        column = [marks[i][j] for i in range(len(marks))]

        total = sum(column)
        average = total / len(column)
        highest = max(column)
        lowest = min(column)

        column_results.append({
            "subject": subjects[j],
            "total": total,
            "average": average,
            "highest": highest,
            "lowest": lowest
        })

    return column_results


def main():

    print("===== STUDENT MARKS MATRIX ANALYSIS =====")

    try:
        students_count = int(input("Enter number of students: "))
        subjects_count = int(input("Enter number of subjects: "))

        if students_count <= 0 or subjects_count <= 0:
            print("Students and subjects must be positive.")
            return

        students = []
        subjects = []
        marks = []

        # Enter subject names
        print("\nEnter subject names:")

        for i in range(subjects_count):
            subject = input(f"Subject {i + 1}: ").strip()

            if not subject:
                print("Subject name cannot be empty.")
                return

            subjects.append(subject)

        # Enter student details and marks
        for i in range(students_count):

            print(f"\nEnter details of Student {i + 1}")

            name = input("Student name: ").strip()

            if not name:
                print("Student name cannot be empty.")
                return

            students.append(name)

            student_marks = []

            for j in range(subjects_count):

                while True:
                    mark = float(
                        input(f"Enter marks in {subjects[j]}: ")
                    )

                    if 0 <= mark <= 100:
                        student_marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

            marks.append(student_marks)

        # Display marks matrix
        print("\n===== STUDENT MARKS MATRIX =====")

        print("Student", end="\t")

        for subject in subjects:
            print(subject, end="\t")

        print()

        for i in range(students_count):
            print(students[i], end="\t")

            for mark in marks[i]:
                print(mark, end="\t")

            print()

        # Row-wise analysis
        row_results = calculate_row_statistics(marks)

        print("\n===== ROW-WISE STATISTICS =====")
        print("Name\tTotal\tAverage\tHighest\tLowest")

        for i, result in enumerate(row_results):

            print(
                f"{students[i]}\t"
                f"{result['total']:.2f}\t"
                f"{result['average']:.2f}\t"
                f"{result['highest']:.2f}\t"
                f"{result['lowest']:.2f}"
            )

        # Column-wise analysis
        column_results = calculate_column_statistics(
            marks, subjects
        )

        print("\n===== COLUMN-WISE STATISTICS =====")
        print("Subject\tTotal\tAverage\tHighest\tLowest")

        for result in column_results:

            print(
                f"{result['subject']}\t"
                f"{result['total']:.2f}\t"
                f"{result['average']:.2f}\t"
                f"{result['highest']:.2f}\t"
                f"{result['lowest']:.2f}"
            )

        # Identify top performers
        highest_average = max(
            result["average"] for result in row_results
        )

        print("\n===== TOP PERFORMER(S) =====")

        for i, result in enumerate(row_results):

            if result["average"] == highest_average:
                print(
                    f"{students[i]} - "
                    f"{result['average']:.2f}%"
                )

        # Identify low-performing subjects
        print("\n===== LOW-PERFORMING SUBJECTS =====")

        low_subjects = [
            result for result in column_results
            if result["average"] < 50
        ]

        if low_subjects:
            for result in low_subjects:
                print(
                    f"{result['subject']} - "
                    f"Average: {result['average']:.2f}%"
                )
        else:
            print("No low-performing subjects found.")

        print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


if __name__ == "__main__":
    main()

