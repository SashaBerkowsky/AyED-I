# 1.1
def pertenece_A(s: list[int], e: int) -> bool:
    return e in s

def pertenece_B(s: list, e) -> bool:
    return e in s

def pertenece_C(s, e) -> bool:
    return e in s

# 1.2
def divide_a_todos(s: list[int], e:int) -> bool:
    i = 0
    longitud_secuencia = len(s)
    while (i < longitud_secuencia and s[i] % e == 0):
        i+=1
    return i == longitud_secuencia

# 1.3
def suma_total(s: list[int]) -> int:
    suma = 0
    for e in s:
        suma += e
    return suma

print(suma_total([1,2,3,4,5,6]))
