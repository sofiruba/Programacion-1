"""
12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. 
Para ello, se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
    a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe aparecer una sola vez en el informe.
    b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. 
    Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.
"""
def digitos(num):
    n = str(num)
    li = list(map(int,n)) 
    while len(li) !=5:
        n = input("El número de socio debe tener 5 dígitos: ")
        li = list(map(int,n))
    return n
    
def cargarsocios():
    socios = []
    ingresos = []
    num_socio = int(input("Ingrese el número de socio de 5 dígitos: "))
    while num_socio != 0:
        n = digitos(num_socio)
        if num_socio in socios:
            print("El socio ya ingresó al club")
        else:
            socios.append(num_socio)
            ingreso = int(input("Ingrese el número de ingresos: "))
            ingresos.append(ingreso)
        num_socio = int(input("Ingrese el número de socio de 5 dígitos: "))
    return [socios, ingresos]

def informar(socios, ingresos):
    for i in range(len(socios)):
        print("El socio numero", socios[i], "ingresó", ingresos[i], "veces")

def darbaja(socios, ingresos):
    baja = int(input("Ingrese el número de socio que se dio de baja: "))
    while baja not in socios:
        baja = int(input("El socio no se encuentra en la lista. Ingrese el número de socio que se dio de baja: "))
    index = socios.index(baja)
    socios.remove(baja)
    eliminados = ingresos[index]
    ingresos.pop(index)
    print("El socio", baja, "fue eliminado y se eliminaron ", eliminados, " ingresos")
    print("Registros de entrada al club después de eliminarlo: ")
    informar(socios, ingresos)


socios, ingresos = cargarsocios()
informar(socios, ingresos)
darbaja(socios, ingresos)
