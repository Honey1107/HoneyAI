# 07_Class_Methods
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"{self.brand} {self.model}"

    def start_engine(self):
        return "Engine starting..."


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)   # reuse the parent's init
        self.num_doors = num_doors

    def start_engine(self):              # override
        base = super().start_engine()    # extend, don't fully replace
        return f"{base} Car engine ready with {self.num_doors} doors."


class ElectricCar(Car):
    def __init__(self, brand, model, num_doors, battery_kwh):
        super().__init__(brand, model, num_doors)
        self.battery_kwh = battery_kwh

    def start_engine(self):
        return f"{self.describe()} silently powers on. Battery: {self.battery_kwh}kWh."


vehicles = [
    Vehicle("Generic", "Engine-X"),
    Car("Toyota", "Corolla", 4),
    ElectricCar("Tesla", "Model 3", 4, 75),
]

for v in vehicles:
    print(v.describe(), "->", v.start_engine())

print()
print("ElectricCar MRO:", [c.__name__ for c in ElectricCar.__mro__])
tesla = vehicles[2]
print(isinstance(tesla, Car), isinstance(tesla, Vehicle), isinstance(tesla, ElectricCar))