
try:
    numInicio = int(input("Ingrese el numero de inicio: "))
    numFinal = int(input("Ingrese el numero de fin: "))

    if numInicio > numFinal:
        print("El numero de inicio debe ser mayor que el numero final")
    else:
        sumaImpares = 0
        sumaPares = 0
        for i in range(numInicio, numFinal + 1):
            if i % 2 == 0:
                sumaPares += i
            else:
                sumaImpares += i

        print("Los pares suman " + str(sumaPares) + "\nLos impares suman " + str(sumaImpares))

except ValueError:
    print("Introduce un numero valido")