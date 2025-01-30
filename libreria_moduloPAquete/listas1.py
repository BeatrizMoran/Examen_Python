#Dada una lista de números, crea una función que devuelva el promedio de esos números.

def calcularPromedio(numeros: list[int]) -> float:
    suma = 0
    if len(numeros) > 0:  # Usamos len() para comprobar si la lista tiene elementos
        for num in numeros:
            suma += num
        promedio = suma / len(numeros)  # Dividimos entre la cantidad de números
        return promedio
    else:
        print("La lista está vacía")
        return None  # Retornamos None si la lista está vacía

print("Introduce un número o 'fin' para terminar")
n = input()
numeros = []

while n != "fin":
    if n.isdigit():  # Verificamos si la entrada es un número entero
        numeros.append(int(n))  # Convertimos a entero antes de agregar
    else:
        print("Entrada no válida, introduce un número entero")
    print("Introduce un número o 'fin' para terminar")
    n = input()

promedio = calcularPromedio(numeros)

if promedio is not None:
    print("El promedio es:", promedio)
