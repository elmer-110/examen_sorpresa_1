from punto import Punto
from vector import Vector   
class lanzador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    otro_punto = Punto(7, 10)
    vector_resultante = Punto.vector(otro_punto)
    print(f"Vector resultante: {vector_resultante}")
    def distancia(self, otro_punto):
        otro_punto = Punto(6, 9)
        distancia = punto.distancia(otro_punto)
    print(f"La distancia entre los puntos es: {distancia}")
     
  
punto = Punto(3, -4)
print(punto.cuadrante())