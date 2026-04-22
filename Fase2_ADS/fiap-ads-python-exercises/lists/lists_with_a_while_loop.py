#Create a program where the teacher enters an undetermined number of grades and, upon completion, the program displays the arithmetic mean

exam_grade = []

while input("Would you like to enter a grade ? Y - Yes, N no: ").upper() != "N":
    exam_grade.append(float(input("Enter a grade: ")))

average = sum(exam_grade) / len(exam_grade)

print(f"For the typed grades, the average was: {average}")
