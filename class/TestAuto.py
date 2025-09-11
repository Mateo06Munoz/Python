from auto import auto

autoMaria=auto("Ferari","clasico",2000,19000)
autoJose=auto("mercedes","lugoso",1996,20001)
AutoNatalia=auto("camaro","moderno",2010,1200000)

#print(autoMaria.mostrarInfirmacio())
#print(autoJose.actualizarKilometraje(1000000))
#print(AutoNatalia.realizarViaje(20000))
#autoMaria.estadoAuto()


toyotaAuto=auto.ToyotaAuto()
print(toyotaAuto.__dict__)

ferrariAuto=auto.ferariAuo()
print(ferrariAuto.__dict__)

print(auto.validarKilometraje(autoJose,AutoNatalia))
print(auto.validarAño(autoJose,AutoNatalia))

