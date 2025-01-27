cadena = input("Introduce una cadena de texto: ")

longitudCadena = len(cadena)

if longitudCadena >= 3:
    a = cadena[:3]
    b = cadena[-3:]
    print(a+b)
else:
    print("Introduce una cadena de mas de 3 caracteres")


