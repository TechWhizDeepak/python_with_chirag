'''
Create old_car class and inherit  in new_car class
Add Method car_bill
Add method car_loan_elgiblity 
Add Method Car_insurance Details 
'''

class Old_Car:
    def __init__(self,car_brand,car_model,car_colour,car_price):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_colour = car_colour
        self.car_price = car_price


class New_car(Old_Car):
    def __init__(self, car_brand, car_model, car_colour, car_price):
        super().__init__(car_brand, car_model, car_colour, car_price)
    
    def Car_loan(self):
        eligible_loan_amount = self.car_price * .70 
        return eligible_loan_amount
    
    def Car_insurance(self):
        insurance_amount = self.car_price * .10
        insurance_coverage = ["Engine","Wind Shield", "Gearbox"]
        return insurance_amount,insurance_coverage

    def Car_bill(self):
      insurance_amount, insurance_coverage = self.Car_insurance()
      bill =   f'''
        #Car Brand               : {self.car_brand}
        #Car Model               : {self.car_model}
        #Car Colour              : {self.car_colour}
        #Car Basic Price         : {self.car_price}
        #Eligible Loan Amount    : {Car1.Car_loan()}
        #Insurance Amount        : {insurance_amount}
        #Insurance Coverage      : {insurance_coverage}
        '''
      
      return bill
        
        
Car1 = New_car("Audi" ,"Audi-TT", "Black", 100000)
print(Car1.Car_bill())

    