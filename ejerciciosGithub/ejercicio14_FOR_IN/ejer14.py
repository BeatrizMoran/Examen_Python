lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]

diccionarioNumeros = {}

for num in lista:
    diccionarioNumeros[num] = lista.count(num)

print(diccionarioNumeros)