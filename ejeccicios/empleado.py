from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, nombre, salariobase):
        self.nombre = nombre
        self.salariobase = salariobase

    @abstractmethod
    def calcularsalario(self):
        pass


class EmpleadoTiempoCompleto(empleado):
    def calcularsalario(self):
        return self.salariobase * 1.20  


class EmpleadoMedioTiempo(empleado):
    def calcularsalario(self):
        return self.salariobase * 1.10   
