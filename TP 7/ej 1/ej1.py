"""
1. Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPANA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:

Arslanian, Gustavo-> ARMENIA.TXT
Rossini, Giuseppe-> ITALIA.TXT
Pérez, Juan-> ESPAÑA.TXT
Smith, John-> descartar

El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""


try:
    
    arch = open(r"C:\Users\USUARIO\Documents\GitHub\Programacion-1\TP 7\ej 1\apellidos.txt", "rt")
    armenia = open("ARMENIA.TXT", "w")
    italia = open("ITALIA.TXT", "w")
    espana = open("ESPANA.TXT", "w")
    for linea in arch:
        apellido, nombre = linea.split(", ")
        if apellido[-3:] == "ian":
            armenia.write(linea)
        elif apellido[-3:] == "ini":
            italia.write(linea)
        elif apellido[-2:] == "ez":
            espana.write(linea)
except FileNotFoundError:
    print("No se pudo abrir el archivo")
except OSError:
    print("Error de E/S")
finally:
    try:
        arch.close()
        armenia.close()
        italia.close()
        espana.close()
    except NameError:
        pass  
