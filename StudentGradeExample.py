grade1 = float(input("Type the grade of the first test: "))
grade2 = float(input("Type the grade of the first test: "))
absences = int(input("Type number of absences: "))
total_classes = int(input("Type total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendences = (total_classes - absences) / total_classes

print("Average grade:", round(avg_grade,2) )
print("Attendance rate: ", str(round(attendences*100, 2)) + "%")

if(avg_grade >= 6):
    if(attendences >= 0.8):
        print("Student was approved")
    else:
        print("The student has failed due to attendance rate lower then 80%")
elif(attendences >= 0.8):
    print("The student has failed due to an average grade lower than 6.0")
else:
    print("The student has failed due to attendance rate lower then 80% and an attendance rate lower than 80% ")