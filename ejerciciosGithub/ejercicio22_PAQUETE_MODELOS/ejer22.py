from calculadora import aritmetica , geometria

"""
no usar prefijo:
from calculadora.aritmetica import *
from calculadora.geometria import *
"""

print("Suma: " , aritmetica.sumar(2,2))
print("Resta: " , aritmetica.restar(2,2))
print("Multiplicacion: " , aritmetica.multiplicar(2,2))
print("Division: " , aritmetica.dividir(2,2))

print("Area circulo: " , geometria.calcularArea(4))