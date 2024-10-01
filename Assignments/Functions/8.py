'''
Write a Python function that accepts a string and counts the number of upper and lower case letters. 
a. Sample String : 'The quick Brow Fox' Expected Output : 
b. No. of Uppercase characters : 3 c. No. of Lower case Characters : 12
'''

def string_count(name):
    upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_str = "abcdefghijklmnopqrstuvwxyz"
    upper_total_count = 0
    lower_total_count = 0
    for i in name:
        if i in upper_str:
           upper_total_count += 1
        elif i in lower_str:
            lower_total_count += 1

    return f"No. of Uppercase characters : {upper_total_count} \nNo. of Lower case Characters : {lower_total_count} " 

print(string_count("The quick Brow Fox"))



# def string_count(a: str):
#     upper_case_count = 0
#     for i in a:
#         if i.isupper()==True :
#             upper_case_count+=1
#     lower_case_count = 0
#     for j in a:
#         if j.islower() == True :
#             lower_case_count+=1
#     return f"No. of Uppercase characters : {upper_case_count} \nNo. of Lower case Characters : {lower_case_count} " 
          
# result = string_count("Deepak")

# print(result)