'''
Write a Python function to calculate the factorial of a number
 (a non-negative integer). The function accepts the number as an argument. a. It take one number argument and 
return of factorial b. If a negative number is received then return an Error message
'''

def check_factorial(a: int):
    if a < 0:
        print("Please enter valid number")
    else:
        total = 1
        for i in range(1, a + 1):
            total = total * i 
        print(total)
            

input_number = int(input("Please enter a number: ")) 
check_factorial(input_number)