'''
Write a program to calculate sum of 5 subjects & find the percentage.
Subject marks entered by user.
'''
math = float(input("Hi, Let's start checking your total grades!! \n Please enter your Math's score out of 100: "))
science = float(input("Please enter your Science's score out of 100: "))
history = float(input("Please enter your History's score out of 100: "))
english = float(input("Please enter your English's score out of 100: "))
computers = float(input("Please enter your Computer's score out of 100: "))

total_score = math + science + history + english + computers
print("Your total score from 500 is: ", total_score)
print(f"You have got {total_score / 5 }% score out of 100 ")
