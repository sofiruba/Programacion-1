"""
1. Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:

a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N dias a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al dia anterior. En ningun
caso la diferencia en horas puede superar las 24 horas.
"""

def bisiesto(a):
    match a:
        case x if x%100 == 0 and x %400 == 0:
            return True
        case x if x % 100 == 0:
            return False
        case x if x % 4 == 0:
            return True
        case _:
            return False


def dias_del_mes(m, a):
    meseslargos = (1,3,5,7,8,10,12)
    mesesmedios = [4,6,9,11]
    if m in meseslargos:
        return 31
    elif m in mesesmedios:
        return 30
    elif m == 2 and bisiesto(a):
        return 29
    else:
        return 28

def ingresar_fecha():
    año = int(input("Ingrese el año de la fecha que desea ingresar: "))
    while año not in range(0, 2025):
        año = int(input("Ingrese un año válido: "))
    
    mes = int(input("Ingrese el mes de la fecha que desea ingresar: "))
    while mes not in range(1, 13):
        mes = int(input("Ingrese un mes válido: "))
    
    dias_validos = dias_del_mes(mes, año)
    dia = int(input("Ingrese el día de la fecha que desea ingresar: "))
    while dia not in range(1, dias_validos + 1):
        dia = int(input("Ingrese un día válido: "))
    
    return (dia, mes, año)

def sumardias(n, fecha):
    dia, mes , año = fecha
    dia = dia + n
    while dia > dias_del_mes(mes, año):
        dia -= dias_del_mes(mes, año)
        mes += 1
        if mes > 12:
            mes = 1
            año += 1
    return (dia, mes, año)


def ingresar_horario():
    hora = int(input("Ingrese la hora en formato 24 hs"))
    while hora not in range(0, 24):
        hora = int(input("Ingrese una hora válida (0-23): "))
    
    minuto = int(input("Ingrese los minutos (0-59): "))
    while minuto not in range(0, 60):
        minuto = int(input("Ingrese minutos válidos (0-59): "))
    return (hora, minuto)

def diferencia_horarios(horario1, horario2):
    hora1, min1 = horario1
    hora2, min2 = horario2
    total1 = hora1*60 + min1
    total2 = hora2*60 + min2
    if total1 > total2:
        total2 = total2 + 24*60
    diferencia = total2 - total1
    return (diferencia//60, diferencia%60)


fecha = ingresar_fecha()
n = int(input("Ingrese cuantos dias quiere sumarle a la fecha: "))

nueva_fecha = sumardias(n, fecha)
print(nueva_fecha)

primer_horario = ingresar_horario()
segundo_horario = ingresar_horario()
diferencia_hora = diferencia_horarios(primer_horario, segundo_horario)
print(diferencia_hora)

