#listas

planetas=["Mercurio","venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno",5,40.5,True]
# print(planetas[-3])
# print(planetas[2:])
# print(len(planetas))
# print(planetas[8])

#TRABAJAR CON UNAS LISTAS DE NUMEROS
gravedadEnPlanetas=[0.378,0.907,1,0.377,2.36,0.916,0.889,1.12]
pesoBus=124054 #Newtons, en la Tierra

print(f"En la tierra un autobús de dos pisos pera {pesoBus} N")
print(f"En mercurio, un autobús de dos pisos pesa {pesoBus*gravedadEnPlanetas[0]} N")

print (f"Lo mas Liviano que seria un autobús en el sistema solar es {pesoBus*min(gravedadEnPlanetas)} N")
print (f"Lo mas Pesdo que seria un autobús en el sistema solar es {pesoBus*max(gravedadEnPlanetas)} N")