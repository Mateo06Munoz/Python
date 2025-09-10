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

autoMaria=auto("Ferari","clasico",2000,19000)
autoJose=auto("mercedes","lugoso",1996,20001)
AutoNatalia=auto("camaro","moderno",2010,1200000)

print(autoMaria.mostrarInfirmacio())
print(autoJose.actualizarKilometraje(1000000))
print(AutoNatalia.realizarViaje(20000))
autoMaria.estadoAuto()