

intentos = 3
correcto = False

while intentos > 0 and correcto == False:
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")

    if usuario == "root" and password == "toor":
        print("Bievenido!")
        correcto = True
    else:
        intentos -= 1
        print("Datos incorrectos.Te quedan " + str(intentos) + " intentos")
        if intentos == 0:
            print("Has agotado los intentos")

