import os

FILE_NAME = "employees.txt"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, 'w').close()

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!")

def view_employees():
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No employee records found.")
        else:
            for record in records:
                print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for record in lines:
            if record.startswith(emp_id + ","):
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                file.write(record)

    if found:
        print("Employee record updated.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for record in lines:
            if not record.startswith(emp_id + ","):
                file.write(record)
            else:
                found = True

    if found:
        print("Employee record deleted.")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
