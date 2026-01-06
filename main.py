from employee import Employee
from database import create_table
from operations import add_employee, view_employees, update_employee, delete_employee, search_employee

create_table()

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Search Employee by ID")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            emp_id = int(input("ID: "))
            name = input("Name: ")
            role = input("Role: ")
            salary = float(input("Salary: "))

            emp = Employee(emp_id, name, role, salary)
            add_employee(emp)
            print("Employee added successfully.")

        except ValueError:
            print("Invalid input. ID and Salary must be numbers.")

    elif choice == "2":
        employees = view_employees()
        if not employees:
            print("No employees found.")
        else:
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Role: {emp[2]}, Salary: {emp[3]}")

    elif choice == "3":
        try:
            emp_id = int(input("Enter Employee ID: "))
            salary = float(input("Enter New Salary: "))

            update_employee(emp_id, salary)
            print("Employee salary updated.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == "4":
        try:
            emp_id = int(input("Enter Employee ID to delete: "))
            delete_employee(emp_id)
            print("Employee deleted.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    elif choice == "5":
        try:
            emp_id = int(input("Enter Employee ID to search: "))
            emp = search_employee(emp_id)

            if emp:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Role: {emp[2]}, Salary: {emp[3]}")
            else:
                print("Employee not found.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")


    elif choice == "6":
        print("Exiting...")
        break
