from punto  import Punto
class rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.p1 = punto1
        self.p2 = punto2

    def base(self):
        return abs(self.p2.x - self.p1.x)

    def altura(self):
        return abs(self.p2.y - self.p1.y)

    def area(self):
        return self.base() * self.altura()