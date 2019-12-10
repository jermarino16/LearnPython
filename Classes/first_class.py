# define the Vehicle class below:

# instantiate a new Vehicle and save it to a variable called car:

# instantiate a new Vehicle and save it to a variable called boat:
class Vehicle:
    def __init__(self, make, model, year):
    	self.make = make
    	self.model = model
    	self.year = year

car = Vehicle("ford", "fiesta", 2099)
boat = Vehicle("big", "boat", 2011)

print(car.make, car.model)
print(boat.make, boat.model)