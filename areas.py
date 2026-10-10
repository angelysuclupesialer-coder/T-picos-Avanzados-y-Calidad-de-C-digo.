#areas
def calcular_area_cuadrado(lado):
    return lado * lado


def calcular_area_rectangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def mostrar_resultados():
    print("Area del cuadrado:", calcular_area_cuadrado(4))
    print("Area del rectangulo:", calcular_area_rectangulo(5, 3))
    print("Area del triangulo:", calcular_area_triangulo(6, 2))


if __name__ == "__main__":
    mostrar_resultados()
