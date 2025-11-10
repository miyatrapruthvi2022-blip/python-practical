#reate a program name “employee.py” and implement the functions DA, HRA, PF, and ITAX. Create another 
#program that uses the function of employee module and calculates gross and net salaries of an employee 
# employee.py

def da(basic):
    return basic * 0.10   # 10% DA

def hra(basic):
    return basic * 0.20   # 20% HRA

def pf(basic):
    return basic * 0.12   # 12% PF

def itax(gross):
    return gross * 0.05   # 5% Income Tax
