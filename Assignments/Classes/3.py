'''
Create Class Mobile and take value Like Model_name,brand_name,price,
And add Method
Print Bill()
	Add All Mobile Details With price 18% GST and Discount price also calculated .
Using Instance Method 
Using Class Method print How much mobile cell
If i need to check mobile stock it return list of mobile are available 
'''
class Mobile: 
    in_stock = {"Apple": 10, "Samsung": 5, "Xiaomi" : 8}
    out_stock = {"Apple": 5, "Samsung": 0, "Xiaomi" : 0}
    total_stock = {}

    def __init__(self,model_name,brand_name,price):
        self.model_name = model_name
        self.brand_name = brand_name
        self.price = price
   
    def print_bill(self):
        discount = self.price * .20
        GST = (self.price - discount) * .18
        Mobile.out_stock[self.brand_name]+=1
        return f'''
#Receipt No: 1
#Model_name: {self.model_name}
#Brand_name: {self.brand_name}
Basic Price : {self.price}
Discount : {discount}
GST : {GST}
Total Price : {self.price - discount + GST}
'''
    @classmethod
    def total_inventory(cls):
        for key,value in cls.in_stock.items():
            for i,j in cls.out_stock.items():
                if key == i:
                    cls.total_stock[key] = value - j
        return cls.total_stock


Apple = Mobile("Iphone 16 Pro Max", "Apple",140000)
Samsung = Mobile("Samsung S23+", "Samsung",130000)
Xiaomi = Mobile("Chinese Phone 1 ", "Xiaomi",10000)

print(Apple.print_bill())
print(Samsung.print_bill())
print(Xiaomi.print_bill())
print(Mobile.total_inventory())
