'''
Write a Python program to convert a tuple to a string using class object
'''

class Convert_Tuple:
    def __init__(self,tupleA):
        self.tupleA = tupleA
    
    def convert_tuple_to_string(self):
        return_tuple_string = ""
        for i in self.tupleA:
            return_tuple_string += str(i)
        return return_tuple_string

values = (1,4,"Deepak", "Chirag")
a = Convert_Tuple(values)
print(a.convert_tuple_to_string())
print(type(a.convert_tuple_to_string()))

