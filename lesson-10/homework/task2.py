import csv
with open("grades.csv", "r") as file:

    reader = csv.DictReader(file)
    grades = [row for row in reader]

subject_grades = {}
for entry in grades:
    subject = entry["Subject"]
    grade = int(entry["Grade"])
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade)

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, avg])
