#65º Diseña un programa que, dado un número entero, determine si éste es el doble de un número impar. (Ejemplo: 14 es
#el doble de 7, que es impar.

num = input(int("Introduce un numero entero:"))
if num % 2 == 0 and (num / 2) % 2 != 0:
    print(f"{num} es el doble de {(num/2)} que es impar")
else:
    print(f"{num} no es el doble de un numero impar")

# 66º Diseña un programa que, dados dos números enteros, determine si uno de ellos es múltiplo del otro. Que muestre el mensaje:
# <El segundo es el cuadrado exacto del primero.>, <El segundo es menor que el cuadrado del primero.> o <El segundo es
# mayor que el cuadrado del primero.>, dependiendo de la verificación de la condición correspondiente al significado de
# cada mensaje

num1 = input(int("Introduce numero 1: "))
num2 = input(int("Introduce numero 2: "))
if num2 == num1 ** 2:
    print(f"El segundo es el cuadrado exacto del primero.")
elif num2 < num1 ** 2:
    print(f"El segundo es menor que el cuadrado del primero.")
else:
    print(f"El segundo es mayor que el cuadrado del primero.")

# 68º Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de
# 500, 200, 100, 50, 20, 10 y 5$ y monedas de 2 y 1$.
# Por ejemplo, si deseamos conocer el desglose de 434$, el programa mostrará por pantalla el siguiente resultado:
# 2 billetes de 200 euros.
# 1 billete de 20 euros.
# 1 billete de 10 euros.
# 2 monedas de 2 euros.

cantidad = input(int("Introduce una cantidad exacta de euros: "))
billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
desglose = {}
for valor in billetes_monedas:
    if cantidad >= valor:
        num_billetes_monedas = cantidad // valor
        desglose[valor] = num_billetes_monedas
        cantidad -= num_billetes_monedas * valor

for valor, num in desglose.items():
    if valor >= 5:
        print(f"{num} billetes de {valor} euros.")
    else:
        print(f"{num} monedas de {valor} euros.")

# 82 Diseña un programa que calcule la menor de cinco palabras dadas; es decir, la primera palabra de las cinco en orden
# alfabético. No aceptaremos que las mayúsculas sean ✭✭alfabéticamente✮✮ menores que las minúsculas. O sea, ’pepita’ es
# menor que ’Pepito’

palabras = []
for i in range(5):
    palabra = input("Introduce la "+ i + " palabra: ")
    palabras.append(palabra)
menor_palabra = min(palabras)
print(f"La menor palabra en orden alfabetico es: {menor_palabra}")

# 83 Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano
# al primero. (Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más cercano al 2 es el 1. 

num1 = input(int("Introduce numero 1: "))
num2 = input(int("Introduce numero 2: "))
num3 = input(int("Introduce numero 3: "))
num4 = input(int("Introduce numero 4: "))
num5 = input(int("Introduce numero 5: "))

numeros = [num2, num3, num4, num5]
diferencia = num2 - num1
mas_cercano = num2
for numero in numeros:
    if abs(numero - num1) < abs(diferencia):
        diferencia = numero - num1
        mas_cercano = numero
print(f"El numero mas cercano a {num1} es {mas_cercano}")

# 104 Implementa un programa que muestre todos los múltiplos de n entre n y m ·n, ambos inclusive, donde n y m son
# números introducidos por el usuario

n = input(int("Introduce un numero n: "))
m = input(int("Introduce un numero m: "))
multiplos = []
for i in range(n, (m * n) + 1, n):
    multiplos.append(i)
print(f"Los multiplos de {n} entre {n} y {m*n} son: {multiplos}")

# 190 Una palabra es <alfabética> si todas sus letras están ordenadas alfabéticamente. Por ejemplo, <amor>, <chino> e
# <himno> son palabras <alfabéticas>. Diseña un programa que lea una palabra y nos diga si es alfabética o no

palabra = input("Introduce una palabra: ")
if list(palabra) == sorted(palabra):
    print(f"La palabra {palabra} es alfabetica")
else:
    print(f"La palabra {palabra} no es alfabetica")

# 194 Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido las vocales. Por ejemplo,
# el texto <.n .j.mpl. d. p.s.t..mp.s>, se descifra sustituyendo cada punto con una vocal del texto. La solución es <un
# ejemplo de pasatiempos>. Diseña un programa que ayude al creador de pasatiempos. El programa recibirá una cadena y
# mostrará otra en la que cada vocal ha sido reemplazada por un punto.

