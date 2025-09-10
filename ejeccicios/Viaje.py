pais = input("Ingresa el país Ecuador, Colombia, Peru: ")
zona = input("Ingresa la zona urbana, rural, perimetral: ")
velocidad = int(input("Ingresa tu velocidad actual Km/h: "))


if pais == "Ecuador":
    if zona == "urbana":
        if velocidad <=9:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=51:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "rural":
        if velocidad <=50:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=71:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "perimetral":
        if velocidad <=70:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=91:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
elif pais == "Colombia":
    if zona == "urbana":
        if velocidad <=9:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=31:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "rural":
        if velocidad <=30:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=81:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "perimetral":
        if velocidad <=80:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=101:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
elif pais == "Peru":
    if zona == "urbana":
        if velocidad <=9:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=41:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "rural":
        if velocidad <=40:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=61:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")
    elif zona == "perimetral":
        if velocidad <=60:
            print(f"Tu velocidad es {velocidad} Km/h. Está por debajo del mínimo permitido (10 Km/h).")
        if velocidad >=121:
            print(f"Tu velocidad es {velocidad} Km/h. Está por encima del mínimo permitido (50 Km/h).")

