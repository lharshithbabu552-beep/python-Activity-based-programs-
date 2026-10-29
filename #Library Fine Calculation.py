#Library Fine Calculation
days = int(input("Enter late days: "))

if days <= 0:
    fine = 0
else:
    fine = days * 2

print("Library Fine: Rs.", fine)
