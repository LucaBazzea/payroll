from main import Date, Employee, HourlyEmployee, MonthlyEmployee

def MainMethod():

    while True:

        option = int(input(f"Enter 1 for Monthly employee or 2 for hourly employee"))

        if option == 1:

            FirstName = input("First Name: ")
            LastName = input("Last Name: ")

            DOB = {}
            print("Date of birth: ")
            DOB["Day"] = int(input("Day: "))
            DOB["Month"] = int(input("Month: "))
            DOB["Year"] = int(input("Year: "))

            EmployeeID = (input("ID: "))

            EmploymentDate = {}
            EmploymentDate["Day"] = int(input("Day: "))
            EmploymentDate["Month"] = int(input("Month: "))
            EmploymentDate["Year"] = int(input("Year: "))

            MonthlySalary = float(input("Monthly Salary: "))

            Employee1 = MonthlyEmployee(MonthlySalary, FirstName, LastName, DOB, EmployeeID, EmploymentDate)

            Employee1.DisplayEmployee()

        else:

            FirstName = input("First Name: ")
            LastName = input("Last Name: ")

            DOB = {}
            print("Date of birth: ")
            DOB["Day"] = int(input("Day: "))
            DOB["Month"] = int(input("Month: "))
            DOB["Year"] = int(input("Year: "))

            EmployeeID = (input("ID: "))

            EmploymentDate = {}
            EmploymentDate["Day"] = int(input("Day: "))
            EmploymentDate["Month"] = int(input("Month: "))
            EmploymentDate["Year"] = int(input("Year: "))

            HourlyRate = float(input("Hourly Rate: "))

            Employee1 = HourlyEmployee(HourlyRate, FirstName, LastName, DOB, EmployeeID, EmploymentDate)

            Employee1.DisplayEmployee()

if __name__=="__main__":

    MainMethod()

        


