'''
Write a python Function and check palindrome string or not a. It take one argument string and return string is palindrome or not
'''

def check_palindrom_string(name: str):
    if name ==  name[::-1]:
        print("It's a palindrome string")
    else:
        print("Not a palindrome string!!")

name_or_string = str(input("Please enter a string or a number: "))

result = check_palindrom_string(name_or_string)