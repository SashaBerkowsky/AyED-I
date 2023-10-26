import random
from queue import LifoQueue as Pila
#   **********Archivos**********
# 1.1
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas: int = 0

    for _ in archivo.readlines():
        lineas += 1

    archivo.close()

    return lineas

# 1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    res = False
    archivo = open(nombre_archivo, "r")
    lineas: list[str] = archivo.read().splitlines()
    i: int = 0

    while(i < len(lineas) and not res):
        palabras = lineas[i].split(" ")
        f: int = 0
        while(f < len(palabras) and not res):
            res = palabras[f] == palabra
            f += 1
        i += 1

    archivo.close()

    return res

# 1.3
def cantidad_apariciones(palabra: str, nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas: list[str] = archivo.read().splitlines()
    apariciones: int = 0

    for linea in lineas:
        palabras: list[str] = linea.split(" ")
        for p in palabras:
            apariciones += 1 if p == palabra else 0

    archivo.close()

    return apariciones

# 2
def clonar_sin_comentarios(nombre_archivo: str) -> None:
    archivo = open(nombre_archivo, "r")
    texto_limpio: list[str] = []
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        es_comentario: bool = linea.strip().startswith("#")
        nueva_linea: str = linea.replace("#", "", 1) if es_comentario else linea
        texto_limpio.append(nueva_linea)

    archivo.close()
    
    # deberia poner x, para testear pongo w
    archivo_limpio = open("file_uncommented.txt", "w")
    archivo_limpio.writelines(texto_limpio)
    archivo_limpio.close()

# 3
def reverso(nombre_archivo: str) -> None:
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    lineas_reverso: list[str] = []

    for i in range(1, len(lineas) + 1):
        lineas_reverso.append(lineas[-i])

    archivo.close()

    # deberia poner x, para testear pongo w
    archivo_reverso = open("file_inverted.txt", "w")
    archivo_reverso.writelines(lineas_reverso)
    archivo_reverso.close()

# 4
def agregar_frase_final(nombre_archivo: str, frase: str) -> None:
    archivo = open(nombre_archivo, "a")
    archivo.write(frase + "\n")
    archivo.close

# 5
def agregar_frase_comienzo(nombre_archivo: str, frase: str) -> None:
    archivo = open(nombre_archivo, "r")
    contenido: str = archivo.read()
    archivo.close()

    nuevo_archivo = open(nombre_archivo, "w")
    nuevo_archivo.write(frase + "\n" + contenido)
    nuevo_archivo.close()

# 6 fiaca

# 7
def promedio_estudiante(lu: str) -> float:
    nombre_archivo: str = "notes.csv"
    archivo = open(nombre_archivo, "r")
    linea: str = quitar_salto_de_linea(archivo.readline())
    notas: list[int] = []

    while(linea != ""):
        valores: list[str] = linea.split(",")
        if(valores[0] == lu):
            nota = int(valores[3])
            notas.append(nota)
        linea: str = quitar_salto_de_linea(archivo.readline())
    archivo.close()

    return sum(notas)/len(notas)

def quitar_salto_de_linea(texto: str) -> str:
    return texto.removesuffix("\n")

#   **********Pilas**********
# 8
def generar_nros_al_azar(n: int, desde: int, hasta: int) -> Pila[int]:
    pila: Pila[int] = Pila()
    while (n > 0):
        pila.put(random.randint(desde, hasta))
        n -= 1

    return pila

# 9
def cantidad_elementos(p: Pila[int]) -> int:
    cantElementos: int = 0
    pilaAux = Pila()

    while(not p.empty()):
        cantElementos += 1
        pilaAux.put(p.get())

    rearmar_pila(p, pilaAux)

    return cantElementos

def rearmar_pila(pilaOriginal: Pila, pilaAux: Pila) -> None:
    while (not pilaAux.empty()):
        pilaOriginal.put(pilaAux.get())

# 10
def buscar_el_maximo(p: Pila[int]) -> int:
    pilaAux: Pila[int] = Pila()
    maximo: int = p.get()

    while(not p.empty()):
        elemento: int = p.get()
        if (elemento > maximo):
            maximo = elemento
        pilaAux.put(elemento)

    rearmar_pila(p, pilaAux)

    return maximo

# 11
def esta_bien_balanceada(cuenta: str) -> bool:
    esta_balanceada = False
    operaciones = ["+", "-", "*", "/"]
    for char in cuenta:

        print(type(char))

    return esta_balanceada
    
esta_bien_balanceada("testeo")
