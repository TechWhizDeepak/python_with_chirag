'''
Write a Python function reverse string a. It take one argument string and return reverse string
'''

def return_reverse_string(a: str):
    a = a[::-1]
    return a


statement = str(input("Please enter the string you want to reverse: "))
result = return_reverse_string(statement)
print(result)