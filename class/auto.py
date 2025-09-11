class auto():
    def __init__(self,marca,modelo,año,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.kilometraje=kilometraje

    def mostrarInfirmacio(self):
        return self.marca , self.modelo ,self.año 
    
    def actualizarKilometraje(self,kilometrajeN):
        if self.kilometraje > kilometrajeN:
            print("No se puede reducir el kilometraje")
        else:
            self.kilometraje=kilometrajeN
            return self.kilometraje

    def realizarViaje(self,kilometros):
        if kilometros>-1:
            self.kilometraje =self.kilometraje+kilometros
            return self.kilometraje
        else:
            return "La cantidad de kilómetros debe ser positiva"

    def estadoAuto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje>20000 and self.kilometraje< 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    @classmethod
    def ToyotaAuto(cls):
        marca="Toyota"
        modelo="deportivo"
        año=2025
        return cls(marca,modelo,año)
    
    @classmethod
    def ferariAuo(cls):
        marca="ferrari"
        modelo="moderno"
        año=2000
        return cls(marca,modelo,año)
    
    @staticmethod
    def validarKilometraje (auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return"Los dos autos tiene el mismo kilometraje"
        return"El kilometraje de los autos son diferentes"

    @staticmethod
    def validarAño (auto1,auto2):
        if auto1.año == auto2.año:
            return"Los dos autos tiene el mismo año"
        return"El año de los autos son diferentes"