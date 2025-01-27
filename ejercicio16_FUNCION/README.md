# Ejercicio16

Crea un programa que genere un número aleatorio del 1 al 10. El usuario tendrá que adivinarlo, y
el programa tras cada intento le indicará al usuario si el número es más alto, bajo o si ha acertado.
La lógica para dar la respuesta al usuario deberá estar incluida en una función a la que se llamará
tras cada intento.
Nota: Para la creación del número aleatorio, utiliza el siguiente código:
```python
from random import randint, uniform,random
numero = randint(0,10)
