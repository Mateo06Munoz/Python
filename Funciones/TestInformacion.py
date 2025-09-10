import Infromacion

cantidad=int(input("Cantidad de pacientes: "))

for i in range(cantidad):
    nombre=input("Ingresa el nombre: ")
    edad=int(input("Ingresa año de nacimiento: "))
    Infromacion.agregarNombre(nombre)
    Infromacion.agregarEdad(edad)

Infromacion.mostrarListas()
Infromacion.indentificarMayor()