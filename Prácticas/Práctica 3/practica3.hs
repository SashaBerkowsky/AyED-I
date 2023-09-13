-- 1.a
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
f:: Integer->Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- 1.b
g:: Integer->Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- 1.c
h:: Integer->Integer
h x = g(f x)

k:: Integer->Integer
k x = f(g x)

-- 2.a
absoluto:: Int -> Int
absoluto x | x >= 0 = x
           | otherwise = -x

-- 2.b
maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y | absoluto_x >= absoluto_y = x
                   | otherwise = y
                   where absoluto_x = absoluto x
                         absoluto_y = absoluto y

-- 2.c 
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise = z

-- 2.d.1 
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False

--2.d.2
algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM x 0 = True
algunoEs0PM 0 y = True
algunoEs0PM x y = False

-- 2.e.1 
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x == 0 && y == 0 = True
              | otherwise = False

-- 2.e.2 
ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM x y = False

-- 2.f
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= y && x <= 3 && y <= 3 = True
                   | x <= y && (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

-- 2.g
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x == y && x == z = x 
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = x + y
                    | otherwise = x + y + z

-- 2.h                    
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

-- 2.i
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

-- 2.j
digitoDecenas :: Int -> Int
digitoDecenas x = mod (div x 10) 10

-- 3
estanRelacionados:: Int -> Int -> Bool
estanRelacionados x y | mod x y == 0 = True
                      | otherwise = False
            
-- 4.a
prodInt:: (Float, Float) -> (Float, Float) -> (Float, Float)
prodInt (ax, ay) (bx, by) = (ax * bx, ay * by)

-- 4.b
todoMenor:: (Float, Float) -> (Float, Float) -> Bool
todoMenor (ax, ay) (bx, by) | ax < bx && ay < by = True
                            | otherwise = False

-- 4.c
distanciaPuntos:: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (ax, ay) (bx, by) = sqrt((bx - ax)^2 + (by - ay)^2)

-- 4.d
sumaTerna:: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x + y + z

-- 4.e
sumarSoloMultiplos:: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) k | mod x k == 0 && mod y k == 0 && mod z k == 0 = x + y + z
                               | mod x k == 0 && mod y k == 0 = x + y 
                               | mod x k == 0 && mod z k == 0 = x + z
                               | mod y k == 0 && mod z k == 0 = y + z
                               | mod x k == 0 = x
                               | mod y k == 0 = y
                               | mod z k == 0 = z
                               | otherwise = 0

-- 4.f
posPrimerPar:: (Int, Int, Int) ->  Int
posPrimerPar (x, y, z) | even x = 1
                       | even y = 2
                       | even z = 3
                       | otherwise = 4

-- 4.g
crearPar:: a -> b -> (a, b)
crearPar a b = (a, b)

-- 4.h
invertir:: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- 5
todosMenores:: (Int, Int, Int) -> Bool
todosMenores (x, y, z) | f5 x > g5 x && f5 y > g5 y && f5 z > g5 z = True
                       | otherwise = False

f5:: Int -> Int
f5 x | x <= 7 = x^2
     | otherwise = 2*x - 1

g5:: Int -> Int
g5 x | even x = div x 2
     | otherwise = 3*x + 1

-- 6 
bisiesto:: Integer -> Bool
bisiesto x | mod x 4 /= 0 || (mod x 100 == 0 && mod x 400 /= 0) = False
           | otherwise = True

-- 7
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (ax, ay, az) (bx, by, bz) = abs (ax - bx) + abs (ay - by) + abs (az - bz) 

-- 8
comparar:: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | otherwise = 0

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10
