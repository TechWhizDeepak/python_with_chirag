'''
Write a Python program to find the list of words that are longer than n from a given list of words.
'''

def check_words_longer_than_input_number(listA, n):
    total = []
    for i in listA:
        if len(i) >= n:
            total.append(i)
    return total

fruits =['Banana', 'Mango', 'Apple', 'Pineapple', "Pear", "Lichi"]
results = check_words_longer_than_input_number(fruits, 5)
print(results)