import numpy as np

#----Crear matriz binaria aleatoria en dos ciclos filas y columnas-------
rows = 7
columns = 10

p = np.zeros([rows, columns])

for fila in range(rows):
    for column in range(columns):
        p[fila,column] = np.random.choice([0, 1])

for i in range(7):
    p[i] = np.random.choice([0, 1])

print(p)

#------------------------------------------------------------------------

#TODO: Averiguar con el profesor como crear la matriz binaria con funciones python