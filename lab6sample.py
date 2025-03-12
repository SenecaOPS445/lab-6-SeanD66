#!/usr/bin/env python 3

from lab6a import Student

student1 = Student('Jack', 931686102)

student1.addGrade('ops535', 2.0)

student1.addGrade('win310', 1.0)

student1.displayStudent()
# Will print: 'Student Name: Jack\nStudent Number: 931686102'
#print(student1.displayStudent())
student1.displayGPA()
# Will print: 'GPA of student Jack is 1.0'
#print(student1.displayGPA())

student1.displayCourses()
print(student1.displayCourses())
# Will print: ['ops535']

student2 = Student('Jen', 987654321)

student2.addGrade('ops445', 3.0)

student2.displayGPA()
# Will print: 'GPA of student Jen is 0.0'

student2.displayCourses()
# Will print: []