Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Employee Management System

# Step 1 - Data Storage
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Amit", "age": 30, "department": "IT", "salary": 60000},
    103: {"name": "Priya", "age": 25, "department": "Finance", "salary": 55000}
}

# Step 2 - Define Menu System
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the Employee Management System. Goodbye!")
            break
...         else:
...             print("Invalid choice. Please try again.")
... 
... # Step 3 - Add Employee Functionality
... def add_employee():
...     emp_id = int(input("Enter Employee ID: "))
...     if emp_id in employees:
...         print("Employee ID already exists. Please enter a unique ID.")
...         return
... 
...     name = input("Enter Employee Name: ")
...     age = int(input("Enter Employee Age: "))
...     department = input("Enter Employee Department: ")
...     salary = float(input("Enter Employee Salary: "))
... 
...     employees[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}
...     print("Employee added successfully!")
... 
... # Step 4 - View All Employees
... def view_employees():
...     if not employees:
...         print("No employees available.")
...         return
... 
...     print("\nEmployee List:")
...     print(f"{'ID':<10}{'Name':<15}{'Age':<5}{'Department':<15}{'Salary':<10}")
...     print("-" * 55)
... 
...     for emp_id, details in employees.items():
...         print(f"{emp_id:<10}{details['name']:<15}{details['age']:<5}{details['department']:<15}{details['salary']:<10.2f}")
... 
... # Step 5 - Search for Employee by ID
... def search_employee():
...     emp_id = int(input("Enter Employee ID to search: "))
...     if emp_id in employees:
...         details = employees[emp_id]
...         print("\nEmployee Found:")
...         print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']:.2f}")
    else:
        print("Employee not found.")

# Step 6 - Run the Program
if __name__ == "__main__":
    main_menu()
