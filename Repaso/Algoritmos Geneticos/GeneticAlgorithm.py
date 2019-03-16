##Problema de la Bolsa (representación binaria)

import numpy as np

def funcion_aptitud(x):
    peso = np.array([28, 11, 15, 19, 5, 3, 8]) 
    valor = np.array([40, 22, 30, 37, 8, 5, 12])
        
    CapacidadMax = 44    

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

#Creamos una matriz de ceros
p = np.zeros([nc, ng])

#Para cada gen de la poblacion de cromosomas, le asignamos un valor aleatorio entre 0 y 1
for chromosome in range(nc):
    for gene in range(ng):
        p[chromosome,gene] = np.random.choice([0, 1])

fa = np.zeros([nc], dtype=np.int)
for i in range(nc):
    fa[i] = funcion_aptitud(p[i,:])

print("Población =>",p)
print ("Función de Aptitud =>",fa)