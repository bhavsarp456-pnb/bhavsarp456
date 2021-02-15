#2.	Define a class Employee with instance variables empid, name, salary.
# Define constructor to initialize member variables. Define function to show employee data.
class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    @property
    def employee(self):
        return f"{self.empid}-{self.name}-{self.salary}"

Ayush = Employee("7523", "Ayush", "25000")
print(f"{Ayush.empid}-{Ayush.name}-{Ayush.salary}")