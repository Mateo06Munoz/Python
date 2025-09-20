class vehiculo:
    def __init__(self,marca,modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"   

class Auto(vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        return super().descripcion() + f", Puertas: {self.num_puertas}"
    
class Moto(vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def descripcion(self):
        return super().descripcion() + f", Tipo: {self.tipo}"

    pass    