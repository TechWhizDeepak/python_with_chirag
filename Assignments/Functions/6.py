'''
Write python Function to find the length of string a. It can take one argument 
string and return count of char in string
note:Not using built-in len()
'''

def count_length(a: str):
    count = 0
    for i in a:
        count+=1
    return count

result = str(input("Please enter your string for length check: "))
print(count_length(result))



