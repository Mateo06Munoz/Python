from laptop import laptop
from laptapGaming import laptopGaming
from laptapBusiness import laptapBusiness


def imprimirInforme(Laptop):
    informe=Laptop.realizarInformeUso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")



laptopPepito=laptop("lenovo","i7",32)
laptopMaria=laptop("lenovo","i7",32,600)

laptopJuanito=laptopGaming("MSI","i7",4,"RTX 8GB")
laptopNatalia=laptapBusiness("MSI","i7",4,"RTX 8GB",100,2)

print("PEPITO: ")
imprimirInforme(laptopPepito)

print("JUEANITO: ")
imprimirInforme(laptopJuanito)