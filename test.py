class Planet(object):
    """Planet """

    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume

    def saymass(self):
        print("Mass: ", self.mass)

    def showdata(self):
        print(f"Info:\n\t-) Masse: {self.mass}\n\t-) Volumen: {self.volume}")


Erde = Planet(50, 100)
Erde.saymass()
print("-------------------------")
Erde.showdata()
