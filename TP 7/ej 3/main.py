"""
3. Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
proximos Juegos Panamericanos. Para eso encargo la realizacion de un programa
que incluya las siguientes funciones:
"""

def GrabarRangoAlturas():
    arch = open("alturas.txt", "w")
    deporte = input("Ingrese el nombre del deporte: ")
    while deporte:
        arch.write(deporte + "\n") 
        altura = input("Ingrese la altura del atleta: ")
        while altura:
            arch.write(altura + "\n")
            altura = input("Ingrese la altura del atleta: ")
        deporte = input("Ingrese el nombre del deporte: ")
    arch.close()

"""
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:

<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
"""
def GrabarPromedio():
    try:
        arch = open("alturas.txt", "r")
        arch_promedio = open("promedios.txt", "w")
        deporte = arch.readline().strip()
        while deporte:
            suma = 0
            cantidad = 0
            altura = arch.readline().strip()
            while altura:
                if altura.isnumeric(): 
                    try :
                        suma += int(altura)  # Cambia a int solo si es un número
                        cantidad += 1
                    except ValueError:
                        print(f"Valor no válido para altura: {altura}. Se omite.")  # Manejo del error
                altura = arch.readline().strip()
            if cantidad > 0:  # Asegurarse de que no se divida por cero
                promedio = suma / cantidad
                arch_promedio.write(deporte + "\n")
                arch_promedio.write(str(promedio) + "\n")
            deporte = arch.readline().strip()
        
        arch.close()
        arch_promedio.close()  # Cerrar el archivo de promedios también
    except Exception as e:
        print(f"Error: {e} 2")
        return
"""
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""

def MostrarMasAltos():
    try:
        arch_promedios = open("promedios.txt", "r")
        arch_alturas = open("alturas.txt", "r")
        deporte_prom = arch_promedios.readline().strip()
        while deporte_prom:
            deporte_alt = arch_alturas.readline().strip()
            if deporte_alt == deporte_prom:
                promedio = float(arch_promedios.readline().strip())
                altura = arch_alturas.readline().strip()
                cont = 0
                while altura.isnumeric():
                    if float(altura) > float(promedio):
                        cont += 1
                    altura = arch_alturas.readline().strip()
                if cont > 0:
                    print(f"en el deporte: {deporte_alt} hay jugadores que superan la altura promedio")  
            deporte_prom = arch_promedios.readline().strip()
            deporte_alt = arch_alturas.readline().strip()

    except Exception as e:
        print(f"Error: {e}, aca 3")
        return
    
GrabarRangoAlturas()
GrabarPromedio()
MostrarMasAltos()