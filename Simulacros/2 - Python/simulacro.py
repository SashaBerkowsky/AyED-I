from queue import Queue
from queue import LifoQueue

# 1
def ultima_aparicion(s: list[int], e: int) -> int:
    posicion: int = len(s) - 1

    while(posicion > 0 and s[-posicion] != e):
        posicion -= 1

    return posicion

# 2
def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    elementosExclusivos: list[int] = []

    for elementoS in s:
        if (not elementoS in t and not elementoS in elementosExclusivos):
            elementosExclusivos.append(elementoS)


    for elementoT in t:
        if (not elementoT in s and not elementoT in elementosExclusivos):
            elementosExclusivos.append(elementoT)

    return elementosExclusivos

# 3
def contar_traducciones_iguales(ing: dict[str, str], ale: dict[str, str]) -> int:
    mismasTraducciones: int = 0

    for palabra in ing:
        if (palabra in ale and ing[palabra] == ale[palabra]):
            mismasTraducciones += 1

    return mismasTraducciones

# 4
def convertir_a_diccionario(lista: list[int]) -> dict[int, int]:
    diccionario = {}

    for elemento in lista:
        if (elemento in diccionario):
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1

    return diccionario

