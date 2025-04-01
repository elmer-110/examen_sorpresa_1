from punto import Punto
from rectangulo import rectangulo

class Lanzador:
    def __init__(self):
        self.puntos = {}
        self.rectangulos = {}

    def crear_puntos(self):
        self.puntos['A'] = Punto(2, 3)
        self.puntos['B'] = Punto(5, 5)
        self.puntos['C'] = Punto(-3, -1)
        self.puntos['D'] = Punto(0, 0)

    def mostrar_puntos(self):
        print("Puntos:")
        for nombre, punto in self.puntos.items():
            print(f"{nombre} = {punto}")

    def mostrar_cuadrantes(self):
        print("\nCuadrantes:")
        for nombre in ['A', 'C', 'D']:
            punto = self.puntos[nombre]
            print(f"{nombre}: {punto.cuadrante()}")

    def mostrar_vectores(self):
        A = self.puntos['A']
        B = self.puntos['B']
        print("\nVectores:")
        print("Vector AB:", A.vector(B))
        print("Vector BA:", B.vector(A))

    def mostrar_distancias(self):
        A = self.puntos['A']
        B = self.puntos['B']
        print("\nDistancias:")
        print("Distancia A-B:", A.distancia(B))
        print("Distancia B-A:", B.distancia(A))

    def mostrar_mas_lejano(self):
        origen = Punto()
        distancias = {nombre: p.distancia(origen) for nombre, p in self.puntos.items() if nombre in ['A', 'B', 'C']}
        mas_lejano = max(distancias, key=distancias.get)
        print(f"\nEl punto más lejano del origen es {mas_lejano} con distancia {distancias[mas_lejano]:.2f}")

    def crear_rectangulo(self):
        A = self.puntos['A']
        B = self.puntos['B']
        self.rectangulos['AB'] = rectangulo(A, B)

    def mostrar_info_rectangulo(self):
        rect = self.rectangulos['AB']
        print("\nRectángulo formado por A y B:")
        print("Base:", rect.base())
        print("Altura:", rect.altura())
        print("Área:", rect.area())

    def ejecutar(self):
        self.crear_puntos()
        self.mostrar_puntos()
        self.mostrar_cuadrantes()
        self.mostrar_vectores()
        self.mostrar_distancias()
        self.mostrar_mas_lejano()
        self.crear_rectangulo()
        self.mostrar_info_rectangulo()
