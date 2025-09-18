import random
from laptop import laptop

class laptapBusiness(laptop):
    def __init__(self, marca, procesador, memoria, espacio, duracionBateria,costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.espacio=espacio
        self.duracionBateria=duracionBateria

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n  espacio: {self.espacio}\n Duracion de bateria: {self.duracionBateria} \nCosto {self.costo}\n Impuestos {self.impuestos}"

    def realizarDiagnosticoSistma(self):
        dignostico=super().realizarDiagnosticoSistma()  
        resultado=self.verificarCopnectividadRed()
        dignostico["Resultados"]=resultado
        return dignostico
  


    def verificarCopnectividadRed(self):
        resultado={
            "Wifi ": "Ok" if random.choice([True,False])else "no hay señal wifi",
            "latencia":"Ok" if random.choice([True,False])else "red lenta",
            "servidores":"Ok" if random.choice([True,False])else "no hay servidores"
        }
        return resultado

    pass