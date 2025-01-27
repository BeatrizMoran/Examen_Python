try:
    num = int(input("Ingresa el numero de la tabla de multiplicar: "))

    if num < 1 or num > 10:
        print("Introduce un numero entre 1-10")
    else:
        tabla = ""
        for i in range(1, 11):
            tabla += str(num) + " X " + str(i) + " = " + str(num * i) + "\n"
        print(tabla)

except ValueError:
    print("Introduce un numero valido")


