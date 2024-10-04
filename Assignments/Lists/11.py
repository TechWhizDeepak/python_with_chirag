'''
 Write a Python program to find the second smallest number in a list.
'''

def find_the_second_smallest_number(listA):
    smallest_number = float('inf')
    second_smallest_number = float('inf')
    for i in listA:
        if i < smallest_number:
                second_smallest_number = smallest_number
                smallest_number = i
        elif smallest_number < i < second_smallest_number:
             second_smallest_number = i
    return second_smallest_number

lst=[5,2,3,4,6,9,11,13,56,8]
results = find_the_second_smallest_number(lst)
print(results)
    


