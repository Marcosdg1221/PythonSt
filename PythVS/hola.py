print ("hola")
print ("""glr   
       owmfgeo""")

#comentario
a=1
b=2.5
c='a'
d="si"
suma=1+2.5
print(suma)
elevado=2**5
divideyquedatelaparteentera=5//2

cadena = "si"
print(cadena*2)


variable = input("introduzca algo") #es el scanner el input basicamente
print (res)

a1= int(input("Pon un numeeero"))
a2= int(input("Pon otro numeero"))


suma=a1+a2
print (suma)
#Si sumas a1+a2 y no has puesto INT(input(...)) te lo lee como cadena


if num % 2 ==0 and num%2<1: #and, or, not
    print("numero es par")
    print ("Condicion cumplida")
else:
       print ("es impar")
print ("al no estar esto tabulado, está fuera del if")
#para else if, usa elif

num=int(input("Pon un número"))
print("Su número es:",num)



while 1<=num:
       print(num)
       num+= 1
print (num)


for contador in range(1,101): #es un for each, empieza en uno y termina en 100
      print(contador)

for asf in range(1,101,-1): #va a menos 1
      print(asf)

cadena=input("pon cadena")
for caracter in cadena: #una cadena es un conjunto de caracteres
      print(caracter)




def suma(num1, num2): #funcion; el nombre de la funcion y los parametros
       res=num1+num2
       return res

print(suma(3,4))

from hola import *

diccionario={'C':1972, 'python': 1991, 'Java': 1996}
diccionario['C++']=1980
print (diccionario('C'))
for clave in diccionario:
      print(diccionario[clave])



class Persona:
      def __init__(self,nombre,edad): #constructor; self es this.
      self.nombre=nombre
      self.edad=edad

#En otra clase imaginate, (aplica a lo siguiente)

from Persona import *

per1=Persona("Si", 0)
print(toString.per1)

def__str__(self):
       cadena="Nombre: " self.nombre + "\n"
       cadena+="Edad: " + str(self.edad)
       return cadena