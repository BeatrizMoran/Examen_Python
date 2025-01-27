import math

class Poligono:
    def __init__(self, color):
        self.color = color

class Triangulo(Poligono):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        s = self.perimetro() / 2 #semiperimetro
        return round(math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)))


    def forma(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"
        
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def __str__(self):
        return f"Triángulo de color {self.color}, lados ({self.lado1}, {self.lado2}, {self.lado3})"

class Cuadrado(Poligono):
    def __init__(self, color, lado):
        super().__init__(color)

        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4
    
    def __str__(self):
        return f"Cuadrado de color {self.color} con lado de {self.lado}"
    
triangulo = Triangulo("Rojo", 2, 3, 5)
cuadrado = Cuadrado("Verde", 4)

print(triangulo)  # Triángulo de color azul, lados (3, 4, 5)
print("Area: " , triangulo.area())
print("La forma del triangulo es: ", triangulo.forma())
print("El perimetro es: ", triangulo.perimetro())

print(cuadrado)  # Cuadrado de color rojo con lado de 5
print(f"Área del cuadrado: {cuadrado.area()}")
print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")

    
        
        
    