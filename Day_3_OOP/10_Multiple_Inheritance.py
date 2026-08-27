# 10_Multiple_Inheritance
class Flyable:
    def move(self):
        return "flies through the air"


class Swimmable:
    def move(self):
        return "swims through water"


class Duck(Flyable, Swimmable):
    """Multiple inheritance -- Duck can both fly and swim."""
    pass


d = Duck()
print(d.move())  # Which move() wins? Determined by MRO.
print([c.__name__ for c in Duck.__mro__])


# Classic Diamond Problem, resolved via C3 linearization (MRO)
class Base:
    def greet(self):
        return "Base greet"


class Left(Base):
    def greet(self):
        return "Left greet -> " + super().greet()


class Right(Base):
    def greet(self):
        return "Right greet -> " + super().greet()


class Diamond(Left, Right):
    def greet(self):
        return "Diamond greet -> " + super().greet()


print(Diamond().greet())
print([c.__name__ for c in Diamond.__mro__])