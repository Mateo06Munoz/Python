nombrePaciente=[]
edad=[]
def agregarNombre(nombre):
    nombrePaciente.append(nombre)

def agregarEdad(anioNacimiento):
    edadActual=2025-anioNacimiento
    edad.append(edadActual)

def mostrarListas():
    print(f"Lista de Nombre \n {nombrePaciente}")
    print(f"Lista de Nombre \n {edad}")

def indentificarMayor():
    print(f"persona con mayor edad {max(edad)}")