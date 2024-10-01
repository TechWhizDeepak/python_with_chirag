'''
Write a Python program to check if a list is empty or not.
'''

def check_if_list_is_empty(listA):
    if listA:
        print("The list is not empty, it has some data inside.")
    else:
        print("The list is Empty")

lst=[]
results = check_if_list_is_empty(lst)