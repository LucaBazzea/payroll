class Payroll:

    def __init__(self, employeeName, employeeID, salary):

        self.employeeName = employeeName
        self.employeeID = employeeID
        self.salary = salary

    def DisplayInfo(self):

        print(f"Name: {self.employeeName}\tID: {self.employeeID}\tSalary: {self.salary}")

    