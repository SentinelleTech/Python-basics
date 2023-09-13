import math

class Circle:

    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        
        area = math.pi * self.radius * self.radius

        return area