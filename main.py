class Payroll:

    def __init__(self, firstName, secondName, DOB, employeeID, employmentDate, salary):

        self.firstName = firstName
        self.secondName = secondName
        self.DOB = DOB
        self.employeeID = employeeID
        self.employmentDate = employmentDate

class HourlyPay(Payroll):

    def __init__(self, hourlyRate):

        self.hourlyRate = hourlyRate

    def Salary(self, salary):

        self.salary = salary

        salary = self.hourlyRate * 180

class Date:

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

class Display(Payroll):

    def DisplayInfo(self):

        print(f"Name: {self.firstName} {self.secondName}\nDOB: {self.DOB}\nID: {self.employeeID}\nEmployment Date: {self.employmentDate}\nSalary: {self.salary}")