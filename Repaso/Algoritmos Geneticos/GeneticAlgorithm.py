##Problema de la Bolsa (representación binaria)

import numpy as np

def funcion_aptitud(x):
    peso = np.array([28, 11, 15, 19, 5, 3, 8]) 
    valor = np.array([40, 22, 30, 37, 8, 5, 12])
    
    
    CapacidadMax = 44 
    
    #utilice np.sum para calcular la sumatoria de un vector
    #COMPLETAR
    if (np.sum(peso*x) > CapacidadMax):
        aptitud = 0
    else:
        aptitud = np.sum(valor*x)
    
    return aptitud

'''
Program: Genetic Algorithm for bag problem.
Author: Pedro Atencio
Copyright 2017
'''

#GA parameters
ni = 100 #number of iterations
nc = 10 #number of individuals
ng = 7 #number of genes == items in problem

pc = 0.9
pm = 0.5

p = np.zeros([nc, ng])

fa = np.zeros([nc], dtype=np.int)
for i in range(nc):
    fa[i] = funcion_aptitud(p[i,:])

print (fa)