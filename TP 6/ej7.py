"""
7. Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un numero al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomo hallar
el número. Si el usuario introduce algo que no sea un numero se mostrara un
mensaje en pantalla y se lo contará como un intento más.

"""
import random

def juego_adivina_numero():
    numero_a_adivinar = random.randint(1, 500)
    intentos = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 500. ¿Puedes adivinar cuál es?")

    while True:
        try:
            numero_usuario = int(input("Introduce un número entre 1 y 500: "))
            intentos += 1 

            if not 1 <= numero_usuario <= 500:
                raise ValueError("El número debe estar entre 1 y 500.") 

            if numero_usuario < numero_a_adivinar:
                print("El número que buscas es mayor.")
            elif numero_usuario > numero_a_adivinar:
                print("El número que buscas es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError as e:
            print(f"Error: {e}. Cuenta como un intento.")

# Llamamos a la función para ejecutar el juego
juego_adivina_numero()
