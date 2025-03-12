#!/usr/bin/env python 3

from student import Student # importing Student class from student.py script

# Creates an instance of the Student class, it will be separate from all other objects created with the Student class:
student1 = Student('John', '013454900') ## creating an instance/object student1 is equal to the class Student(John and its id no.)
student2 = Student('Jessica', '023384103')
# student3 is the object, Student is the class name, 'Jen' is the first argument passed to __init__, '034686901' is the second argument passed to init.
student3 = Student('Jen', '034686901')

# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

student3.addGrade('ops445', 3.0)
student3.addGrade('mst400', 3.5)
#print(student1.name)
#print(student1.courses)
#print(student2.name)
#print(student2.courses)

#print(student1.name) 
#print(student1.number)
#print(student1.courses)
#student1.displayStudent()

#print(student2.name)
#print(student2.number)
#print(student2.courses)
#student2.displayStudent()

# student1.name is a string like any other
print(student3.name)
#student1.name = 'Jack'
print(student3.courses)
print(len(student1.name))
#student3.displayStudent()