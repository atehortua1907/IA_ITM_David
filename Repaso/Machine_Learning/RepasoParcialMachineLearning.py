'''
From Miercoles 24 de abril de 2019 02:00 hh
Repaso parcial Machine Learning
1. Cargar Iris Dataset
2. Utilizar Knn, k = 3
3. Utilizar Knn, k = 5
4. Utilizar Naive Bayes
5. Utilizar Matriz de Confusión
6. Utilizar Accuracy
7. Utilizar K.Fold, k = 10

Tomar de ejemplo el archivo PerformanceTools

Nota: Visual Studio Code, correr en debuggin(F5) para ver los resultados completos en "Debug Console"
To Jueves 25 de abril de 2019
'''
#0. Cargar librerias
from sklearn.datasets import load_iris
from tabulate import tabulate
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#1. Cargar Iris Dataset
dataset = load_iris()
X, Y = dataset.data, dataset.target

#1.1 Tabular dataset para  una mejor visualización
#concatenemos X y Y para poder tabularlos
m, n = np.shape(X)
data = np.zeros([m, n+1])
data[:, 0:n] = X
data[:, n] = Y
headers = list(dataset.feature_names)+list(dataset.target_names)
tabla = tabulate(data, headers=headers, tablefmt="grid", floatfmt=".2f")
print(tabla)

#----------------------------------Entendiendo------------------------------------#
#Para este caso obtenemos una exactitud(accuracy) del 96% debido a:
#Estamos evaluando(preds) los mismos datos que entrenamos
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, Y)
preds = model.predict(X)
print('Accuracy evaluando los mismos datos entrenados: ',accuracy_score(preds, Y)) #96%


#Una posible solución es obtener del dataset un porcentaje para entrenar por ejemplo el 70%, el resto para evaluar
#Pero aún hay un problema, ya que estamos tomando partes fijas del dataset, es decir, entrenamos siempre desde un punto fijo
#hasta otro punto fijo, asi mismo con el test... omitiendo así tipos de clasificaciones que nunca fueron entrenadas.
n = np.shape(X)[0]
train_len = int(n*0.7)
X_train , Y_train = X[0:train_len], Y[0:train_len]
X_test, Y_test = X[train_len:], Y[train_len:]
model.fit(X_train, Y_train)
preds = model.predict(X_test)
print('Accuracy evaluando una parte fija del dataset, diferente a la otra parte fija que fue entrenada: ',accuracy_score(preds,Y_test))#62%

#Una posible solución es permutar los indices del dataset, obteniendo así features y targets de todos los tipos...
#tanto para el entrenamiento como para el test
indices = np.arange(0,149,1)
perm_index = np.random.permutation(indices)
X_train, Y_train = X[perm_index[0:train_len]], Y[perm_index[0:train_len]]
X_test, Y_test = X[perm_index[train_len:]], Y[perm_index[train_len:]]
model.fit(X_train, Y_train)
preds = model.predict(X_test)
print('Accuracy con indices permutados tanto en entrenamiento como en test: ', accuracy_score(preds, Y_test))
