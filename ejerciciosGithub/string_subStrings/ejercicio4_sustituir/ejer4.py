frase = input("Ingresa una frase: ")

letra1 = input("Ingresa la letra que quieres sustituir: ")
letra2 = input("Ingresa la letra por la que quieres sustituir: ")

if len(letra1) != 1 or len(letra2) != 1:
    print("Introduce solo una letra.")
else:
    apariciones = frase.count(letra1)
    frase = frase.replace(letra1, letra2)
    print(apariciones, " apariciones. ", frase)
