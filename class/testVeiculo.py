from veiculo import Auto
from veiculo import Moto

auto1 = Auto("Toyota", "Corolla", 2021, 4)
moto1 = Moto("Yamaha", "MT-07", 2022, "Deportiva")

print(f"Auto: {auto1.descripcion()}")
print(f"Moto: {moto1.descripcion()}")

vehiculos = [auto1, moto1, Auto("Honda", "Civic", 2020, 2), Moto("Suzuki", "Burgman", 2021, "Scooter")]

print("\nLista de vehículos:")
for vehiculo in vehiculos:
    print(vehiculo.descripcion())