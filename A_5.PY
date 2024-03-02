import numpy as np

def rotacion_x(angulo):
    radianes = np.radians(angulo)
    matriz = np.array([[1, 0, 0],
                       [0, np.cos(radianes), -np.sin(radianes)],
                       [0, np.sin(radianes), np.cos(radianes)]])
    return matriz

def rotacion_y(angulo):
    radianes = np.radians(angulo)
    matriz = np.array([[np.cos(radianes), 0, np.sin(radianes)],
                       [0, 1, 0],
                       [-np.sin(radianes), 0, np.cos(radianes)]])
    return matriz

def rotacion_z(angulo):
    radianes = np.radians(angulo)
    matriz = np.array([[np.cos(radianes), -np.sin(radianes), 0],
                       [np.sin(radianes), np.cos(radianes), 0],
                       [0, 0, 1]])
    return matriz

angulo = 25
rotacion_x = rotacion_x(angulo)
rotacion_y = rotacion_y(angulo)
rotacion_z = rotacion_z(angulo)

print("Rotacion en X:")
print(rotacion_x)
print("\nRotacion en Y:")
print(rotacion_y)
print("\nRotacion en Z:")
print(rotacion_z)