import math


# 1.1
def raizDe2():
    return round(math.sqrt(2), 4)


# 1.2
def imprimir_hola():
    print("hola")


# 1.3: seru >>
def imprimir_un_verso():
    print(
        "Si en la música que escuchas ya no hay vida\nSi la letra ya no tiene inspiración\nSi aunque aumentes el volumen ya no hay fuerza\nSon los tiempos que están huecos de emoción"
    )


# 1.4 a 1.7
# me reuso a hacer esta atrocidad, hago todo en 1 funcion como dios manda
# si no te gusta hace un print de cada factorial
def factorial(x: int) -> int:
    res = x if x > 0 else 1
    while x > 1:
        res = res * (x - 1)
        x -= 1
    return res


# 2.1
def imprimir_saludo(saludo: str) -> None:
    print(saludo)


# 2.2
def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)


# 2.3
def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo * 2)
