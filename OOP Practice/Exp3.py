#3.	Using class Employee (Que 2), create a list of employees (data taken from user),
# and display list of employees in sorted order according to their names.
# Also define a function to sort list of employees according to their salary in descending order.
class Employee:
    def __init__(self, employees, salary):
        self.employees = employees
        self.salary = salary
        
    @property
    def employee(self):
        return f"{self.employees} - {self.salary}"
    
    @employee.setter
    def emp_salary(self, new_employees, new_salary):
        self.employees = new_employees
        self.salary = new_salary

BAPS = eval(input("Enter the employers list:"))
Salary = eval(input("Enter the salary:"))

Company = Employee(BAPS,Salary)

print(sorted(Company.employees), sorted(Company.salary, reverse=True))