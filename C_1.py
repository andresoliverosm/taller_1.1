import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de la ecuación de resistencia vs temperatura para un sensor PT100
a = 3.9083e-3
b = -5.775e-7

# Función para calcular la resistencia del sensor PT100 dado una temperatura
def pt100_resistencia(temperatura):
    return 100 * (1 + a*temperatura + b*temperatura**2)

temperatura2 = np.linspace(-200, 200, num=1000)

# Calcula la resistencia para cada temperatura en el intervalo
resistencia = pt100_resistencia(temperatura2)

# Grafica la resistencia vs temperatura
plt.plot(temperatura2, resistencia)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ω)')
plt.title('Comportamiento PT100')
plt.grid()
plt.show()