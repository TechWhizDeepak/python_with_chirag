'''
Write a Python program to sum all the items in a list.
'''

def sum_of_the_list(listA):
    total = 0
    for i in listA:
        total =  i + total 
    return total


lst=[1,2,3]
results = sum_of_the_list(lst)
print(results)