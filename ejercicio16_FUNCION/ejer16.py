from random import randint


def ComprobarNumero(entrada, numero):
    if entrada == numero:
        return True
    elif numero > entrada:
        print("El número es mayor")
        return False
    else:
        print("El número es menor")
        return False


try:
    numero = randint(0, 10)
    print("El numero es: {}".format(numero))
    acertado = False

    while not acertado:
        entrada = int(input("Introduce un número entre 0 y 10: "))

        acertado = ComprobarNumero(entrada, numero)

    print("¡Has acertado!")

except ValueError:
    print("Error, introduce un número entero válido.")
