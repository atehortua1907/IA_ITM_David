import numpy as np

#----Crear matriz binaria aleatoria en dos ciclos filas y columnas-------
rows = 7
columns = 10

p = np.round(np.random.random([rows, columns]))


for fila in range(rows):
    for column in range(columns):
        p[fila,column] = np.random.choice([0, 1])

for i in range(7):
    p[i] = np.random.choice([0, 1])

print(p)

#------------------------------------------------------------------------

#genera una matiz binaria random.random genera un aleatorio entre 0 y 1, round redonde a 0 o 1
matrizBin = np.round(np.random.random([rows, columns]))
print(matrizBin)
