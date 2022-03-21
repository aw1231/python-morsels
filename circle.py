from math import pi
class Circle:
    def __init__(self,radius=1) -> None:
        self.radius = radius
    def __str__(self) -> str:
        return "Circle(" + str(self.radius) + ")"
    def __repr__(self) -> str:
        return "Circle(" + str(self.radius) + ")"
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return pi * self.radius ** 2
