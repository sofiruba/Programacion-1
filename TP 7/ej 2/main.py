"""
2. Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electronico. 
El tamano maximo de las partes se
ingresa por teclado.
Los nombres de los archivos generados deben respetar el nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la particion debe efectuar-
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""

tamaño = int(input("Ingrese el tamaño máximo de las partes: "))
try: 
    arch = open(r"C:\Users\USUARIO\Documents\GitHub\Programacion-1\TP 7\ej 2\archivo.txt", "rt") # abro archivo
    parte = 1 # inicializo parte
    tamaño_actual = 0
    nombre_parte = f"parte{parte}.txt"
    contenido = ""
    for linea in arch:
        tamaño_linea = len(linea)
        if tamaño_linea > tamaño:
            print("Error: linea excede el tamaño máximo")
            arch.close()
            break

        if tamaño_linea + tamaño_actual > tamaño:
            if contenido:
                arch_parte = open(nombre_parte, "w")
                arch_parte.write(contenido)
                arch_parte.close()
                print(f"Parte {parte} creada")
                contenido = ""
                parte += 1
                nombre_parte = f"parte{parte}.txt"
                tamaño_actual = tamaño_linea
        
        contenido += linea
        tamaño_actual += tamaño_linea
    if contenido:
        arch_parte = open(nombre_parte, "w")
        arch_parte.write(contenido)
        arch_parte.close()
        print(f"Parte {parte} creada")
        contenido = ""
        parte += 1
        nombre_parte = f"parte{parte}.txt"
        tamaño_actual = 0
    arch.close()
except Exception as e:
    print(f"Error: {e}")
