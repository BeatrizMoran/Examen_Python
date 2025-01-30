import math


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
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
            return "Irregular"
        
        
    def perimetro(self):
        # Devuelve el perímetro del triángulo
        return self.lado1 + self.lado2 + self.lado3
    
triangulo = Triangulo(2, 2, 2)


print("Area: " , triangulo.area(), 2)
print("La forma del triangulo es: ", triangulo.forma())
print("El perimetro es: ", triangulo.perimetro())
