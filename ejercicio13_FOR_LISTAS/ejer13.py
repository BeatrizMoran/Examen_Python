lista1 = []
lista2 = []
listaNumerosComun = []

try:
    for i in range(1,11):
        if i <= 5:
            numero = int(input("Ingrese un numero para la primera lista: "))
            lista1.append(numero)
        else:
            numero = int(input("Ingrese un numero para la segunda lista "))
            lista2.append(numero)

    for num in lista1:
        if num in lista2:
            listaNumerosComun.append(num)

    print("Los numeros en comun son: ", listaNumerosComun)

except ValueError:
    print("Error, introduce un numero invalido")