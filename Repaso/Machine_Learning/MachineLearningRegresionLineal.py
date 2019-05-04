'''
Se abordan los temas:

Regresión lineal.
Descenso del gradiente.
'''
#Un modelo lineal se define como:  𝑌=𝑊𝑋+𝑏

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2) #aseguramos que el resultado del random es el mismo en cada ejecucion
m = 100
X = 2 * np.random.rand(m,1)
W = np.random.randint(3,8)+np.random.rand()
b = np.random.randint(3,8)+np.random.rand()
Y = W * X + b #regreson lineal
Y += np.random.randn(m,1) #ruido

plt.scatter(X, Y, color='red')
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.show()

'''
La regresión lineal consiste en hallar los valores de  𝑊  y  𝑏  tales que definan una recta
que se acerque lo mejor posible a los valores originales de  𝑌 dados los  𝑋  de entrada.
En este punto, podemos adivinar dichos valores?
'''

# W = None
# b = None
Y_pred = W * X + b
plt.scatter(X, Y, color='red')
plt.plot(X, Y_pred)
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.show()
