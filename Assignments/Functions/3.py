'''
It take one argument and return True or False 3. Write a python function is_Odd
a. It take one argument and return True or False
'''

def is_odd(a : int):
    if a % 2 != 0:
        return True
    else:
        return False

number = int(input("Please enter your number: "))
result = is_odd(number)
print(result)