def cargarmatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input("Elemento: ")))
        matriz.append(fila)
    return matriz

def intercambiar_filas(filas, matriz):
    fila1 = filas[0]
    fila2 = filas[1]
    
    for i in range(len(matriz)):
        if i == fila1:
            for j in range (n):
                aux = matriz[i][j]
                matriz[i][j] = matriz[fila2][j]
                matriz[fila2][j] = aux
                
def intercambiar_columnas(columnas, matriz):
    c1 = columnas[0]
    c2 = columnas[1]
    
    for i in range(len(matriz)):
        if i == c1:
            for j in range (n):
                aux = matriz[j][i]
                matriz[j][i] = matriz[j][c2]
                matriz[j][c2] = aux

def transponer(matriz):
    transpuesta = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
    return transpuesta

def promediofila(fila):
    suma = 0
    for elemento in fila:
        suma += elemento
    return suma/len(fila)

def impares_columna(matriz, columna):
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][columna] % 2 != 0:
            contador += 1
    return contador

def imprimirmatriz(matriz):
    for i in range(len(matriz)):
        print("|", end=" ")
        for j in range(len(matriz)):
            print(matriz[i][j], end=" ")
        print("|")
# cargar matriz y ordenar ascendentemente
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = cargarmatriz(n)
matriz.sort()
imprimirmatriz(matriz)

# Intercambiar filas
primera_fila = int(input("ingresa la primera fila q quieras cambiar: "))
while 0>primera_fila or primera_fila> (n-1) :
    primera_fila = int(input("volve a ingresar la primera fila q quieras cambiar: "))

segunda_fila = int(input("ingresa la segunda fila q quieras cambiar: "))
while 0>segunda_fila or segunda_fila> (n-1) :
    segunda_fila = int(input("volve a ingresar la primera fila q quieras cambiar: "))
    
    
filas = [primera_fila, segunda_fila]
filas.sort()
intercambiar_filas(filas, matriz)
imprimirmatriz(matriz)

#Intercambiar columnas 
primera_columna = int(input("ingresa la primera columna q quieras cambiar: "))
while 0>primera_columna or primera_columna> (n-1) :
    primera_columna = int(input("volve a ingresar la primera columna q quieras cambiar: "))

segunda_columna = int(input("ingresa la segunda columna q quieras cambiar: "))
while 0>segunda_columna or segunda_columna> (n-1) :
    segunda_columna = int(input("volve a ingresar la primera columna q quieras cambiar: "))
    
    
columnas = [primera_columna, segunda_columna]
columnas.sort()
intercambiar_columnas(columnas, matriz)
imprimirmatriz(matriz)

# Transponer matriz
transpuesta = transponer(matriz)
imprimirmatriz(transpuesta)

# Promedio de una fila
fila = int(input("Ingrese la fila de la cual quiere saber el promedio: "))
while 0>fila or fila> (n-1) :
    fila = int(input("volve a ingresar la fila de la cual quiere saber el promedio: "))
print(promediofila(matriz[fila]))

# Cantidad de impares en una columna
columna = int(input("Ingrese la columna de la cual quiere saber la cantidad de impares: "))
while 0>columna or columna> (n-1) :
    columna = int(input("volve a ingresar la columna de la cual quiere saber la cantidad de impares: "))
print(impares_columna(matriz, columna))
