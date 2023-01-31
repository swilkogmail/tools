#!/usr/bin/python3
class Vehicle:
    """
    Vehicle is a type that helps us travel
    """

    default_tyre = 'tyre'

    def __init__(self, engine, tyres):
        """
        Cusomizes the initialization of the object
        """
        self.engine = engine
        self.tyres = tyres

    # this is a decorator - commented out so we can put it
    # into the Bycle class and demonstrate inheritance
    # @classmethod
    # def bicycle(cls, tyres=None):
    #     if not tyres:
    #         tyres = [cls.default_tyre, cls.default_tyre]
    #     return cls(None, tyres)


    def description(self):
        print(f"A vehicle with an {self.engine} and {self.tyres}")

car = Vehicle('4-cylinder',[1,2,3,4])
print(car.engine)
print(car.tyres)
# bike = Vehicle.bicycle()
# print(bike.engine)
# print(bike.tyres)
# bike = Vehicle.bicycle([1,2])
# print(bike.engine)
# print(bike.tyres)