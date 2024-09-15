
def imprimirmatriz(matriz):
    for i in range(len(matriz)):
        print("|", end=" ")
        for j in range(len(matriz)):
            print(matriz[i][j], end=" ")
        print("|")


""" A: 
def impar(x):
    return 2*x+1
def generarmatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(impar(i))
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz
"""
""" b:
def generarmatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i + j == n-1:
                fila.append(3**j)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz
"""

""" c:
def generarmatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i <= j: 
                fila.append(i+1)
            else:
                fila.append(0)
        fila.reverse()
        matriz.append(fila)
    matriz.reverse()

    return matriz
"""
"""
d:
def generarmatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(2**i)
        matriz.append(fila)
    matriz.reverse()
    return matriz

"""
""" e: 
def esimpar(n):
    return n%2 != 0
def generar_matriz(n):
    matriz = []
    contador = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if  i == j:
                fila.append(0)
            elif (not esimpar(j) and not esimpar(i) or (esimpar(j) and esimpar(i))): 
                fila.append(0)
            
            else:
                fila.append(contador)
                contador = contador+ 1
            
        matriz.append(fila)
    return matriz

"""
""" f:
def generar_matriz(n):
    matriz = []
    contador = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(contador)
                contador = contador + 1
            elif j < i + 1: 
                fila.append(contador)
                contador = contador + 1
            else:
                fila.append(0)
        fila.reverse()
        matriz.append(fila)

    return matriz

"""
"""g: 
def generar_matriz(n):
    matriz = [[0] * n for _ in range(n)]  # Crear la matriz vacía de nxn
    contador = 1  # Iniciar el contador
    f, c = 0, 0  # Coordenadas iniciales (fila y columna)
    limite = n - 1  # Límite inicial
    
    while contador <= n * n:
        # Llenar hacia la derecha
        while c <= limite and matriz[f][c] == 0:
            matriz[f][c] = contador
            contador += 1
            c += 1
        c -= 1
        f += 1
        
        # Llenar hacia abajo
        while f <= limite and matriz[f][c] == 0:
            matriz[f][c] = contador
            contador += 1
            f += 1
        f -= 1
        c -= 1
        
        # Llenar hacia la izquierda
        while c >= 0 and matriz[f][c] == 0:
            matriz[f][c] = contador
            contador += 1
            c -= 1
        c += 1
        f -= 1
        
        # Llenar hacia arriba
        while f > 0 and matriz[f][c] == 0:
            matriz[f][c] = contador
            contador += 1
            f -= 1
        f += 1
        c += 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Solicitar el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
m = generar_matriz(n)
imprimir_matriz(m)
"""
"""h: 
def generar_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for col in range(n):
        col_aux = col
        fil = 0
        matriz[fil][col_aux] = contador
        contador += 1
        while col_aux > 0:
            col_aux = col_aux - 1
            fil = fil + 1
            matriz[fil][col_aux] = contador
            contador += 1
        # Cuando ya se lleno toda la fila 0 ( hasta el contador = 10)

        if col == n - 1:
            for fil in range(1,n):
                col_aux = col
                while fil < n :
                    matriz[fil][col_aux] = contador
                    contador += 1
                    fil += 1
                    col_aux -= 1
               
    return matriz
"""
def generar_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for col in range(n):
        col_aux = col
        fil = 0
        matriz[fil][col_aux] = contador
        contador += 1
        if col_aux % 2 !=0:
            while col_aux > 0:
                col_aux = col_aux - 1
                fil = fil + 1
                matriz[fil][col_aux] = contador
                contador += 1
        else:
            if fil!= 0 and col_aux!= 0:
                fil = col
                col_aux = 0
                while fil > 0:
                    col_aux = col_aux + 1
                    fil = fil - 1
                    matriz[fil][col_aux] = contador
                    contador += 1
        # Cuando ya se lleno toda la fila 0 ( hasta el contador = 10)

        if col == n - 1:
            for fil in range(1,n):
                col_aux = col
                while fil < n :
                    matriz[fil][col_aux] = contador
                    contador += 1
                    fil += 1
                    col_aux -= 1
               
    return matriz


# Solicitar el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
m = generar_matriz(n)
imprimirmatriz(m)

