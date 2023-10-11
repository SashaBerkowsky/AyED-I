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


    
        

