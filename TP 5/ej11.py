def contarvocales(frase):
    vocales = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for palabra in frase:
        for letra in palabra:
            if letra in vocales:
                vocales[letra] += 1
        
    return vocales

p = input("ingrese una palabra: ")
lista = p.split()
print(contarvocales(lista))