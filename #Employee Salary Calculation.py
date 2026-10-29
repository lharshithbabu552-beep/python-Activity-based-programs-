#Employee Salary Calculation
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))

gross = basic + allowance
net = gross - deduction

print("Gross Salary:", gross)
print("Net Salary:", net)
