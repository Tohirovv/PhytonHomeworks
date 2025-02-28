class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        if EmployeeManager.employee_exists(employee.employee_id):
            print("Employee ID already exists. Try again.")
            return
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees(sort_by=None):
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = [line.strip() for line in file.readlines()]
                if not employees:
                    print("No records found.")
                    return
                if sort_by == "name":
                    employees.sort(key=lambda x: x.split(", ")[1])
                elif sort_by == "salary":
                    employees.sort(key=lambda x: float(x.split(", ")[3]))
                print("Employee Records:")
                for emp in employees:
                    print(emp)
        except FileNotFoundError:
            print("No records found.")

    @staticmethod
    def search_employee(employee_id):
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(str(employee_id) + ","):
                        print("Employee Found:")
                        print(line.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = file.readlines()
            with open(EmployeeManager.FILE_NAME, "w") as file:
                updated = False
                for line in employees:
                    data = line.strip().split(", ")
                    if data[0] == str(employee_id):
                        if name:
                            data[1] = name
                        if position:
                            data[2] = position
                        if salary:
                            data[3] = str(salary)
                        line = ", ".join(data) + "\n"
                        updated = True
                    file.write(line)
                if updated:
                    print("Employee updated successfully!")
                else:
                    print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    @staticmethod
    def delete_employee(employee_id):
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = file.readlines()
            with open(EmployeeManager.FILE_NAME, "w") as file:
                found = False
                for line in employees:
                    if not line.startswith(str(employee_id) + ","):
                        file.write(line)
                    else:
                        found = True
                if found:
                    print("Employee deleted successfully!")
                else:
                    print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    @staticmethod
    def employee_exists(employee_id):
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                return any(line.startswith(str(employee_id) + ",") for line in file)
        except FileNotFoundError:
            return False


# Example usage
emp1 = Employee(1001, "John Doe", "Software Engineer", 75000)
EmployeeManager.add_employee(emp1)
EmployeeManager.view_all_employees()
EmployeeManager.search_employee(1001)
EmployeeManager.update_employee(1001, salary=80000)
EmployeeManager.view_all_employees(sort_by="salary")
EmployeeManager.delete_employee(1001)
EmployeeManager.view_all_employees()
