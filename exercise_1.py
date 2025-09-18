from abc import ABC, abstractmethod

class Shape3D(ABC):  # Task 1


    @ abstractmethod
    def volume(self):
        pass

    @ abstractmethod
    def surface_area(self):
        pass

    def describe(self):
        print('I am a 3D shape.')


# Task 2
class Cube(Shape3D):


    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * self.side ** 2


class Sphere(Shape3D):


    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return 4 / 3 * 3.14 * self.radius ** 3

    def surface_area(self):
        return 4 * 3.14 * self.radius ** 2


class Cylinder(Shape3D):


    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius ** 2
                + 2 * 3.14 * self.radius * self.height)


# Task 3
shapes = [Cube(2), Sphere(3), Cylinder(2, 5)]

for s in shapes:
    s.describe()
    print("Volume:", s.volume())
    print("Surface area:", s.surface_area())
    print("---")

# (For Task 4) Results are displayed here by comments (#).
# I am a 3D shape.
# Volume: 8
# Surface area: 24
# ---
# I am a 3D shape.
# Volume: 113.03999999999999
# Surface area: 113.04
# ---
# I am a 3D shape.
# Volume: 62.800000000000004
# Surface area: 87.92
# ---