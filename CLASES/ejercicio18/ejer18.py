class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def mueve(self, orden):
        orden = orden.lower()

        if orden == "A":  # Avanzar hacia adelante (aumentar Y)
            self.y += 1
        elif orden == "R":  # Retroceder (disminuir Y)
            self.y -= 1
        elif orden == "I":  # Avanzar hacia la izquierda (disminuir X)
            self.x -= 1
        elif orden == "D":  # Avanzar hacia la derecha (aumentar X)
            self.x += 1
        elif orden == "fin":
            print("Fin del programa")
        else:
            print("Orden no válida. Usa A, R, I, D o fin.")

        """
        CON SWITCH CASE
        match orden:
            case "A":  # Avanzar hacia adelante (aumentar Y)
                self.y += 1
            case "R":  # Retroceder (disminuir Y)
                self.y -= 1
            case "I":  # Avanzar hacia la izquierda (disminuir X)
                self.x -= 1
            case "D":  # Avanzar hacia la derecha (aumentar X)
                self.x += 1
            case "fin":
                print("Fin del programa")
            case _:
                print("Orden no válida. Usa A, R, I, D o fin.")
        """

    def posicion_actual(self):
        return self.x, self.y

miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    if orden != 'fin':
        miRobot.mueve(orden)
        print("Posición actual:", miRobot.posicion_actual())