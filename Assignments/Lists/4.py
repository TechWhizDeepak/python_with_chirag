'''
Write a Python program to get the largest number from a list.
'''
def find_largest_number(listA):
    big_number = 0
    for i in listA:
        if i >= big_number:
            big_number = i
    print(big_number) 

lst=[5,1,2,3,4,6]
results = find_largest_number(lst)
print(results)