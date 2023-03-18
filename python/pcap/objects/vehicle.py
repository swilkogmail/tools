#!/usr/bin/python3
class Vehicle:
    """
    Vehicle is a type that helps us travel
    """

    def __init__(self, distance_traveled=0, unit='miles'):
        """
        Cusomizes the initialization of the object
        """
        self.distance_traveled = distance_traveled
        self.unit = unit

    def description(self):
        return (f"A {self.__class__.__name__} that has travelled {self.distance_traveled} {self.unit}")

car = Vehicle('32000',['km'])
print(car.distance_traveled)
print(car.unit)
# bike = Vehicle.bicycle()
# print(bike.engine)
# print(bike.tyres)
# bike = Vehicle.bicycle([1,2])
# print(bike.engine)
# print(bike.tyres)