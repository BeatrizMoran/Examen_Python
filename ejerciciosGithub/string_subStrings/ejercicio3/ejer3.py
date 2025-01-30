try:
    n1 = int(input("Introduce la posición de inicio: "))
    n2 = int(input("Introduce la longitud del substring: "))
    frase = input("Introduce la frase: ")

    if n1 < 0 or n1 >= len(frase):
        raise ValueError("La posición de inicio está fuera del rango de la frase.")
    if n2 < 0:
        raise ValueError("La longitud del substring debe ser positiva.")

    print("Substring:", frase[n1:n1 + n2])

except ValueError as e:
    print("Error:", e)
except IndexError:
    print("Error: Los índices están fuera del rango de la frase.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
