# Ingresar num y que me imprima en texting

unos = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
miles = ["", "mil", "millón", "mil millones", "billón"]

text = ""
num = int(input("Ingrese un número: "))
while num < 0 or num > 1*10**12:
    num = int(input("Ingrese un número valido: "))

lista_num = list(map(int, str(num)))
print(lista_num)
for i in range(len(lista_num), 0, -1):
    digit = lista_num[len(lista_num) - i]
    if i % 3 == 1:
        if len(lista_num) != 4 or digit != 1:
            text += unos[digit] + " "
    elif i % 3 == 2:
        text += decenas[digit] + " "
    elif i % 3 == 0:
        text += centenas[digit] + " "
    if i % 3 == 1 and i // 3 > 0:
        text += miles[i // 3] + " "

print(text)