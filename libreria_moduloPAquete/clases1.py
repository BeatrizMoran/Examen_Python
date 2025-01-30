#Crea una clase Persona que tenga los atributos nombre, edad y ciudad. Añade un método que imprima la presentación de la persona, como "Hola, soy [nombre], tengo [edad] años y vivo en [ciudad]."

class Persona:
    nombre: str
    edad: int
    ciudad: str

    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def presentacion(self):
        print("Hola soy ", self.nombre, " tengo ", self.edad, " años y vivo en ", self.ciudad)


per1 = Persona("Beatriz", 20, "Vitoria")
per1.presentacion()
        