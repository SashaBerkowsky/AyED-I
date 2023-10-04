{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) | not (esTuplaValida x) || not (perteneceAPersonas x xs)  = False
                         | otherwise = relacionesValidas xs

esTuplaValida :: (String, String) -> Bool
esTuplaValida (pa, pb) = pa /= pb

perteneceAPersonas :: (String, String) -> [(String, String)] -> Bool
perteneceAPersonas _ [] = True
perteneceAPersonas (pa, pb) ((xa, xb):xs) | (xa, xb) == (pa, pb) ||  (xa == pb) && (xb == pa) = False
                                          | otherwise = perteneceAPersonas (pa, pb) xs

personas :: [(String, String)] -> [String]
personas (x:xs) = acumularPersonas (x:xs) [fst x, snd x]

acumularPersonas :: [(String, String)] -> [String] -> [String]
acumularPersonas [] lp = lp
acumularPersonas (x:xs) lp | noPerteneceFst && noPerteneceSnd = acumularPersonas xs (lp ++ [fst x, snd x])
                           | noPerteneceFst = acumularPersonas xs (lp ++ [fst x])
                           | noPerteneceSnd = acumularPersonas xs (lp ++ [snd x])
                           | otherwise = acumularPersonas xs lp
                           where noPerteneceFst = not (pertenece (fst x) lp)
                                 noPerteneceSnd = not (pertenece (snd x) lp)

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece p (x:xs) | p == x || p == x = True
                   | otherwise = pertenece p xs

amigosDe :: String -> [(String, String)] -> [String]
amigosDe p (r:rs) = acumularAmigos p (r:rs) []

acumularAmigos :: String -> [(String, String)] -> [String] -> [String]
acumularAmigos _ [] a = a
acumularAmigos p ((p1, p2):rs) a | pertenece p1 a || pertenece p2 a = acumularAmigos p rs a
                                 | p == p1 = acumularAmigos p rs (a ++ [p2])
                                 | p == p2 = acumularAmigos p rs (a ++ [p1])
                                 | otherwise = acumularAmigos p rs a

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos (x:xs) = compararCantApariciones (x:xs) listaPersonas (head listaPersonas)
                          where listaPersonas = personas (x:xs)

compararCantApariciones :: [(String, String)] -> [String] -> String -> String
compararCantApariciones _ [] pma = pma
compararCantApariciones (r:rs) p pma | cantApariciones (head p) (r:rs) > cantApariciones pma (r:rs) = compararCantApariciones (r:rs) p (head p)
                                     | otherwise = compararCantApariciones (r:rs) (tail p) pma
                                    
cantApariciones :: String -> [(String, String)] -> Integer
cantApariciones _ [] = 0
cantApariciones p (r:rs) | p == fst r || p == snd r = 1 + cantApariciones p rs
                         | otherwise = cantApariciones p rs

-- Testing a mano
relacion1 :: (String, String)
relacion1 = ("yo", "otro")

relacion2 :: (String, String)
relacion2 = ("otro", "yo")

relacion3 :: (String, String)
relacion3 = ("uno", "dos")

relacion4 :: (String, String)
relacion4 = ("yo", "yo")

relacion5 :: (String, String)
relacion5 = ("Nuev", "yo")

relacionValida :: [(String, String)]
relacionValida = [relacion1, relacion3, relacion5]

relacionInvalida :: [(String, String)]
relacionInvalida = [relacion1, relacion2]

relacionInvalida2 :: [(String, String)]
relacionInvalida2 = [relacion1, relacion1]