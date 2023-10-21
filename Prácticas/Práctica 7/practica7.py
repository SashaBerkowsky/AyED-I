# 1.1
def pertenece_A(s: list[int], e: int) -> bool:
    return e in s

def pertenece_B(s: list, e) -> bool:
    return e in s

def pertenece_C(s, e) -> bool:
    return e in s

# 1.2
def divide_a_todos(s: list[int], e:int) -> bool:
    i: int = 0
    longitud_secuencia: int = len(s)
    while (i < longitud_secuencia and s[i] % e == 0):
        i+=1
    return i == longitud_secuencia

# 1.3
def suma_total(s: list[int]) -> int:
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
def longitud_mayor_7(frase: str) -> bool:
    i: int = 0
    palabras: list[str] = frase.split(' ')
    cantidad_palabras: int = len(palabras)
    while(i < cantidad_palabras and len(palabras[i]) <= 7):
        i += 1
    return i != cantidad_palabras

# 1.6
def es_palindromo(palabra: str) -> bool:
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

def fortaleza_contraseña(contraseña: str) -> str:
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
def movimientos_cuenta_bancaria(movimientos: list[tuple[str, int]]) -> int:
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
def tiene_3_vocales_distintas(palabra: str) -> bool:
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
def borrar_posiciones_pares(s: list[int]) -> list[int]:
    for i in range(len(s)):
        if(i % 2 == 0):
            s[i] = 0
    return s

# 2.2
def borrar_posiciones_pares_B(s: list[int]) -> list[int]:
    nuevaSecuencia: list[int] = []

    for i in range(len(s)):
        nuevoElemento = 0 if i % 2 == 0 else s[i]
        nuevaSecuencia.append(nuevoElemento)

    return nuevaSecuencia

# 2.3
def quitar_vocales(texto: str) -> str:
    vocales: list[str] = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    textoSinVocales: str = ""

    for e in texto:
        if (not pertenece_B(vocales, e)):
            textoSinVocales += e

    return textoSinVocales

# 2.4
def reemplaza_vocales(texto: str) -> str:
    vocales: list[str] = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    textoModificado: str = ""

    for e in texto:
        if(pertenece_B(vocales, e)):
            textoModificado += "_"
        else:
            textoModificado += e
    
    return textoModificado
    
# 2.5
def da_vuelta_str(texto: str) -> str:
    textoModificado: str = ""

    for i in range(1, len(texto) + 1):
        textoModificado += texto[-i]

    return textoModificado

# 2.6
def eliminar_repetidos(texto: str) -> str:
    textoSinRepetidos: str = ""

    while(len(texto) != 0):
        textoSinRepetidos += texto[0]
        texto = texto.replace(texto[0], "")

    return textoSinRepetidos

print(eliminar_repetidos("manzana"))
    
            



        


    
