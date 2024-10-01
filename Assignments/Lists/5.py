'''
Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

def check_the_string_data(listA):
    total_count = 0
    for i in listA:
        if len(i) > 2 and  i[0] == i[-1]:
            total_count += 1
    return total_count   
            
lst=['abc', 'xyz', 'aba', '1221','aaab']
results = check_the_string_data(lst)
print(results)