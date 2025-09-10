
datos=[]

cantidad=int(input("Cuántos datos desea ingresar: "))

for i in range(cantidad):
    valor=input(f"Ingrese el dato {i+1}: ")


    if valor.isdecimal():
        datos.append(int(valor))
    else:
        datos.append(valor)


print(f"Su lista es: {datos}")