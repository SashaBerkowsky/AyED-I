-- 1
fibonacci:: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

-- 2
parteEntera:: Float -> Int
parteEntera x | x <= -1 = parteEnteraNegativo x
              | x >= 1 = parteEnteraPositivo x
              | otherwise = 0

parteEnteraPositivo:: Float -> Int
parteEnteraPositivo x | x < 1 = 0
                      | otherwise = 1 + parteEnteraPositivo (x - 1)

parteEnteraNegativo:: Float -> Int
parteEnteraNegativo x | x > 0 = 0
                      | otherwise = (-1) + parteEnteraNegativo (x + 1)

-- 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | x < y = False
                | otherwise = esDivisible (x - y) y

-- 4
obtenerUltimoDigito:: Integer -> Integer
obtenerUltimoDigito x = mod x 10

sumaImpares:: Integer -> Integer
sumaImpares x | x < 10 = x
              | even ultimoDigito = sumaImpares (div x 10)
              | otherwise = ultimoDigito + sumaImpares (div x 10)
              where ultimoDigito = obtenerUltimoDigito x

-- 5
medioFact:: Integer -> Integer
medioFact n | n <= 1 = 1
            | otherwise = n * medioFact(n - 2)

-- 6
sumaDigitos:: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito + sumaDigitos (div n 10)
              where ultimoDigito = obtenerUltimoDigito n

-- 7
todosDigitosIguales:: Integer -> Bool
todosDigitosIguales x | x < 10 = True
                      | otherwise = (obtenerUltimoDigito x == obtenerUltimoDigito xSinUltimoDigito) && todosDigitosIguales (div x 10)
                      where xSinUltimoDigito = div x 10

-- 8
cantDigitos:: Integer -> Integer
cantDigitos x | x < 10 = 1
              | otherwise = 1 + cantDigitos (div x 10)

iesimoDigito:: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantDigitos n - i))) 10

-- 9
quitarExtremos:: Integer -> Integer
quitarExtremos n = div (n - iesimoDigito n 1 * 10^(cantDigitos n - 1)) 10

esCapicua:: Integer -> Bool
esCapicua n | n < 10 = True
            | otherwise = primerDigito == mod n 10 && esCapicua (quitarExtremos n)
            where primerDigito = iesimoDigito n 1

-- 10.a
f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = 2^n + f1 (n - 1)

-- 10.b
f2 :: Integer -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = q^n + f2 (n - 1) q

-- 10.c
f3 :: Integer -> Float -> Float
f3 n = f2 (n * 2)

-- 10.d
f4 :: Integer -> Float -> Float
f4 n q = f3 n q - f2 (n - 1) q

-- 11.a
eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = 1 / factorial n + eAprox (n - 1)

factorial :: Integer -> Float
factorial n | n == 0 = 1.0
            | otherwise = fromIntegral n * factorial (n - 1)

-- 11.b
e :: Float
e = eAprox 10

-- 12
sucesionA :: Integer -> Float
sucesionA n | n == 1 = 2
               | otherwise = 2 + 1 / sucesionA (n - 1)

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesionA n - 1

-- 13
sumatoriaDePotencia :: Integer -> Integer -> Integer
sumatoriaDePotencia m j | j == 0 = 0
                        | otherwise = m^j + sumatoriaDePotencia m (j - 1)

fnm :: Integer -> Integer -> Integer
fnm n m | n == 0 = 0
        | otherwise = sumatoriaDePotencia n m + fnm (n - 1) m

-- 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = sumaTodasLasPosibilidades q n m + sumaTodasLasPosibilidades q m n

sumaTodasLasPosibilidades :: Integer -> Integer -> Integer -> Integer
sumaTodasLasPosibilidades q n m | n == 0 = 0
                                | otherwise = q^(n+m) + sumaTodasLasPosibilidades q (n - 1) m

