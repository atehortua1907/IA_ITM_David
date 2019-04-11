# import keras
# from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

##Se comentan las lineas porque keras no importo en visual code

# X = np.array([-1,0,1,2,3,4], dtype=float)
# Y = np.array([-3,-1,1,3,5,7], dtype=float)
# #1.1.1 Creamos un modelo de red neuronal simple (1 neurona)
# model = keras.Sequential()
# model.add(Dense(units=1, input_shape=[1]))

# #1.1.2. Compilamos el modelo
# #Definimos el optimizador y el error a minimizar.
# model.compile(optimizer='sgd', loss='mean_squared_error')

# #1.1.3. Entrenamiento
# #Hacemos que el modelo aprenda.

# history = model.fit(X, Y, epochs=500, verbose=False)
# plt.plot(history.history['loss'])
# plt.show()

# #1.1.4. Utilizamos el modelo entrenado para predecir
# model.predict([5])

# #1.1.4. Qué aprendió el modelo???
# model.get_weights()

#2. Tipos de problemas y datasets
'''
Usualmente los problemas de predicción se dividen en dos categorías:

Clasificación: En cuyo caso la salida del modelo es DISCRETA, es decir una etiquta o categoria que se asigna al objeto en cuestión.
𝐺(𝑥)=𝑘;𝑘={𝑙𝑎𝑏𝑒𝑙1,𝑙𝑎𝑏𝑒𝑙2,𝑙𝑎𝑏𝑒𝑙3,...,𝑙𝑎𝑏𝑒𝑙𝑛} 
Regresión: En cuyo caso la salida del modelo es CONTINUA, es decir, un valor real que estima a partir de la entrada.
𝐺(𝑥)=𝑘;𝑘∈𝑅𝑛

Analicemos el siguiente dataset de la librería <a href=https://scikit-learn.org/stable/index.html>sklearn:
'''

from sklearn.datasets import load_boston
from tabulate import tabulate

dataset = load_boston() #cargamos el dataset
entrada = dataset.data #aislamos los valores de entrada del problema
salida = dataset.target #aislamos los valores de salida del problema

#usualmente los datos se cargan de esta manera
X, Y = dataset.data, dataset.target

#concatenemos X y Y para poder tabularlos
m, n = np.shape(X)
data = np.zeros([m, n+1])
data[:, 0:n] = X
data[:, n] = Y

headers = [str(i) for i in dataset.feature_names]+['target']
tabla = tabulate(data, headers=headers, tablefmt="fancy_grid", floatfmt=".2f")
print(tabla)