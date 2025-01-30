from tokenize import String

mayor = None

while True:
    num = input("Introduce un número o 'fin' para terminar: ")

    if num.lower() == 'fin':
        break

    try:
        numero = float(num)

        if mayor is None or numero > mayor:
            mayor = numero
    except ValueError:
        print("Error, introduce un número válido.")

if mayor is not None:
    print(f"El mayor número ingresado es: " , mayor)
else:
    print("No se ingresaron números.")