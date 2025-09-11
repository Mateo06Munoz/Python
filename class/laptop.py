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

    @staticmethod
    def compararCostos(laptap1,laptop2):
        if laptap1.costo == laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    @classmethod
    def asusLaptop(cls,costo):
        marca="asus"
        procesador="i5"
        memoria=16
        return cls(marca,procesador,memoria,costo)