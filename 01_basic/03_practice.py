# Object Oriented Programming
class Car:

    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1


    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_type(self):
        return "Petrol or Diesel"

    @staticmethod  #---> Decorator
    def general_description():
        return "Car are means of transport"   

    @property
    def model(self):
        return self.__model 


    
class ElectricCar(Car):
    def __init__(self, __brand, model,Battery_Size):
        super().__init__(__brand, model)
        self.Battery_Size = Battery_Size


    def full_type(self):
        return "Electric Charge" 


safari = Car("TATA","Safari")
safari_2 = Car("TATA","Nexon")
print(safari.full_type())


# my_Tesla = ElectricCar("Tesla","Model S","85KWH")

# print(isinstance(my_Tesla,Car))    #----> isinstance()
# print(isinstance(my_Tesla,ElectricCar))
#  print(my_Tesla.brand)
# print(my_Tesla.model)
# print(my_Tesla.Battery_Size)
# print(my_Tesla.full_name()) 
# print(my_Tesla.get_brand())
# print(my_Tesla.full_type())

# my_Car = Car("Toyota","Corolla")

#  print(my_Car.brand)
# print(my_Car.model) 
# print(my_Car.full_name()) 


# my_new_Car = Car("TATA","Safari")

# my_new_Car.model = "City"
# # print(my_new_Car.brand)
# print(my_new_Car.model)



# print(Car.total_car)
# print(Car.general_description())
# print(my_Car.model)


# Multiple Inheritance 
class Battery:
    def battery_info(self):
        return "This is Battery"
    
class Engine:
    def Engine_info(self):
        return "This is Engine"

class ElectricCar_2(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar_2("Tesla","Model A")

print(my_new_tesla.battery_info())
print(my_new_tesla.Engine_info())