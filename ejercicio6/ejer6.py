try:
    num = int(input("Ingresa un numero: "))

    if num < 0:
        print("Es un número negativo")
    elif num > 0:
        print("Es un número positivo")
    else:
        print("Es igual a cero")

except ValueError:
    print("Introduce un número válido")
