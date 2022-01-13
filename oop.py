
class Circle():
    pi=3.14

    def __init__(self,radius=0):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def hello():
        return "Aese he Sexy lg rha tha to function me aagya!"

C1 = Circle(2)
print(C1.area())
print(hello())
