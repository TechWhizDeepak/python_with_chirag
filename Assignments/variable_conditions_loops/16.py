'''
Write a program user enter the 5 subjects mark. You have to make a total
and find the percentage.
percentage > 75 you have to print “Distinction”
percentage > 60 and percentage <= 75 you have to print “First class” 
percentage >50 and percentage <= 60 you have to print “Second class” 
percentage > 35 and percentage <= 50 you have to print “Pass class” 
Otherwise print “Fail”

'''

math = float(input("Enter Math's score out of 100: "))
science = float(input("Enter Science's score out of 100: "))
history = float(input("Enter History's score out of 100: "))
english = float(input("Enter English's score out of 100: "))
computers = float(input("Enter Computer's score out of 100: "))

total_percentage = (math + science + history + english + computers) / 5

if total_percentage > 75:
    print(f"Distinction, with {total_percentage}% marks!!")
elif total_percentage > 60 and total_percentage <= 75:
    print(f"First Class with {total_percentage}% marks!!") 
elif total_percentage > 50 and total_percentage <= 60:
    print(f"Second Class, with {total_percentage}% marks!!") 
elif total_percentage > 35 and total_percentage <= 50:
    print(f"Third Class, with {total_percentage}% marks!!")
else:
    print(f"You are Fail, try again next year")