'''
Write a Python program to multiply all the items in a list.
'''

def multiply_all_items_list(listA):
    total = 1
    for i in listA:
        total = i * total
    return total

lst=[1,2,3,4]
results = multiply_all_items_list(lst)
print(results)