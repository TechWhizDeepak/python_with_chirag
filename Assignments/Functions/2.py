'''
Write a Python function is_even a. It take one argument and return True or False
'''

def is_even(a : int):
    if a % 2 == 0:
        return True
    else:
        return False

number = int(input("Please enter your number: "))
result = is_even(number)
print(result)