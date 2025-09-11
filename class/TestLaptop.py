from laptop import laptop


laptopPepitp=laptop("lenovo","i7",32)
laptopMaria=laptop("lenovo","i7",32,600)

for numero in range(1,1001):
    asusLaptop=laptop.asusLaptop(numero)
    print(asusLaptop.__dict__)
#print(laptop.compararCostos(laptopPepitp,laptopMaria))