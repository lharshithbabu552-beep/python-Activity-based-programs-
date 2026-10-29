#Student Marks Matrix
marks = []

for i in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", max(marks))


