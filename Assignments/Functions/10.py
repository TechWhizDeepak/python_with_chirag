'''
Write a Python function that accepts a number and returns it total.
Like input is 1286 and function return 17
Like 1+2+8+6=17
'''

def add_number(number):
    total = 0
    for i in str(number):
       total += int(i) 
    print(total) 


add_number(123456)
