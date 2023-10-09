{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
-- NOTA: 10
-- 1
golesDeNoGoleadores :: [(String, String)] -> [Int] -> Int -> Int
golesDeNoGoleadores goleadoresPorEquipo goles totalesGolesTorneo = totalesGolesTorneo - sumatoriaGoles goles

sumatoriaGoles :: [Int] -> Int
sumatoriaGoles [] = 0
sumatoriaGoles (x:xs) = x + sumatoriaGoles xs

-- 2
-- interpreto que es imposible que hayan 2 jugadores con el mismo nombre jugando en equipos distintos
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((equipo, jugador): xs) | perteneceAEquipo equipo xs || perteneceAEquipo jugador xs || perteneceAJugador equipo xs || perteneceAJugador jugador xs || jugador == equipo = False
                                       | otherwise = equiposValidos xs

perteneceAJugador :: String -> [(String, String)] -> Bool
perteneceAJugador _ [] = False
perteneceAJugador e ((equipo, jugador):xs) | e == jugador = True
                                           | otherwise = perteneceAJugador e xs

perteneceAEquipo :: String -> [(String, String)] -> Bool
perteneceAEquipo _ [] = False
perteneceAEquipo e ((equipo, jugador):xs) | e == equipo = True
                                          | otherwise = perteneceAEquipo e xs

-- 3
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles jugador ((equipo, goleador):gs) (cantGoles:cs) = division golesDeJugador golesDeGoleadores * 100
                                                                where golesDeGoleadores = sumatoriaGoles (cantGoles: cs)
                                                                      golesDeJugador = obtenerGolesDeJugador jugador ((equipo, goleador): gs) (cantGoles: cs)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b) 

obtenerGolesDeJugador :: String -> [(String, String)] -> [Int] -> Int
obtenerGolesDeJugador jugador ((equipo, goleador):gs) (cantGoles: cs) | goleador == jugador = cantGoles
                                                                      | otherwise = obtenerGolesDeJugador jugador gs cs

-- 4
botinDeOro :: [(String, String)] -> [Int] -> String
botinDeOro ((equipo, goleador):gs) (cantGoles:cs) | esMaximo cantGoles cs = goleador
                                                  | otherwise = botinDeOro gs cs

esMaximo :: Int -> [Int] -> Bool
esMaximo _ [] = True
esMaximo e (x:xs) | e < x = False
                  | otherwise = esMaximo e xs