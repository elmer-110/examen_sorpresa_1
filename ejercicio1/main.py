
from vector import Vector
from rectangulo import Rectangulo
import math
from punto import Punto
if __name__ == "__main__":
    # Trabajando con la clase Punto
    print("=== Clase Punto ===")
    punto1 = Punto(3, 5)
    punto2 = Punto(6, 9)
    print(f"Punto 1: {punto1}")
    print(f"Punto 2: {punto2}")
    print(f"Distancia entre puntos: {punto1.distancia(punto2)}")

    # Trabajando con la clase Vector
    print("\n=== Clase Vector ===")
    vector1 = Vector(1, 2, 3)
    vector2 = Vector(4, 5, 6)
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Suma de vectores: {vector1 + vector2}")
    print(f"Resta de vectores: {vector1 - vector2}")
    print(f"Producto punto: {vector1 * vector2}")
    print(f"Magnitud de Vector 1: {vector1.magnitud()}")

    # Trabajando con la clase Rectangulo
    print("\n=== Clase Rectangulo ===")
    rectangulo = Rectangulo(punto1, punto2)
    print(f"Rectángulo: {rectangulo}")
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")
