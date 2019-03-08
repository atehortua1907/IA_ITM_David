import numpy as np

def funcion_aptitud(x):
    peso = np.array([28, 11, 15, 19, 5, 3, 8]) 
    valor = np.array([40, 22, 30, 37, 8, 5, 12])
    
    
    k = 44 
    
    #utilice np.sum para calcular la sumatoria de un vector
    #COMPLETAR
    if (None):
        aptitud = None
    else:
        aptitud = None
    
    return aptitud

ni = 100 #numero de iteraciones
nc = 10 #tamaño de la poblacion
ng = 7 #numero de genes por cromosoma

pc = 0.9 #probabilidad de cruce
pm = 0.5 #probabilidad de mutacion

seed = 2
np.random.seed(seed)

#utilice np.random.random y np.round para generar la matriz de binarios p.
#COMPLETAR
p = None

#fa es un vector que almacenará las funciones de aptitud de cada individuo de la población.
fa = np.zeros([nc], dtype=np.int)

for i in range(None):
    fa[i] = funcion_aptitud(None)

print("Poblacion inicial: ", p)
print("Aptitudes: ", fa)