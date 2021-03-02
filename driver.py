from main import Date, Employee, HourlyEmployee, MonthlyEmployee
from querystrings import registerEmployee, employeeSalary
import sys

def MainMethod():

    while True:

        option = int(input(f"Enter 1 for Monthly employee or 2 for hourly employee"))

        if option == 1:

            try:
                FirstName = input("First Name: ")
            except:
                print("ERROR")
            
            try:
                LastName = input("Last Name: ")
            except:
                print("ERROR")

            DOB = {}
            print("Date of Birth: ")

            try:
                DOB["Day"] = int(input("Day: "))
            except:
                print("ERROR")
            
            try:
                DOB["Month"] = int(input("Month: "))
            except:
                print("ERROR")

            try:
                DOB["Year"] = int(input("Year: "))
            except:
                print("ERROR")

            try:
                EmployeeID = (input("ID: "))
            except:
                print("ERROR")

            EmploymentDate = {}
            print("Date of Employment: ")

            try:
                EmploymentDate["Day"] = int(input("Day: "))
            except:
                print("ERROR")

            try:
                EmploymentDate["Month"] = int(input("Month: "))
            except:
                print("ERROR")

            try:
                EmploymentDate["Year"] = int(input("Year: "))
            except:
                print("ERROR")

            try:
                MonthlySalary = float(input("Monthly Salary: "))
            except:
                print("ERROR")

            Employee1 = MonthlyEmployee(MonthlySalary, FirstName, LastName, DOB, EmployeeID, EmploymentDate)

            Employee1.DisplayEmployee()
            Employee1.installEmployee()

        else:

            try:
                FirstName = input("First Name: ")
            except:
                print("ERROR")
            
            try:
                LastName = input("Last Name: ")
            except:
                print("ERROR")

            DOB = {}
            print("Date of Birth: ")

            try:
                DOB["Day"] = int(input("Day: "))
            except:
                print("ERROR")
            
            try:
                DOB["Month"] = int(input("Month: "))
            except:
                print("ERROR")

            try:
                DOB["Year"] = int(input("Year: "))
            except:
                print("ERROR")

            try:
                EmployeeID = (input("ID: "))
            except:
                print("ERROR")

            EmploymentDate = {}
            print("Date of Employment: ")

            try:
                EmploymentDate["Day"] = int(input("Day: "))
            except:
                print("ERROR")

            try:
                EmploymentDate["Month"] = int(input("Month: "))
            except:
                print("ERROR")

            try:
                EmploymentDate["Year"] = int(input("Year: "))
            except:
                print("ERROR")

            try:
                HourlyRate = float(input("Hourly Rate: "))
            except:
                print("ERROR")

            Employee1 = HourlyEmployee(HourlyRate, FirstName, LastName, DOB, EmployeeID, EmploymentDate)

            Employee1.DisplayEmployee()
            Employee1.installEmployee()

if __name__=="__main__":

    sys.setrecursionlimit(1500)

    MainMethod()

        


