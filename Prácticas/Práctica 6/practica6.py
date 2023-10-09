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
def fahrenheit_a_celcius(temp_far: float) -> float:
    return ((temp_far-32)*5)/9
    
# 2.4
def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo * 2)

# 2.5
def es_multiplo_de(n:int, m:int) -> bool:
    return n % m == 0

# 2.6
def es_par(n:int) -> bool:
    return es_multiplo_de(n, 2)

# 2.7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return math.ceil(comensales*min_cant_de_porciones/8)

# 3.1
def alguno_es_0(numero1: int, numero2 :int) -> bool:
    return numero1 == 0 or numero2 == 0

# 3.2
def ambos_son_0(numero1: int, numero2: int) -> bool:
    return numero1 == 0 and numero2 == 0

# 3.3
def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# 3.4
def es_bisiesto(año: int) -> bool:
    return año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)

# 4.1
def peso_pino(altura_m: int) -> int:
    peso = 0
    while (altura_m > 3):
        peso += 200
        altura_m -= 1
    peso += 300 * altura_m
    return peso

# 4.2
def es_peso_util(peso_kg: int) -> bool:
    return peso_kg >= 400 and peso_kg <= 1000

# 4.3
def sirve_pino(altura_m: int) -> bool:
    peso = peso_pino(altura_m)
    sirve = es_peso_util(peso)
    return sirve

# 4.4
def sirve_pino_comp(altura_m: int) -> bool:
    return es_peso_util(peso_pino(altura_m))

# 5.1
def devolver_el_doble_si_es_par(n: int) -> int:
    return 2*n if n % 2 == 0 else n

# 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int: #PONERLE ESTOS NOMBRES DEBERIA SER ILEGAL
    return n if n % 2 == 0 else n + 1

# 5.3
def devolver_el_doble_si_es_multiplo_de_3_el_triple_si_es_multiplo9(n: int) -> int: # ESE NOMBRE ??????
    return 3*n if n % 9 == 0 else 2*n if n % 3 == 0 else n

# 5.4
def lindo_nombre(nombre: str) -> None:
    nombre_len = len(nombre)
    print("Tu nombre tiene muchas letras") if nombre_len >= 5 else print("Tu nombre tiene menos de 5 caracteres")

# 5.5
def el_rango(n: int) -> None:
    if (n > 20):
        print("Mayor a 20")
    elif (n <= 20 and n >= 10):
        print("Entre 10 y 20")
    elif (n < 10 and n >= 5):
        print("Entre 5 y 9")
    else:
        print("Menor a 5")

# 5.6
def verificar_vacaciones(genero: str, edad: int) -> None:
    edad_jubilatoria = 65 if genero == "M" else 60
    if (edad < 18 or edad >= edad_jubilatoria):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

# 6.1
def imprimir_1_a_10() -> None:
    i = 1
    while (i <= 10):
        print(i)
        i += 1

# 6.2
def imprimir_pares_10_a_40() -> None:
    i = 10
    while (i <= 40):
        print(i)
        i += 2

# 6.3
def imprimir_eco_10_veces() -> None:
    i = 0
    while (i < 10):
        print("eco")
        i += 1

# 6.4
def cuenta_regresiva(desde: int) -> None:
    while (desde > 0):
        print(desde)
        desde -= 1
    print("Despegue")

# 6.5
def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> None:
    distancia = año_partida - año_llegada
    while (distancia >=  0):
        print("Viajó un año al pasado, estamos en el año: " + str(año_llegada + distancia))
        distancia -= 1

# 6.6
def conocer_aristoteles(año_partida: int) -> None:
    AÑO_ARISTOTELES = -384
    desde = año_partida - 20
    while (desde >= AÑO_ARISTOTELES):
        año_actual: str = str(desde) if desde >= 0 else (str(desde * (-1)) + " a.c")
        print("Viajó veinte años al pasado, estamos en el año:", año_actual)
        desde -= 20

# 7.1
def imprimir_1_a_10_for() -> None:
    for i in range(1, 11):
        print(i)

# 7.2
def imprimir_pares_10_a_40_for() -> None:
    for i in range(10, 41, 2):
        print(i)

# 7.3
def imprimir_eco_10_veces_for() -> None:
    for _ in range(10):
        print("eco")

# 7.4
def cuenta_regresiva_for(desde: int) -> None:
    for i in range(desde, 0, -1):
        print(i)
    print("Despegue!")

# 7.5
def viaje_en_el_tiempo_for(año_salida: int, año_llegada: int) -> None:
    for i in range(año_salida, año_llegada - 1, -1):
        print("Viajó un año al pasado, estamos en el año: " + str(i))

# 7.6
def conocer_aristoteles_for(año_partida: int) -> None:
    AÑO_ARISTOTELES = -384
    for i in range(año_partida - 20, AÑO_ARISTOTELES + 20, -20):
        año_actual: str = str(i) if i >= 0 else (str(i * (-1)) + " a.c")
        print("Viajó veinte años al pasado, estamos en el año: ", año_actual)



conocer_aristoteles_for(20)

