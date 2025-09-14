from laptop import laptop

class laptopGaming(laptop):
    def __init__(self, marca, procesador, memoria,tarjetaGrafica, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.tarjetaGrafica=tarjetaGrafica

    def realizarDiagnosticoSistma(self):
        resultadoDiagnostico=super().realizarDiagnosticoSistma()
        ressultadoJuegos=self.realizarDiagnosticoJuegos()
        resultadoDiagnostico["Resultados juegos"]=ressultadoJuegos
        return resultadoDiagnostico


    def realizarDiagnosticoJuegos(self):
        juegos=["FRONITE","COD","GTA"]
        resultados={}
        for juego in juegos :
            fpsBase=30
            if "RTX" in self.tarjetaGrafica:
                fps=fpsBase*3
            elif "GTX" in self.tarjetaGrafica:
                fps=fpsBase*2 
            else:
                fps=fpsBase       

            resultados[juego]=f"{fps} FPS"
        return resultados        

    pass