cadena = input("Introduce tu cadena de texto: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]

for i in list(cadena):
    if i == vocales.item():
        cadena[i] = "."

print(cadena)
# COMPROBAR

# 270 La última letra del DNI puede calcularse a partir del número. Para ello sólo tienes que dividir el número por 23 y
# quedarte con el resto, que es un número entre 0 y 22. La letra que corresponde a cada número la tienes en esta tabla:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# T R W A G M Y F P D X B N J Z S Q V H L C K E
# Define una función que, dado un número de DNI, devuelva la letra que le corresponde

dni_sin_letra = input(int("Introduce tu dni sin letra: "))

letra = {
    0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J",
    14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"
}

def letra_dni(dni_sin_letra):
    total = 0
    for i in dni_sin_letra:
        total =+ i

    num = total//23 
    print(f"La letra correspondiente a {dni_sin_letra} es {letra(num)}")
    return {letra(num)}

# COMPROBAR

# 272 Diseña una función llamada es_repeticion que reciba una cadena y nos diga si la cadena está formada mediante la
# concatenación de una cadena consigo misma. Por ejemplo, es_repeticion(’abab’) devolverá "True", pues la cadena ’abab’
# está formada con la cadena ’ab’ repetida; por contra es_repeticion(’ababab’) devolverá "False"

def es_repeticion():
    cadena = input("Introduce tu cadena de texto: ")
    return 


# 276 Define una función que devuelva el número de días que tiene un año determinado. Ten en cuenta que un año es
# bisiesto si es divisible por 4 y no divisible por 100, excepto si es también divisible por 400, en cuyo caso es bisiesto.
# (Ejemplos: El número de días de 2002 es 365: el número 2002 no es divisible por 4, así que no es bisiesto. El año 2004 es
# bisiesto y tiene 366 días: el número 2004 es divisible por 4, pero no por 100, así que es bisiesto. El año 1900 es divisible por
# 4, pero no es bisiesto porque es divisible por 100 y no por 400. El año 2000 sí es bisiesto: el número 2000 es divisible por 4
# y, aunque es divisible por 100, también lo es por 400. 

def año_bisiesto():
    return

# 289 Diseña una función que reciba una lista de cadenas y devuelva el prefijo común más largo. Por ejemplo, la cadena
# ’pol’ es el prefijo común más largo de esta lista:
# [’poliedro’, ’policía’, ’polífona’, ’polinizar’, ’polaridad’, ’política’]

def prefijo_more_comun():
    return


# 296 Haz una función que reciba un número de DNI y una letra. La función devolverá True si la letra corresponde a ese
# número de DNI, y False en caso contrario. La función debe llamarse comprueba_letra_dni .
# Si lo deseas, puedes llamar a la función letra_dni , desarrollada en el ejercicio 270, desde esta nueva función 

def comprueba_letra_dni(dni_sin_letra, letra):
    letra_real = letra_dni(dni_sin_letra)
    if letra == letra_real:
        return True
    else: 
        return False
    
# COMPROBAR

# 308 Tenemos los tiempos de cada ciclista y etapa participantes en la última vuelta ciclista local. La lista ciclistas contiene
# una serie de nombres. La matriz tiempos tiene una fila por cada ciclista, en el mismo orden con que aparecen en ciclistas.
# Cada fila tiene el tiempo en segundos (un valor flotante) invertido en cada una de las 5 etapas de la carrera. ¿Complicado?
# Este ejemplo te ayudará: te mostramos a continuación un ejemplo de lista ciclistas y de matriz tiempos para 3 corredores
# ciclistas = [’Pere Porcar’, ’Joan Beltran’, ’Lledó Fabra’]
# tiempo = [[10092.0, 12473.1, 13732.3, 10232.1, 10332.3],
# [11726.2, 11161.2, 12272.1, 11292.0, 12534.0],
# [10193.4, 10292.1, 11712.9, 10133.4, 11632.0]]
# En el ejemplo, el ciclista Joan Beltran invirtió 11161.2 segundos en la segunda etapa.
# Se pide:
# Una función que reciba la lista y la matriz y devuelva el ganador de la vuelta (aquel cuya suma de tiempos en las 5 etapas es mínima).
# Una función que reciba la lista, la matriz y un número de etapa y devuelva el nombre del ganador de la etapa.
# Un procedimiento que reciba la lista, la matriz y muestre por pantalla el ganador de cada una de las etapas.

def fruncion1 (ciclistas, tiempos): # Ganador de la vuelta (las 5 etapas)
    return

def fruncion2 (ciclistas, tiempos, etapa): # En base a una etapa, devolvemos el nombre del ganador de esa etapa
    return

def fruncion3 (ciclistas, tiempos): # Ganador de cada etapa
    return

# 468 (con un while al menos) Diseña un programa que obtenga los 100 primeros números primos y los almacene en un fichero de texto llamado primos.txt

def primos():
    return