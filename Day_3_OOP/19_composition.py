class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine ({self.horsepower}hp) roars to life."


class GPS:
    def navigate(self, destination):
        return f"Navigating to {destination}..."


class Car:
    """Car HAS-A Engine and HAS-A GPS, instead of inheriting from them."""

    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)   # composition
        self.gps = GPS()                    # composition

    def start(self):
        return f"{self.brand}: {self.engine.start()}"

    def drive_to(self, destination):
        return f"{self.brand}: {self.gps.navigate(destination)}"


car = Car("Honda", 158)
print(car.start())
print(car.drive_to("Ahmedabad"))

# The engine can be swapped independently -- flexibility inheritance doesn't give
car.engine = Engine(300)
print(car.start())