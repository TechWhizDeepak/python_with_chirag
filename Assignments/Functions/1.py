'''
Write a Python function to find the Odd Even Number a. It take one argument and return the argument number is odd or Even
'''

def check_odd_even(number :int):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


a = int(input("Please enter your number: "))
check_odd_even(a)