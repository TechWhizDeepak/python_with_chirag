'''
Write a Python program to convert a list of characters into a string
'''

def convert_from_list_to_string(listA):
    stringA = ""
    for i in listA:
        stringA += str(i)
    return stringA

values = (1,4,"Deepak", "Chirag")
a = convert_from_list_to_string(values)
print(a)
