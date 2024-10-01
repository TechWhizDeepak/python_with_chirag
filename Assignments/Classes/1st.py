class Car:
    def __init__(self,car_brand, car_colour, car_price, maximum_speed):
        self.car_brand = car_brand
        self.car_colour = car_colour
        self.car_price = car_price
        self.maximum_speed = maximum_speed

    def car_names(self):
        print(f"So you car brand is {self.car_brand} and your car colour is {self.car_colour}!!\n You will pay {self.car_price} for this and you will get maximum speed of {self.maximum_speed} ")

    def car_loan(self):
        user_asked_loan = int(input("Please enter the loan amount you want: "))
        maximum_loan = self.car_price * 70 / 100
        if user_asked_loan >= maximum_loan:
            print(f"No, We cannot give you loan!! You are only elibile for {maximum_loan}")
        else:
            print("Congrts!! we will provide you the loan")

#Audi = Car("Audi", "Black", "150000", "250MPH")
#print(Audi.car_brand,Audi.car_colour,Audi.car_price, Audi.maximum_speed)

Audi = Car("Audi", "Black", 150000, "250MPH")
Audi.car_names()
Audi.car_loan()

