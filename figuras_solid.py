
from abc import ABC, abstractmethod


class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Triangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio


def mostrar_area(figura):
    print("Area:", figura.calcular_area())


if __name__ == "__main__":
    figuras = [
        Cuadrado(4),
        Rectangulo(5, 3),
        Triangulo(6, 2),
        Circulo(2)
    ]

    for figura in figuras:
        mostrar_area(figura)
