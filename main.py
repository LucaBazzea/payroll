class Payroll:

    def __init__(self, firstName, secondName, employeeID, salary):

        self.firstName = firstName
        self.secondName = secondName
        self.employeeID = employeeID
        self.salary = salary

    def DisplayInfo(self):

        print(f"Name: {self.firstName,self.secondName}\tID: {self.employeeID}\tSalary: {self.salary}")

    