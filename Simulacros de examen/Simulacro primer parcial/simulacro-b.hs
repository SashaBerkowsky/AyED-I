relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x, y):rs) | x == y = False
                              | pertenece (x, y) rs || pertenece (y, x) rs = False
                              | otherwise = relacionesValidas rs

-- problema pertenece (elemento: t, lista: seq<t>): Bool {
--  requiere {True}
--  asegura {res = True si y solo si elemento pertenece a lista}
-- }
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece _ [] = False
pertenece e (x:xs) | e == x = True 
                   | otherwise = pertenece e xs
personas :: [(String, String)] -> [String]
personas [] = []
personas (x:xs) = quitarRepetidos (elementosDeRelaciones (x:xs))

-- problema elementosDeRelaciones (relaciones: seq<StringxString>): seq<String>
--  requiere {relacionesValidas(relaciones)}
--  asegura  {res = [p1, p2] para todo (p1, p2) que pertenece a relaciones}
-- }
elementosDeRelaciones :: [(String, String)] -> [String]
elementosDeRelaciones [] = []
elementosDeRelaciones ((pa, pb):xs) = pa:pb:elementosDeRelaciones xs 

-- problema quitarRepetidos (lista: seq<T>): seq<T>
--  requiere {True}
--  asegura {x pertenece a res si y solo si existe un unico x en res}
-- }
quitarRepetidos :: (Eq t) => [t] -> [t]
quitarRepetidos [] = []
quitarRepetidos (x:xs) | pertenece x xs = quitarRepetidos xs 
                       | otherwise = x:quitarRepetidos xs

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe p ((a1, a2): rs) | a1 == p = a2:amigosDe p rs
                          | a2 == p = a1:amigosDe p rs
                          | otherwise = amigosDe p rs

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos (r:rs) = compararAmigos (r:rs) ps p
                            where (p:ps) = personas (r:rs)

compararAmigos :: [(String, String)] -> [String] -> String -> String
compararAmigos _ [] pma = pma
compararAmigos (r:rs) personas pma | cantAmigosP > cantAmigosMax = compararAmigos (r:rs) (tail personas) (head personas)
                                   | otherwise = compararAmigos (r:rs) (tail personas) pma
                                   where cantAmigosP = length (amigosDe (head personas) (r:rs))
                                         cantAmigosMax = length (amigosDe pma (r:rs))
p1 = "p1"
p2 = "p2"
p3 = "p3"
p4 = "p4"
p5 = "p5"
p6 = "p6"

r1 = (p1, p2)
r2 = (p3, p4)
r3 = (p5, p6)
r1_i = (p2,p1)
r1_eq = (p1, p1)

relacionesV = [r1, r2, r3, (p2, p3)]
relacionesI_1 = [r1, r2, r3, r1]
relacionesI_2 = [r1, r1_i, r2, r3]
relacionesI_3 = [r1, r1_eq, r2, r3]