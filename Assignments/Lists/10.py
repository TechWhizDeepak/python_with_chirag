'''
Write a Python program to append a list to the second list using class and object.
'''

class Apendlist:
    @staticmethod
    def append_two_lists(listA, listB):
        #result =  listA + listB
        listA.extend(listB)
        #return result
        return listA


a = [1,2,4]
b = [4,5,7,9]
c = Apendlist.append_two_lists(a,b)
print(c)