import numpy as np

s = np.random.uniform(0,1)

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

#----------One-dimensional subarrays--------
#https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html

x = np.arange(10)
x[:5]  # first five elements
x[5:]  # elements after index 5
x[4:7]  # middle sub-array
x[::2]  # every other element
x[1::2]  # every other element, starting at index 1
x[::-1]  # all elements, reversed
x[5::-2]  # reversed every other from index 5

#-------argsort-------#
x = np.array([3, 1, 2])
np.argsort(x) # devuelve los indices ascedentemente basado en los valores del array
#array([1, 2, 0])

#-----shape------#
#Devuelve la forma de un vector, ejemplo x = np.random.rand(50, 2) * 15
#y = x.shape[0]
#print(y) imprime el número 50 correspondientes al número de filas del vector x