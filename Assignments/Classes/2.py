'''
Class Method defining
'''

class Weather:
    @classmethod
    def season(cls,month):
        if month >= 1 and month <= 3:
            print("This is Spring weather")
        elif month >= 4 and month <= 6:
            print("This is Summar weather")
        elif month >= 7 and month <= 9:
            print("This is rainy weather")
        elif month >= 10 and month <= 12:
            print("This is Winters weather")
        else:
            print("Please enter valid month from 1-12")

# Weather.season(14)        


class Laptop:
    @classmethod
    def generate_bill(cls, amount): 
        discount = amount * 30 / 100
        gst =  discount * 18 / 100
        return amount - discount + gst

print(Laptop.generate_bill(100000))
