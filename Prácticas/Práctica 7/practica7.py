import random

# 1.1
def perteneceA(s: list[int], e: int) -> bool:
    return e in s

def perteneceB(s: list, e) -> bool:
    return e in s

def perteneceC(s, e) -> bool:
    return e in s

# 1.2
def divideATodos(s: list[int], e:int) -> bool:
    i: int = 0
    longitud_secuencia: int = len(s)
    while (i < longitud_secuencia and s[i] % e == 0):
        i+=1
    return i == longitud_secuencia

# 1.3
def sumaTotal(s: list[int]) -> int:
    suma: int = 0
    for e in s:
        suma += e
    return suma

# 1.4
def ordenados(s: list[int]) -> bool:
    i: int = 0
    longitud_secuencia: int = len(s)
    while(i < longitud_secuencia - 1 and s[i] < s[i+1]):
        i+=1
    return i == longitud_secuencia - 1

# 1.5
def longitudMayorSiete(frase: str) -> bool:
    i: int = 0
    palabras: list[str] = frase.split(' ')
    cantidad_palabras: int = len(palabras)
    while(i < cantidad_palabras and len(palabras[i]) <= 7):
        i += 1
    return i != cantidad_palabras

# 1.6
def esPalindromo(palabra: str) -> bool:
    i: int = 0
    palabraMinuscula = palabra.lower()
    longitud_palabra: int = len(palabraMinuscula)
    while(i < longitud_palabra and palabraMinuscula[i] == palabraMinuscula[longitud_palabra - i - 1]):
        i+=1
    return i == longitud_palabra


# 1.7
def es_digito_numerico(ascii: int) -> bool:
    return ascii >= 48 and ascii <= 57  

def es_letra_mayuscula(ascii: int) -> bool:
    return (ascii >= 65 and ascii <= 90) or ascii == 209

def es_letra_minuscula(ascii: int) -> bool:
    return (ascii >= 97 and ascii <= 122) or ascii == 241

def fortalezaContraseña(contraseña: str) -> str:
    longitud_contraseña: int = len(contraseña)
    tieneMinuscula: bool = False
    tieneMayuscula: bool = False
    tieneNumero: bool = False
    
    for c in contraseña:
        ascii: int = ord(c)
        tieneMinuscula = tieneMinuscula or es_letra_minuscula(ascii)
        tieneMayuscula = tieneMayuscula or es_letra_mayuscula(ascii)
        tieneNumero = tieneNumero or es_digito_numerico(ascii)

    es_contraseña_fuerte = tieneMinuscula and tieneMayuscula and tieneNumero and longitud_contraseña > 8
    if (es_contraseña_fuerte):
        return "VERDE"
    elif (longitud_contraseña >= 5):
        return "AMARILLA"
    else:
        return "ROJA"

# 1.8
def movimientosCuentaBancaria(movimientos: list[tuple[str, int]]) -> int:
    saldo: int = 0
    for movimiento in movimientos:
        tipoMovimiento = movimiento[0]
        monto = movimiento[1]
        if (tipoMovimiento == 'I'):
            saldo += monto
        else:
            saldo -= monto
    
    return saldo

# 1.9
def tiene3VocalesDistintas(palabra: str) -> bool:
    i: int = 0
    longitudPalabra = len(palabra)
    vocalesExistentes: list[str] = ["a","e","i","o","u"]
    vocales: list[str] = []

    while (i < longitudPalabra and len(vocales) < 3):
        letraMinuscula = palabra[i].lower()
        if(pertenece_B(vocalesExistentes, letraMinuscula)):
            vocales.append(letraMinuscula)
        i+=1
        
    return len(vocales) == 3

# 2.1
def borrarPosicionesPares(s: list[int]) -> list[int]:
    for i in range(len(s)):
        if(i % 2 == 0):
            s[i] = 0
    return s

