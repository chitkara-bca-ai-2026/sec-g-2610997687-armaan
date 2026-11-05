print("=" * 40)
print("       SCHOOL RESULT PROCESSING")
print("=" * 40)

# Accept student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks for 5 subjects
marks = []
print("\n--- Enter Marks out of 100 ---")

for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100

# Determine result and grade
if any(mark < 40 for mark in marks):
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"

elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"

else:
    result = "PASS"
    grade = "E"
    remark = "Pass"

# Display student report card
print("\n" + "=" * 40)
print("          STUDENT REPORT CARD")
print("=" * 40)

print("Student Name :", name)
print("Roll Number  :", roll_no)
print("-" * 40)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", f"{percentage:.2f}%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remark)

print("=" * 40)