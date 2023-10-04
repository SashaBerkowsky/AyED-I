-- 1.i
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
longitud :: [t] -> Integer
longitud [] = 0
longitud (x: xs) = 1 + longitud xs

-- 1.ii
ultimo :: [t] -> t
ultimo (x: xs) | longitud (x:xs) == 1 = x
               | otherwise = ultimo xs

-- 1.iii
principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x: principio xs

-- 1.iv
reverso :: (Eq t) => [t] -> [t]
reverso (x: xs) | null xs = [x]
                | otherwise = reverso xs ++ [x]

-- 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e l | longitud l == 0 = False
              | e == head l = True
              | otherwise = pertenece e (tail l)

-- 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x: xs) | longitud xs == 1 = x == head xs
                     | otherwise = x == head xs && todosIguales xs

-- 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x: xs) | longitud xs == 0 = True
                       | pertenece x xs = False
                       | otherwise = todosDistintos xs

-- 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (x: xs) | longitud xs == 0 = False
                     | pertenece x xs = True
                     | otherwise = hayRepetidos xs

-- hayRepetidos :: (Eq t) => [t] -> Bool
-- hayRepetidos (x:xs) = not (todosDistintos (x:xs))

-- 2.5 
quitar :: (Eq t) => t -> [t] -> [t]
quitar e (x: xs) | e == x = xs
                 | not (pertenece e (x: xs)) = x: xs
                 | otherwise = x: quitar e xs

-- 2.6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e l | not (pertenece e l) = l
                | head l == e = quitarTodos e (tail l)
                | otherwise = head l : quitarTodos e (tail l)

-- 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos l | todosDistintos l = l
                    | otherwise = head l : eliminarRepetidos (quitarTodos (head l) (tail l))

-- 2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos la lb = todosLosElementosPertenecen la lb && todosLosElementosPertenecen lb la

todosLosElementosPertenecen :: (Eq t) => [t] -> [t] -> Bool
todosLosElementosPertenecen la lb | longitud la == 0 = True
                                  | not (pertenece (head la) lb) = False
                                  | otherwise = todosLosElementosPertenecen (tail la) lb

-- 2.9
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [x] = True
capicua (x: xs) | x == ultimo xs = capicua (principio xs)
                | otherwise = False

-- 3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x: xs) = x + sumatoria xs

-- 3.2 
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- 3.3
maximo :: [Integer] -> Integer
maximo (x:xs)  = obtenerMaximo xs x

obtenerMaximo :: [Integer] -> Integer -> Integer
obtenerMaximo (x:xs) e | longitud xs == 0 = max e x
                       | x >= e = obtenerMaximo xs x
                       | otherwise = obtenerMaximo xs e

-- 3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) | longitud xs == 0 = [x+n]
                | otherwise = (x+n) : sumarN n xs

-- 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- 3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | even x = x:pares xs
             | otherwise = pares xs

-- 3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

-- 3.9
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = minimo: ordenar (quitar minimo (x:xs))
                where minimo = menor (x:xs)

menor :: [Integer] -> Integer
menor (x:xs) = obtenerMenor xs x

obtenerMenor :: [Integer] -> Integer -> Integer
obtenerMenor (x:xs) n | longitud xs == 0 = min x n
                      | x < n = obtenerMenor xs x
                      | otherwise = obtenerMenor xs n

-- 5.1
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada (x:xs) = sumarElementos (x:xs) [x] 

sumarElementos :: (Num t) => [t] -> [t] -> [t]
sumarElementos (x:xs) y | longX == longY = y
                        | otherwise = sumarElementos (x:xs) (y ++ [sumarHasta (x:xs) longY])
                            where longX = longitud (x:xs)
                                  longY = longitud y

sumarHasta :: (Num t) => [t] -> Integer -> t
sumarHasta _ (-1) = 0
sumarHasta (x:xs) t = x + sumarHasta xs (t-1)

-- 5.2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [x] = [descomponer x]
descomponerEnPrimos (x:xs) = descomponer x:descomponerEnPrimos xs

descomponer :: Integer -> [Integer]
descomponer 1 = []
descomponer n = divisor:descomponer (div n divisor)
              where divisor = menorDivisorPrimo 2 n

menorDivisorPrimo :: Integer -> Integer -> Integer
menorDivisorPrimo d n | dEsPrimo && mod n d == 0 = d
                      | otherwise = menorDivisorPrimo (d+1) n
                      where dEsPrimo = menorDivisor d 2 == d

menorDivisor :: Integer -> Integer -> Integer
menorDivisor n i | mod n i == 0 = i
                 | otherwise = menorDivisor n (i+1)