# 2.2
def borrarPosicionesParesB(s: list[int]) -> list[int]:
    nuevaSecuencia: list[int] = []

    for i in range(len(s)):
        nuevoElemento = 0 if i % 2 == 0 else s[i]
        nuevaSecuencia.append(nuevoElemento)

    return nuevaSecuencia

# 2.3
def quitarVocales(texto: str) -> str:
    vocales: list[str] = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    textoSinVocales: str = ""

    for e in texto:
        if (not pertenece_B(vocales, e)):
            textoSinVocales += e

    return textoSinVocales

# 2.4
def reemplazaVocales(texto: str) -> str:
    vocales: list[str] = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    textoModificado: str = ""

    for e in texto:
        if(pertenece_B(vocales, e)):
            textoModificado += "_"
        else:
            textoModificado += e
    
    return textoModificado
    
# 2.5
def daVueltaStr(texto: str) -> str:
    textoModificado: str = ""

    for i in range(1, len(texto) + 1):
        textoModificado += texto[-i]

    return textoModificado

# 2.6
def eliminarRepetidos(texto: str) -> str:
    textoSinRepetidos: str = ""

    while(len(texto) != 0):
        textoSinRepetidos += texto[0]
        texto = texto.replace(texto[0], "")

    return textoSinRepetidos

# 3
def aprobado(notas: list[int]) -> int:
    promedio: int = round(sum(notas)/len(notas))
    reproboExamenes = hayNotasReprobadas(notas)
    if (not reproboExamenes and promedio >= 7):
        return 1
    elif (not reproboExamenes and promedio >= 4):
        return 2
    else:
        return 3
    
def hayNotasReprobadas(notas: list[int]) -> bool:
    i: int = 0
    tieneReprobados: bool = False
    while (i < len(notas) and not tieneReprobados):
        tieneReprobados = notas[i] < 4
        i+=1

    return tieneReprobados

# 4.1
def pedirNombresDeEstudiantes() -> None:
    INPUT_PROMPT: str = "Ingrese el nombre del estudiante "
    lista: list[str] = []
    nombre: str = input(INPUT_PROMPT)

    while(nombre != "listo"):
        lista.append(nombre)
        nombre = input(INPUT_PROMPT)

    print(lista)

# 4.2
def sistemaSube() -> None:
    INPUT_PROMPT: str = "C = Cargar creditos, D = Descontar creditos, X = Finalizar\n"
    saldo: int = 0
    movimiento: str = input(INPUT_PROMPT).upper()
    historial: list[tuple[str, int]] = []

    # asumo que siempre es C, D o X
    while(movimiento != "X"):
        monto: int = int(input("Ingrese el monto "))
        historial.append((movimiento, monto))
        if (movimiento == "C"):
            saldo += monto
        else:
            saldo -= monto
        movimiento = input(INPUT_PROMPT).upper()

    print("Su saldo total es de $" + str(saldo))
    print(historial)

# 4.3
def sieteYMedio() -> None:
    INPUT_PROMPT: str = "Plantarse (P) o seguir (S)? "  
    puntuacion: float = 0
    cartas: list[float] = []
    continuar: bool = True
    while (continuar and puntuacion < 7.5):
        numero: int = random.choice([1,2,3,4,5,6,7,10,11,12])
        valor: float = numero if numero < 10 else 0.5
        puntuacion += valor
        cartas.append(numero)
        continuar = input(INPUT_PROMPT).upper() != "P"
    
    print("Perdiste" if puntuacion >= 7.5 else "Ganaste")
    print(cartas)

# 5.1
def perteneceACadaUno(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []

    for array in s:
        res.append(perteneceB(array, e))

    return res

# 5.2
def esMatriz(s: list[list[int]]) -> bool:
    i: int = 0
    estaVacio = False
    while(not estaVacio and i < len(s)):
        estaVacio = len(s[i]) == 0
        i+=1

    return not estaVacio

# 5.3
def filasOrdenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    
    for array in m:
        res.append(ordenados(array))

    return res

print(filasOrdenadas([[1,4,3],[1],[1]]))
