'''
Write a Python function that returns whether the number is prime or not.
'''

def check_if_number_is_prime(number):
    if number <= 1:
        print("The number is not prime!!")
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime!!")
            return
    print("This is a prime number")



a = int(input("Please enter a number: "))
result = check_if_number_is_prime(a)