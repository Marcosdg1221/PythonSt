from articulo import *

art1 =Articulo("Boli", 1.5,10)
art2=Articulo("Lapiz", 0.8, 30)

lista=[art1, art2]
lista.sort(reverse=True)
for art in lista:
    print(art)