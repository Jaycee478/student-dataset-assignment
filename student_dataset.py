"""
ASSIGNMENT TWO: STUDENT DATASET CREATION
This program creates a CSV file containing 20 fictional student records.
"""

import csv

students = [
    ["STU001", "Computer Science", 200, 92, 84],
    ["STU002", "Accounting", 100, 85, 76],
    ["STU003", "Mass Communication", 300, 78, 69],
    ["STU004", "Business Administration", 200, 95, 88],
    ["STU005", "Computer Science", 300, 88, 91],
    ["STU006", "Economics", 100, 73, 65],
    ["STU007", "Political Science", 400, 90, 82],
    ["STU008", "Accounting", 300, 81, 74],
    ["STU009", "Microbiology", 200, 96, 89],
    ["STU010", "Computer Science", 100, 67, 71],
    ["STU011", "Biochemistry", 400, 84, 78],
    ["STU012", "Business Administration", 300, 91, 86],
    ["STU013", "Mass Communication", 200, 76, 72],
    ["STU014", "Economics", 300, 89, 80],
    ["STU015", "Computer Science", 400, 98, 94],
    ["STU016", "Political Science", 100, 82, 68],
    ["STU017", "Microbiology", 300, 87, 83],
    ["STU018", "Accounting", 200, 93, 90],
    ["STU019", "Biochemistry", 100, 79, 75],
    ["STU020", "Business Administration", 400, 86, 81],
]

field_names = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(field_names)
    writer.writerows(students)

print("Student dataset created successfully!")
print("Number of fictional students:", len(students))
print("Saved as student_dataset.csv")
