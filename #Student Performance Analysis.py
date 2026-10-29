#Student Performance Analysis
exam1 = int(input("Enter first exam marks: "))
exam2 = int(input("Enter second exam marks: "))

difference = exam2 - exam1

if difference > 0:
    print("Performance Improved")
    print("Improvement:", difference)

elif difference < 0:
    print("Performance Decreased")
    print("Decrease:", -difference)

else:
    print("Performance Remained Same")
