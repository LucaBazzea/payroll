from querystrings import registerEmployee, employeeSalary
import MySQLdb

class Date:

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    def DisplayDate(self):

        return(str(self.day) + "/" + str(self.month) + "/" + str(self.year))

class Employee:

    def __init__(self, firstName, lastName, DOB, employeeID, employmentDate):

        self.firstName = firstName
        self.lastName = lastName
        self.DOB = Date(DOB["Day"], DOB["Month"], DOB["Year"])
        self.employeeID = employeeID
        self.employmentDate = Date(employmentDate["Day"], employmentDate["Month"], employmentDate["Year"])

    def DisplayEmployee(self):

        print("Name: " + self.firstName + " " + self.lastName + " DOB: " + self.DOB.DisplayDate() + " ID: " + str(self.employeeID))

    # Uploads data captured from driver.py
    def installEmployee(self):

        try:
            sql = "INSERT INTO employee(ID, firstName, lastName, DOB, employDate) VALUES(%s, %s, %s, %s, %s)"
            values = (self.employeeID, self.firstName, self.lastName, self.DOB, self.employmentDate)
            connect = MySQLdb.connect(db = "xeenlo",user = "root",password = "")
            cursor = connect.cursor()
            cursor.execute(sql, values)
            connect.commit()

        except Exception as e: 
            print(e)
            print("ERROR failed to connect to database")
    

class HourlyEmployee(Employee):

    def __init__(self, hourlyRate, firstName, lastName, DOB, employeeID, employmentDate):
        Employee.__init__(self, firstName, lastName, DOB, employeeID, employmentDate)

        self.hourlyRate = hourlyRate

    def DisplayHourlyEmployee(self):

        print(self.DisplayEmployee() + "Hourly Rate:" + str(self.hourlyRate))

    def SalaryPerMonth(self):

        salaryPerMonth = self.hourlyRate * 180

        return salaryPerMonth

    #def installEmployee(self):

       # Employee.installEmployee(self)

        # try:
        #     connect = MySQLdb.connect(db = "xeenlo",user = "root",password = "")
        #     cursor = connect.cursor()
        #     cursor.execute(employeeSalary.format(self.employeeID, self.hourlyRate))

        # except:
        #     print("ERROR failed to connect to database")


class MonthlyEmployee(Employee):

    def __init__(self, MonthlySalary, firstName, lastName, DOB, employeeID, employmentDate):
        Employee.__init__(self, firstName, lastName, DOB, employeeID, employmentDate)

        self.MonthlySalary = MonthlySalary

    def DisplayMonthlyEmployee(self):

        print(self.DisplayEmployee() + "Monthly Salary:" + str(self.MonthlySalary))

    def SalaryPerMonth(self):

        return self.MonthlySalary

    # def installEmployee(self):

    #     Employee.installEmployee(self)

        # try:
        #     connect = MySQLdb.connect(db = "xeenlo",user = "root",password = "")
        #     cursor = connect.cursor()
        #     cursor.execute(employeeSalary.format(self.employeeID, self.MonthlySalary))

        # except:
        #     print("ERROR failed to connect to database")""" 

