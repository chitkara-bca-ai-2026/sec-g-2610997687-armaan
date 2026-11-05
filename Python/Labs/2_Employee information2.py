name = input("Enter Employee Name: ")
print("Data type:", type(name))

employee_id = int(input("Enter Employee ID: "))
print("Data type:", type(employee_id))

salary = float(input("Enter Salary: "))
print("Data type:", type(salary))

department = input("Enter Department: ")
print("Data type:", type(department))

active_input = input("Is the employee active? (yes/no): ")
active = active_input.lower() == "yes"
print("Data type:", type(active))

print("\n--- Employee Details ---")
print("Name       :", name)
print("ID         :", employee_id)
print("Salary     :", salary)
print("Department :", department)
print("Active     :", active)