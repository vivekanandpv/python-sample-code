from py_18_class import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    #   all instance methods are virtual by default
    def drive(self):
        print(f'Car: {self.make}/{self.model}/{self.year} is driving...')


car_1 = Car('Mercedes', 'C250D', 2016)
car_1.drive()

print(isinstance(car_1, Car))
print(isinstance(car_1, Vehicle))   # car is a Vehicle
