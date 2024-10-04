'''
Write a Python class named Student with two attributes: student_id, student_name. 
Add a new attribute: student_class. 
Create a function to display all attributes and their values in the Student class
'''

class Student:
    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name =student_name

    def student_class(self):
        return f"Student name is : {self.student_name} and his id is: {self.student_id}"
    
Deepak = Student(8, "Deepak Kumar")
print(Deepak.student_class())