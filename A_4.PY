def calcular_resistencia_PT100(temperatura):
    R0 = 100
    A = 3.9083e-3
    B = -5.775e-7
    
    Rt = R0 * (1 + A * temperatura + B * temperatura**2)
    
    return Rt

temperatura = float(input("Ingrese la temperatura en °C: "))
resistencia = calcular_resistencia_PT100(temperatura)

print(f"La resistencia es de {resistencia} ohmios.")