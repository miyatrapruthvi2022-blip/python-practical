# salary.py

import employee

basic = float(input("Enter basic salary: "))

# Calculate allowances and deductions
da = employee.da(basic)
hra = employee.hra(basic)
pf = employee.pf(basic)

# Gross salary
gross = basic + da + hra

# Income tax
tax = employee.itax(gross)

# Net salary
net = gross - (pf + tax)

print("\n--- Salary Details ---")
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("PF:", pf)
print("Gross Salary:", gross)
print("Income Tax:", tax)
print("Net Salary:", net)
