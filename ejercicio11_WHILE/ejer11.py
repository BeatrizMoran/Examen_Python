numeros = []

for i in range(1, 6):
    num_valido = False
    while not num_valido:
        try:
            num = int(input(f"Introduce el número {i}: "))
            numeros.append(num)
            num_valido = True
        except ValueError:
            print("Introduce un número válido.")

print("El número mayor es:", max(numeros))
