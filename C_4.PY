import numpy as np
import matplotlib.pyplot as plt

x = float(input("Ingrese la coordenada de X en (cm): "))
y = float(input("Ingrese la coordenada de Y en (cm): "))
z = float(input("Ingrese la coordenada de Z en (cm): "))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, x, y, z, color='GREEN')

ax.set_xlim([0, max(x, 1)])
ax.set_ylim([0, max(y, 1)])
ax.set_zlim([0, max(z, 1)])

ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Z (cm)')

plt.show()