-- 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m | n == 0 = 0
                   | otherwise = sumaDenominadores n m + sumaRacionales (n - 1) m

sumaDenominadores :: Integer -> Integer -> Float
sumaDenominadores n m | m == 0 = 0
                      | otherwise = fromIntegral n / fromIntegral m + sumaDenominadores n (m - 1)

-- 16.a
menorDivisorDesdeHasta :: Integer -> Integer -> Integer
menorDivisorDesdeHasta d h | mod h d == 0 = d
                           | otherwise = menorDivisorDesdeHasta (d + 1) h

menorDivisor :: Integer -> Integer
menorDivisor = menorDivisorDesdeHasta 2

-- 16.b
esPrimo :: Integer -> Bool
esPrimo 1 = True
esPrimo n = menorDivisor n == n

-- 16.c
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = sonCoprimosDH n m 2

sonCoprimosDH :: Integer -> Integer -> Integer -> Bool
sonCoprimosDH a b n | n > a || n > b = True
                    | mod a n == 0 && mod b n == 0 = False
                    | otherwise = sonCoprimosDH a b (n + 1)

-- 16.d
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo = encontrarPrimoDesde 1

encontrarPrimoDesde :: Integer -> Integer -> Integer
encontrarPrimoDesde p n | n == 1 && esPrimo p = p
                   | esPrimo p = encontrarPrimoDesde (p + 1) (n - 1)
                   | otherwise = encontrarPrimoDesde (p + 1) n

-- 17
esFibonacci :: Integer -> Bool
esFibonacci = esFibonacciDesde 1

esFibonacciDesde :: Integer -> Integer -> Bool
esFibonacciDesde e n | elemFibonacci > n = False
                     | elemFibonacci == n = True
                     | otherwise = esFibonacciDesde (e + 1) n
                     where elemFibonacci = fibonacci e

-- 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n  = compararMayorDigitoPar n (-1)

compararMayorDigitoPar :: Integer -> Integer -> Integer
compararMayorDigitoPar n dm | n == 0 = dm 
                            | even ultimoDigito = compararMayorDigitoPar (div n 10) (max ultimoDigito dm)
                            | otherwise = compararMayorDigitoPar (div n 10) dm
                        where ultimoDigito = obtenerUltimoDigito n

-- 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = restarPrimos 1 n == 0

restarPrimos :: Integer -> Integer -> Integer
restarPrimos n p | p <= 0 = p
                 | otherwise = restarPrimos (n + 1) (p - nPrimo)
                 where nPrimo = nEsimoPrimo n
                 
-- 20
sumaDivisores:: Integer -> Integer -> Integer -> Integer
sumaDivisores n i s | n == i = s + n
                    | mod n i == 0 = sumaDivisores n (i + 1) (s + i)  
                    | otherwise = sumaDivisores n (i + 1) s

obtenerMaxSumaDivisores :: Integer -> Integer -> Integer -> Integer -> Integer
obtenerMaxSumaDivisores n m s i | n == m && s >= sumaDiv = n
                                | n == m && s < sumaDiv = i
                                | otherwise = obtenerMaxSumaDivisores (n + 1) m (max s sumaDiv) n
                             where sumaDiv = sumaDivisores n 1 0

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n m = obtenerMaxSumaDivisores n m 0 0

-- 21
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r | n == 0 = sumaTernas m 0 r
                | otherwise = sumaTernas m n r + pitagoras m (n-1) r

satisfacePitagoras :: Integer -> Integer -> Integer -> Bool
satisfacePitagoras m n r = m^2 + n^2 <= r^2

sumaTernas :: Integer -> Integer -> Integer -> Integer
sumaTernas m n r | m == 0 && esTernaPitagorica = 1
                 | m == 0 = 0
                 | esTernaPitagorica = 1 + sumaTernas (m-1) n r
                 | otherwise = sumaTernas (m-1) n r
            where
                  esTernaPitagorica = satisfacePitagoras m n r