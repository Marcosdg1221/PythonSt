class Libro:
    def __init__(self, titulo, autor, num_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_prestados = 0

    def prestamo(self):
        if self.num_ejemplares > self.num_prestados:
            self.num_prestados += 1
            return True
        else:
            return False

    def devolucion(self):
        if self.num_prestados > 0:
            self.num_prestados -= 1
            return True
        else:
            return False

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Disponibles: {self.num_ejemplares}, Prestados: {self.num_prestados}'

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor

    def __lt__(self, other):
        if self.autor == other.autor:
            return self.titulo < other.titulo
        else:
            return self.autor < other.autor

libro1 = Libro("Esdr", "Bsqdrl")
libro2 = Libro("Wao", "Koask")
libro3 = Libro("rf", "th", 2)
print(libro1, libro2, libro3) 

if libro1 == libro3:
    print("son iguales.")
else:
    print("son diferentes.")

if libro1 < libro2:
    print(f"{libro1.titulo} va antes")
else:
    print(f"{libro2.titulo} va antes")