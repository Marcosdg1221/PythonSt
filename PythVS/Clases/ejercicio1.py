class CuentaCorriente:
    def __init__(self, dni, nombre="", saldo=0):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    def sacar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f'DNI: {self.dni}, nombre: {self.nombre}, saldo: {self.saldo}'

    def __eq__(self, other):
        return self.dni == other.dni

    def __lt__(self, other):
        return self.saldo < other.saldo

cuenta1 = CuentaCorriente("12345678A", "Juan", 1000)
cuenta2 = CuentaCorriente("87654321B", "María", 1500)
cuenta3 = CuentaCorriente("12345678A", "Juan", 2000)

print(cuenta1)  
print(cuenta2)  
print(cuenta3)  

if cuenta1 == cuenta3:
    print("Las cuentas son iguales.")
else:
    print("Las cuentas son diferentes.")

if cuenta1 < cuenta2:
    print(f"{cuenta1.nombre} tiene menos saldo.")
else:
    print(f"{cuenta2.nombre} tiene menos saldo.")