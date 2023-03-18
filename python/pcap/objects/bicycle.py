#!/usr/bin/python3
from vehicle import Vehicle

#
# as we don't define __init__ we inherit that from the parent class
#
# class Bicycle(Vehicle):
#     pass


class Bicycle(Vehicle):

    default_tyre = 'tyre'

    def __init__(self, tyres=None, distance_traveled=0, unit='miles'):
        # super allows us to call the parent init although
        # this can be overriden by the local one
        # we still want the work from vehicle but we want to do some more
        # it this example we can set distance_traveled and until but out class
        # can set tyre
        super().__init__(distance_traveled, unit)
        if not tyres:
            tyres = [self.default_tyre, self.default_tyre]
        self.tyres = tyres

    def description(self):
        initial = super().description()
        return f"{initial}  on {len(self.tyres)} tyres."
    
    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

bike = Bicycle()
print(bike.tyres)
desc = bike.description()
if __name__ == "__main__":
    bike = Bicycle()
    print(bike.description())