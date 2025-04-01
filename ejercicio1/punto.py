
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está en el origen"
        elif self.x == 0:
            return "Está sobre el eje Y"
        elif self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"

    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)
