'''
Write a Program to check the given year is leap year or not.
'''
year = int(input("Please enter the year: "))


if year < 1000 or year > 9999:
    print("Invalid year")
elif year % 400 == 0 and year % 100 == 0:
    print("It's a Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("It's a Leap Year")
else:
    print("Not a Leap year")