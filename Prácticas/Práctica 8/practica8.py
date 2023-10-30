import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
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

    pilaAux.put(maximo)
    while(not p.empty()):
        elemento: int = p.get()
        if (elemento > maximo):
            maximo = elemento
        pilaAux.put(elemento)

    rearmar_pila(p, pilaAux)

    return maximo

# Esta feo pero funciona
# 11
def esta_bien_balanceada(cuenta: str) -> bool:
    parentesis_parejos: bool = cuenta.count("(") == cuenta.count(")")
    elementos_cuenta = cuenta.split(" ")
    operaciones = ["+", "-", "*", "/"]
    cuenta_invalida: bool = False
    i = 1

    while (i < (len(elementos_cuenta) - 1) and not cuenta_invalida):
        elemento: str = elementos_cuenta[i]
        elemento_ant: str = elementos_cuenta[i - 1]
        elemento_sig: str = elementos_cuenta[i + 1]
        if (elemento == "("):
            cuenta_invalida = not pertenece(elemento_ant, operaciones) and pertenece(elemento_sig, operaciones)
        elif (elemento == ")"):
            cuenta_invalida = pertenece(elemento_ant, operaciones) and not pertenece(elemento_sig, operaciones)

        i+=1

    return parentesis_parejos and not cuenta_invalida

def pertenece(elemento, lista) -> bool:
    i: int = 0
    res = False

    while (not res and i < len(lista)):
        res = lista[i] == elemento
        i += 1

    return res

# 12
def evaluar_expresion_postfix(expresion: str) -> int:
    operaciones: list[str] = ["+", "-", "*", "/"]
    operandos: Pila[int] = Pila()
    elementos = expresion.split(" ")

    for e in elementos:
        if(pertenece(e, operaciones)):
            b = operandos.get()
            a = operandos.get()
            c: int = 0
            match e:
                case "+":
                    c = a + b
                case "-":
                    c = a - b
                case "*":
                    c = a * b
                case "/":
                    c = int(a / b)
            operandos.put(c)
        else:
            operandos.put(int(e))

    return operandos.get()

#   **********Colas**********
# 13
def generar_cola_al_azar(n: int, desde: int, hasta: int) -> Cola:
    pila = generar_nros_al_azar(n, desde, hasta)
    cola = Cola()

    while(not pila.empty()):
        cola.put(pila.get())
    
    return cola

# 14
def cantidad_elementos_cola(cola: Cola) -> int:
    cantidad_elementos: int = 0

    while(not cola.empty()):
        cantidad_elementos += 1
        cola.get()

    return cantidad_elementos

# 15
def buscar_el_maximo_cola(cola: Cola[int]) -> int:
    maximo: int = cola.get()
    colaAux: Cola[int] = Cola()
    
    colaAux.put(maximo)
    while(not cola.empty()):
        elemento: int = cola.get()
        colaAux.put(elemento)
        maximo = elemento if elemento > maximo else maximo

    rearmar_cola(colaAux, cola)
    return maximo


def rearmar_cola(colaAux, colaDef) -> None:
    while(not colaAux.empty()):
        colaDef.put(colaAux.get())

# 16.1
def armar_secuencia_bingo() -> Cola[int]:
    sample: list[int] = random.sample(range(0, 100), 12)
    cola: Cola[int] = Cola()

    for elemento in sample:
        cola.put(elemento)

    return cola

# 16.2
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0

    while(not bolillero.empty() and carton != []):
        numero: int = bolillero.get()
        if (numero in carton):
            jugadas += 1
            carton.remove(numero)

    return jugadas

# 17
def n_pacientes_urgentes(cola: Cola[tuple[int, str, str]]) -> int:
    pacientesUrgentes: int = 0
    colaAux: Cola[tuple[int, str, str]] = Cola()

    while(not cola.empty()):
        paciente = cola.get()
        pacientesUrgentes += 1 if paciente[0] <= 3 else 0
         
        colaAux.put(paciente)

    rearmar_cola(colaAux, cola)
    return pacientesUrgentes

# 18
def cola_clientes(cola: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    colaOrdenada: Cola[tuple[str, int, bool, bool]] = Cola()
    colaPreferencial: Cola[tuple[str, int, bool, bool]] = Cola() 
    colaOrdinaria: Cola[tuple[str, int, bool, bool]] = Cola()

    while (not cola.empty()):
        cliente = cola.get()
        tienePrioridad = cliente[3]
        esPreferencial = cliente[2]

        if (tienePrioridad):
            colaOrdenada.put(cliente)
        elif (esPreferencial):
            colaPreferencial.put(cliente)
        else:
            colaOrdinaria.put(cliente)

    while(not colaPreferencial.empty()):
        colaOrdenada.put(colaPreferencial.get())

    while(not colaOrdinaria.empty()):
        colaOrdenada.put(colaOrdinaria.get())

    return colaOrdenada

#   **********Archivos**********
# 19
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    diccionario: dict = {} 
    archivo = open(nombre_archivo)
    contenido = archivo.read().splitlines()
    archivo.close()

    for linea in contenido:
        for palabra in linea.split(" "):
            longitudPalabra: int = len(palabra)
            if (longitudPalabra in diccionario):
                diccionario[longitudPalabra] = diccionario[longitudPalabra] + 1
            else:
                diccionario[longitudPalabra] = 1

    return diccionario

# /*** A partir de aca me empieza a dar fiaca ***\

# 20
def promedio_estudiante_diccionario() -> dict:
    notas: dict = {}
    cantMaterias: dict = {}
    nombre_archivo: str = "notes.csv"
    archivo = open(nombre_archivo, "r")
    archivo.readline()
    linea: list[str] = quitar_salto_de_linea(archivo.readline()).split(",")

    while(linea != [""]):
        print(linea)
        nro_lu = linea[0]
        if (nro_lu in notas):
            notas[nro_lu] += int(linea[3])
            cantMaterias[nro_lu] += 1
        else:
            notas[nro_lu] = int(linea[3])
            cantMaterias[nro_lu] = 1
        linea: list[str] = quitar_salto_de_linea(archivo.readline()).split(",")

    archivo.close()

    for lu in notas:
        notas[lu] = notas[lu] / cantMaterias[lu]

    return notas

# 21
def palabra_mas_frecuente(nombre_archivo: str) -> str:
    palabraMasFrecuente: tuple[str, int] = ("", 0)
    archivo = open(nombre_archivo, "r")
    contenido: list[str] = archivo.read().replace("\n", " ").split(" ")
    archivo.close

    for palabra in contenido:
        if (palabra != ""):
            cantApariciones = contenido.count(palabra)
            if (cantApariciones > palabraMasFrecuente[1]):
                palabraMasFrecuente = (palabra, cantApariciones)

            contenido.remove(palabra)

    print(palabraMasFrecuente)

    return palabraMasFrecuente[0]

# 22.2
def visitar_sitio(historiales: dict, usuario: str, sitio: str) -> None:
    if usuario in historiales:
        historiales[usuario] = historiales[usuario].put(sitio)
    else:
        historial = Pila()
        historiales[usuario] = historial.put(sitio)

