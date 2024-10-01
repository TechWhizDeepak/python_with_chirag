'''
Write a Python program to find the second largest number in a list.
'''

def second_largest_number_finding(listA):
    first_largest = 0
    second_largest = 0
    for i in listA:
        if i > first_largest: #56
           second_largest = first_largest #56
           first_largest = i #nothing
        elif first_largest > i > second_largest:
             second_largest = first_largest
    return second_largest

lst=[5,2,3,4,6,9,11,13,56,8]
results = second_largest_number_finding(lst)
print(results)