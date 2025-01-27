class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ordenes_recibidas = []  

    def mueve(self, orden):
        orden = orden.lower()
        self.ordenes_recibidas.append(orden) 

        for movimiento in orden:
            match movimiento:
                case "a":  # Avanzar hacia adelante (aumentar Y)
                    self.y += 1
                case "r":  # Retroceder (disminuir Y)
                    self.y -= 1
                case "i":  # Avanzar hacia la izquierda (disminuir X)
                    self.x -= 1
                case "d":  # Avanzar hacia la derecha (aumentar X)
                    self.x += 1
                case "fin":
                    print("Fin del programa")
                case _:
                    print(f"Orden no válida: {movimiento}. Usa A, R, I, D o fin.")

    def posicion_actual(self):
        # Devuelve la posición actual en las coordenadas X e Y
        return self.x, self.y

    def obtener_ordenes(self):
        # Devuelve todas las órdenes recibidas
        return "".join(self.ordenes_recibidas)

    def movimientos_a_origen(self):
        # Calcula los movimientos necesarios para volver a la posición inicial (0, 0)
        movimientos = []
        if self.x > 0:
            movimientos.append("i" * self.x)  # Moverse a la izquierda si X es positivo
        elif self.x < 0:
            movimientos.append("d" * abs(self.x))  # Moverse a la derecha si X es negativo

        if self.y > 0:
            movimientos.append("r" * self.y)  # Moverse hacia atrás si Y es positivo
        elif self.y < 0:
            movimientos.append("a" * abs(self.y))  # Moverse hacia adelante si Y es negativo

        return "".join(movimientos)

miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    if orden != 'fin':
        miRobot.mueve(orden)
        print("Posición actual:", miRobot.posicion_actual())
        print("Órdenes recibidas:", miRobot.obtener_ordenes())
        print("Movimientos para volver al origen:", miRobot.movimientos_a_origen())
