'''
Write a Program to check the given number is prime or not prime.
'''
a =int(input("Please enter a number: "))

# if a % 1: 
#     print("This is a prime number")
# else:
#     print("This is not a prime number")
#39

#40 2 4 5 

#121 = 11 * 11 

if a > 1 :
    for i in range(2,(a//2)+1): 
        if a%i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")
else:
    print("This is not a prime number")