
try:
    numInicio = int(input("Ingrese el numero de inicio: "))
    numFinal = int(input("Ingrese el numero de fin: "))

    if numInicio > numFinal:
        print("El numero de inicio debe ser mayor que el numero final")
    else:
        suma = 0
        for i in range(numInicio, numFinal + 1):
            suma += i

        print("El resultado es: " + str(suma))

except ValueError:
    print("Introduce un numero valido")