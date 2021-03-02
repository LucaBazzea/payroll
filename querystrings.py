registerEmployee = """ 
INSERT INTO employee(ID, firstName, lastName, DOB, employDate)
VALUES """

employeeSalary = """ 
INSERT INTO salary(ID, salary)
VALUES ({0}, {1})
"""