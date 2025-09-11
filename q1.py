class Vector:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __mul__(self, scalar):  # B
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(1, 2)  # A
v2 = Vector(3, 4)  # A
print(v1 + v2)  # A
print(v1 - v2)  # A
print(v1 == v2)  # A
print(v1 * 2)  # B
print(v2 * 3)  # B