class Articulo:
    def __init__(self, nombre="", saldo=0, cuantosQuedan=0, precio=0):
        self.nombre = nombre
        self.saldo = saldo
        self.cuantosQuedan= cuantosQuedan
        self.iva=21
        self.precio=precio

    def getPVP(self, precio, iva):
        return precio+(precio*(iva/100))

    def getPVPDescuento(self,descuento):
        return self.getPVP()-(self.getPVP()*descuento/100)
    
    def vender(self,cantidad):
        res=False
        if cantidad<=self.cuantosQuedan:
            self.cuantosQuedan-=cantidad
            res=True
        return res
    
    def almacenar(self,cantidad,descuento):
        self.cuantosQuedan+=cantidad

    def __str__(self):
        res="Nombre: " + self.nombre
        res+="Cantidad:" + str(self.cuantosQuedan)
        res+="Precio" + str(self.precio)

    def __eq__(self, __value: object) -> bool:
        res=False
        if self.nombre==object.nombre:
            res=True
        return res