import math
import matplotlib.pyplot as plt
import numpy as np

vol = float(input ("\n Ingrese el valor de voltaje (V) de entrada: "))
cap = float(input(" \n Ingrese el valor del capacitor: (F)"))
res = float(input("\n Ingrese el valor de la resistencia: (Ohm) "))

#carga
def carga(vol, cap, res, t):
    return vol * (1 - np.exp(-t / (res * cap)))

#descarga    
def descarga(vol, cap, res, t):
    return vol * np.exp(-t / (res * cap))

# Definición del tiempo de la simulación
t = np.linspace(0, 5*res*cap, 1000)


circuito_carga = carga(vol, cap, res, t)
circuito_descarga = descarga(vol, cap, res, t)


plt.title('Carga y descarga de un circuito RC')
plt.plot(t, circuito_carga, label='Carga del circuito')
plt.plot(t, circuito_descarga, label='Descarga del circuito')
plt.legend()
plt.xlabel('Tiempo(S)')
plt.ylabel('Carga y Descarga (V)')
plt.grid(True)
plt.show()