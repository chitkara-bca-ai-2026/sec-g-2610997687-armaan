# Lab 15 - Student Information Management System

# Initial Student Records
students = {
    101: {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [85, 90, 78]
    },
    102: {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 88, 95]
    },
    103: {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [76, 84, 82]
    }
}


# 1. View All Students
def view_all_students():
    print("\n--- Enrolled Student Records ---")

    if not students:
        print("No student records found.")
        return

    for roll, details in students.items():
        print(
            f"Roll No: {roll} | "
            f"Name: {details['Name']} | "
            f"Branch: {details['Branch']}"
        )
        print(
            f"Semester: {details['Semester']} | "
            f"Marks: {details['Marks']}"
        )

    print("Total Enrolled Students:", len(students))


# 2. Search Student by Roll Number
def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))

        student = students.get(roll)

        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])
        else:
            print("[ERROR] Student record not found.")

    except ValueError:
        print("Invalid input! Enter a valid Roll Number.")


# 3. Register New Student
def register_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("[ERROR] Roll Number already exists!")
            return

        name = input("Enter Student Name: ").strip()
        branch = input("Enter Branch (e.g., BCA AI): ").strip()
        semester = int(input("Enter Semester: "))

        if not name or not branch:
            print("Name and Branch cannot be empty.")
            return

        if not 1 <= semester <= 8:
            print("Semester must be between 1 and 8.")
            return

        marks = []

        print("Enter marks in 3 subjects:")

        for i in range(1, 4):
            mark = int(input(f"Subject {i}: "))

            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        students[roll] = {
            "Name": name,
            "Branch": branch,
            "Semester": semester,
            "Marks": marks
        }

        print(
            f"\n[SUCCESS] Student '{name}' "
            f"(Roll No: {roll}) registered successfully!"
        )

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# 4. Update Student Details
def update_student():
    try:
        roll = int(input("Enter Roll Number to update: "))

        if roll not in students:
            print("[ERROR] Student record not found.")
            return

        student = students[roll]

        print(f"Current details for Roll No {roll}:")
        print("1. Branch:", student["Branch"])
        print("2. Semester:", student["Semester"])

        choice = input(
            "Choose field to update (1 for Branch, 2 for Semester): "
        )

        if choice == "1":
            branch = input("Enter new Branch: ").strip()

            if branch:
                student["Branch"] = branch
                print("[SUCCESS] Branch updated successfully.")
            else:
                print("Branch cannot be empty.")

        elif choice == "2":
            semester = int(input("Enter new Semester: "))

            if 1 <= semester <= 8:
                student["Semester"] = semester
                print(
                    f"[SUCCESS] Semester updated to {semester}."
                )
            else:
                print("Invalid Semester!")

        else:
            print("Invalid field choice!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# 5. View Academic Performance
def view_academic_performance():
    try:
        roll = int(
            input("Enter Roll Number for Academic Performance: ")
        )

        if roll not in students:
            print("[ERROR] Student record not found.")
            return

        student = students[roll]
        marks = student["Marks"]

        total = sum(marks)
        average = total / len(marks)

        result = "PASS" if average >= 40 else "FAIL"

        print("\n" + "=" * 40)
        print("          ACADEMIC REPORT")
        print("=" * 40)

        print(
            f"Student Name : {student['Name']} "
            f"(Roll: {roll})"
        )
        print("Branch       :", student["Branch"])
        print("Semester     :", student["Semester"])
        print("Subject Marks:", marks)
        print(f"Total Marks  : {total} / 300")
        print(f"Average Marks: {average:.2f}%")
        print(f"Final Result : {result}")

        print("=" * 40)

    except ValueError:
        print("Invalid input! Enter a valid Roll Number.")


# 6. Delete Student Record
def delete_student():
    try:
        roll = int(input("Enter Roll Number to delete: "))

        removed_student = students.pop(roll, None)

        if removed_student is not None:
            print(
                f"\n[SUCCESS] Record for "
                f"'{removed_student['Name']}' "
                f"(Roll No: {roll}) deleted successfully."
            )
        else:
            print("[ERROR] Student record not found.")

    except ValueError:
        print("Invalid input! Enter a valid Roll Number.")


# Main Menu
def main():
    while True:
        print("\n" + "=" * 45)
        print("   STUDENT INFORMATION MANAGEMENT SYSTEM")
        print("=" * 45)

        print("\nSelect an operation:")
        print("1. View All Students")
        print("2. Search Student by Roll Number")
        print("3. Register New Student")
        print("4. Update Student Details")
        print("5. View Academic Performance")
        print("6. Delete Student Record")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            view_all_students()

        elif choice == "2":
            search_student()

        elif choice == "3":
            register_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            view_academic_performance()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            print(
                "\nThank you for using Student "
                "Information System. Goodbye!"
            )
            break

        else:
            print("[ERROR] Invalid choice! Please select 1-7.")


# Execute Program
if __name__ == "__main__":
    main()