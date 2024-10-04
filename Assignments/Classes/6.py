''' Create Class Mytype and Take 5 integer value and then add Function like 
Create function MyString and That function return number String 
Create function My Tuple And return number Tuple 
Create Function MyList and return number List 
Create function My Sets and return number sets '''

class Mytype:
    def __init__(self, first, second, third, forth, fivth):
        self.first = first
        self.second = second
        self.third = third
        self.forth = forth
        self.fivth = fivth

    def MyString(self):
       return f"{self.first} {self.second} {self.third} {self.forth} {self.fivth}"
    
    def Mytuple(self):
        return self.first, self.second, self.third, self.forth, self.fivth
    
    def MyList(self):
        return [self.first, self.second, self.third, self.forth, self.fivth]
    
    def MySet(self):
        return {self.first, self.second, self.third, self.forth, self.fivth}

my_values = Mytype(1,2,3,4,5)
print(type(my_values.MyString()), my_values.MyString())

print(type(my_values.Mytuple()), my_values.Mytuple())

print(type(my_values.MyList()), my_values.MyList())

print(type(my_values.MySet()),my_values.MySet())
