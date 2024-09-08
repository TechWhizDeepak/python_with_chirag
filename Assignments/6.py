'''
Write a program to find the simple Interest.
'''

principle_amount = float(input("Please enter total amount: "))
interest_rate = float(input("Please enter the interest rate: "))
time_of_period = float(input("Please enter the total years: "))

simple_interest = principle_amount * interest_rate * time_of_period / 100
print("Total simple interest on your principle is: ", simple_interest)