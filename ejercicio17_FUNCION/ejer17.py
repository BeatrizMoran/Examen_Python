lista =  [6,14,11,3,2,1,15,19]
rangoCorrecto = False
numeroEnLista = False


def ComprobarRango(numero):
    if numero > 1 and numero <= 20:
        return True

def ComprobarLista(numero):
    if numero in lista:
        return True

try:
    numero = int(input("Ingrese un numero del 1-20: "))
    rangoCorrecto = ComprobarRango(numero)
    numeroEnLista = ComprobarLista(numero)

    if not rangoCorrecto:
        print("El rango del numero es invalido")
    elif not numeroEnLista:
        print("El numero no esta en la lista")
    else:
        print("El rango del numero es correcto y esta en la lista")


except ValueError:
    print("Introduce un numero valido")

