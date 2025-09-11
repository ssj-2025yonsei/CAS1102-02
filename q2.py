class Temperature:


    unit = 'Celsius'

    def __init__(self, value):
        self.value = value

    def display(self):
        print(str(self.value) + ' degrees ' + str(self.unit))

    @classmethod

    def change_unit(cls, new_unit):
        cls.unit = new_unit

    @staticmethod

    def to_fahrenheit(celsius):
        return celsius * 1.8 + 32


a = Temperature(100)  # A
b = Temperature(0)  # D
a.display()  # A
print(Temperature.to_fahrenheit(100))  # B
a.change_unit('Kelvin')  # C
a.display()  # C
b.display()  # D
print("Because change_unit command changed the attribute 'unit' "
      "for the whole class.")  # D