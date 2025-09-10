menu=["bolon","ceco de pollo","salchipapa","papipollo","sopa","susi","papas con cuero","cangrejo","camarones","conchas"]


platoAnadir=input("Añadir plato al menu: ")
platoBuscar=input("buscar en el menu: ")
platoEliminar=input("eliminar plato del menu: ")


menu.append(platoAnadir) #añadir plato al menu 
print(menu.index(platoBuscar)) #buscar plato del menu
menu.remove(platoEliminar) # eliminer plato del menu
print(menu)