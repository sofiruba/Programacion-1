"""
Ejercicio 8:
Utilizar la tecnica de listas por comprensión para construir una lista con todos los numeros impares entre 100 y 200.
"""
impares = list(map(lambda x: x, [x for x in range(100,200) if x%2!=0]))
print(impares)

"""
Ejercicio 9:
Generar e imprimir una lista por compresion entre A y B con los multiplos de 7 que no sean multiplos de 5. 
A y B se ingresan por teclado.
"""

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
multiplos = list(map(lambda x:x, [x for x in range(a,b) if x%7==0 and x%5!=0]))
print(multiplos)

"""
Ejercicio 10:
Generar una lista con numeros random entre 1-100 y crear una nueva lista con los elementos de la primera que sean impares.
 usar filter. imprimir dos listas
"""
import random
lista = [random.randint(1,100) for x in range(10)]
imp = list(filter(lambda x: x%2!=0, lista))
print(imp)