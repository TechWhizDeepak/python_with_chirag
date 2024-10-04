'''
Create One Class  MyList 
Method is Return List 
Method remove duplicate list 
Add data in list
Remove data in list 
'''
class Mylist:
    def __init__(self, listA):
        self.listA = listA

    def Return_list(self):
        return self.listA
    
    def Duplicate_list(self):
        A = []
        for i in self.listA:
            if i not in A:
                A.append(i)
        return A
    
    def Add_data(self, listB):
        self.listA.extend(listB)
        return self.listA
    
    def Delete_data(self):
        self.listA.pop()
        return self.listA

A = [1,3,4,1,6,2,3,5,7,9]
B = Mylist(A)
print(B.Return_list())
print(B.Duplicate_list())
print(B.Add_data([11,13,45,14,29]))
print(B.Delete_data())