'''
Create Car class Add Details 
Create Simple_Car Class and inheritance Car class
Create Sports_Car Class and Inheritance Simple_Car
'''

class Car:
    def __init__(self,brand_name,Model,Colour,Engine_capacity):
        self.brand_name = brand_name
        self.Model = Model
        self.Colour = Colour
        self.Engine_capacity = Engine_capacity

class Simple_Car(Car):
    def __init__(self, brand_name, Model, Colour, Engine_capacity,Simple_facilities):
        super().__init__(brand_name, Model, Colour, Engine_capacity)
        self.Simple_facilities = Simple_facilities

class Sports_Car(Simple_Car):
    def __init__(self,brand_name, Model, Colour, Engine_capacity,Simple_facilities,Special_features):
        super().__init__(brand_name, Model,Colour,Engine_capacity,Simple_facilities)
        self.Special_features = Special_features

Maruti = Simple_Car("Suzuki", "Maruti 800", "White", "1000cc","Radio FM")
Audi = Sports_Car("Audi" ,"Audi-TT", "Black", "3000cc","Radio FM","2x Speed Button")

print(Audi.Special_features)
