lista = []
for num1 in range (1,10 +1):
    num = int(input("pon numero"))
    lista.append(num)
    if num%2==0:
        print("Es par")
    else:
        print("Es impar")
print(lista)