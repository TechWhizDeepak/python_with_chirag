'''
Write a program to find the Max number from the given three number
using Nested If
'''

a = int(input("Enter the number one: "))
b = int(input("Enter the number two: "))
c = int(input("Enter the number three: "))

if a > b :
    if a > c: 
        print("The maximum number is A:", a)
    else:
        print("Maximum number is C: ", c)
elif b > c:
        print("The maximum number is B:", b)
else:
    print("Maximum number is C: ", c)




