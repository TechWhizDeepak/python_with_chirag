'''
Write a python Function and check palindrome string or not a. It take one argument string and
return string is palindrome or not
'''

def check_palindrom_string(name: str):
    if name ==  name[::-1]:
        return "It's a palindrome string"
    else:
        return "Not a palindrome string!!"

name_or_string = str(input("Please enter a string or a number: "))
print(check_palindrom_string(name_or_string))