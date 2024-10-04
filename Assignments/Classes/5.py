'''
Create class Person add Details First_name,Last_name,Age and 
Then add Method to return all details in dict 
'''
class Person:
    def __init__(self,First_name,Last_name,Age):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age

Person_details = Person("Deepak", "Kumar", 31)
print(Person_details.__dict__)

