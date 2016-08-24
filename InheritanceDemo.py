"""
This program is just for a demo for inheritance
"""


class Vehicle:
    hp = 0
    power = 0.0
    torque = 0
    fuel_type = 0
    engine = " "

    def __init__(self, hp, power, torque, fuel_type, engine):
        self.engine = engine
        self.hp = hp
        self.fuel_type = fuel_type
        self.power = power
        self.torque = torque

    def display(self):
        pass


class Car(Vehicle):
    __price = 0.0
    __c_o = ""
    __model_no = " "
    __type = " "
    __car_name = ""

    def __init__(self, price, c_o, model_no, name, ty, hp, torque, fuel_type, power, engine):
        self.__price = price
        self.__c_o = c_o
        self.__type = ty
        self.__car_name = name
        self.__model_no = model_no
        super(Car, self).__init__(hp, power, torque, fuel_type, engine)

    def display(self):
        print("Car Name:{0}\nModel No:{1}\nH-P:{2}\nType:{3}\nTorque:{4}\nFuel type:{5}\nEngine:{6}".format(
            self.__car_name, self.__model_no, self.hp, self.torque, self.__type,
            self.fuel_type, self.engine))
C = Car(700000, "India", 56982, "Mercedez S", 320, 180, "Luxury", "Diesel", 250, "Four Stroke")
C.display()
