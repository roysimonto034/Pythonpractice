from abc import ABC, abstractmethod


class Polymorph:

    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    @abstractmethod
    def area(self):
        pass


class Circle(Polymorph):
    def __init__(self, radius, length=0, width=0):
        super().__init__(length, width, radius)

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Polymorph):

    def __init(self, length, width, radius=0):
        super().__init__(length, width, radius)

    def area(self):
        return self.length * self.width


cr = Circle(5)
print(cr.area())
cr.radius
rc = Rectangle(5, 10, 8)
rc.area()