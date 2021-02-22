class Date:

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    def DisplayDate(self):

        return(f"{self.day}/{self.month}/{self.year}")

class Employee:

    def __init__(self, firstName, lastName, DOB, employeeID, employmentDate):

        self.firstName = firstName
        self.lastName = lastName
        self.DOB = Date(DOB["Day"], DOB["Month"], DOB["Year"])
        self.employeeID = employeeID
        self.employmentDate = Date(employmentDate["Day"], employmentDate["Month"], employmentDate["Year"])

    def DisplayEmployee(self):

        print(" Name: " + self.firstName + " " + self.lastName + " DOB: " + self.DOB.DisplayDate() + " ID: " + str(self.employeeID))

class HourlyEmployee(Employee):

    def __init__(self, hourlyRate, firstName, lastName, DOB, employeeID, employmentDate):
        Employee.__init__(self, firstName, lastName, DOB, employeeID, employmentDate)

        self.hourlyRate = hourlyRate

    def DisplayHourlyEmployee(self):

        print(self.DisplayEmployee() + "Hourly Rate:" + str(self.hourlyRate))

    def SalaryPerMonth(self):

        salaryPerMonth = self.hourlyRate * 180

        return salaryPerMonth

class MonthlyEmployee(Employee):

    def __init__(self, MonthlySalary, firstName, lastName, DOB, employeeID, employmentDate):
        Employee.__init__(self, firstName, lastName, DOB, employeeID, employmentDate)

        self.MonthlySalary = MonthlySalary

    def DisplayMonthlyEmployee(self):

        print(self.DisplayEmployee() + "Monthly Salary:" + str(self.MonthlySalary))

    def SalaryPerMonth(self):

        return self.MonthlySalary

