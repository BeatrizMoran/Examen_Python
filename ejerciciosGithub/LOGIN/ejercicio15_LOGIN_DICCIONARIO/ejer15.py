contador = 0
usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermin",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
        }
}

loginCorrecto = False

while contador < 3 and not loginCorrecto:
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if usuario in usuarios:
        if usuarios[usuario]["password"] == password:
            print(f"Bienvenido: {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}")
            loginCorrecto = True
        else:
            print("Error, contraseña incorrecta")
    else:
        print("Error, usuario incorrecto")

    contador += 1

if contador == 3 and not loginCorrecto:
    print("Login fallido. Número de intentos superados.")