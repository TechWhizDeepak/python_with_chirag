'''
Write a Python Program to remove Duplicate value in List
lst=[1,2,3,4,5,6,5,4,5,6,7,8,5,2,5,6,7,2,3,4,5,1,4,4,9,0,4,2,5]
'''

def remove_duplicate(listA):
    a = []
    for i in listA:
        if i not in a:
            a.append(i)
    return a


lst=[1,2,3,4,5,6,5,4,5,6,7,8,5,2,5,6,7,2,3,4,5,1,4,4,9,0,4,2,5]
results = remove_duplicate(lst)
print(results)