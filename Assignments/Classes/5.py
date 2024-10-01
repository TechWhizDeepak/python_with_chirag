'''
Create class Person add Details First_name,Last_name,Age and 
Then add Method to return all details in dict 
'''

class Person:
    def __init__(self,First_name,Last_name,Age):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
    
    def print_all_detail(self) -> dict:
        return {self.First_name, self.Last_name,self.Age}

Person_details = Person("Deepak", "Kumar", 31)
print(Person.print_all_detail(Person_details))
print(type(Person.print_all_detail(Person_details)))
