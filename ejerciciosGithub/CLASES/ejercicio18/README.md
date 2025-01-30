# Ejercicio18

Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se
encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá
realizar los siguientes movimientos:
- Avanzar hacia adelante (A)
- Retroceder (R)
- Avanzar hacia la izquierda (I) o hacia la derecha (D)

El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método,
posicion_actual(), que indicará su posición en las coordenadas X e Y. Al crear el robot este se
inicializará a las coordenadas (0,0).
Puedes utilizar el siguiente código para probar la clase creada:
```python
miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    print(miRobot.posicion_actual())