class laptop:
    def __init__(self,marca,procesador,memoria,costo=500,impuestos=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuestos=impuestos

    def valorFinal(self):
        return self.costo + self.impuestos
    
    def valorDescuento(self,descuento):
        return (self.costo* descuento)/100

laptopPepitp=laptop("lenovo","i7",32)

print(laptopPepitp.__dict__)
print(laptopPepitp.valorFinal())
print(f"el valor de desucento: {laptopPepitp.valorDescuento(10)}")