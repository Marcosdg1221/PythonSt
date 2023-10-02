numero = int(input("Pon numero filas y columnas"))

for i in range(1, numero + 1):
    print((" " * (numero - i)) + (" *" * i))

import random
numero1=random.randint(1,100)