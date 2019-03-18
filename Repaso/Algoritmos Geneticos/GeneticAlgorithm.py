##Problema de la Bolsa (representación binaria)

import numpy as np

def funcion_aptitud(chromosome):
    peso = np.array([28, 11, 15, 19, 5, 3, 8]) 
    valor = np.array([40, 22, 30, 37, 8, 5, 12])

    CapacidadMax = 44    

    if (np.sum(peso*chromosome) > CapacidadMax):
        aptitud = 0
    else:
        aptitud = np.sum(valor*chromosome)
    
    return aptitud

'''
Program: Genetic Algorithm for bag problem.
Author: Pedro Atencio
Copyright 2017
'''

#GA parameters
numberIterations = 100 #number of iterations
numberChromosomes = 10 #number of individuals
numberGenes = 7 #number of genes == items in problem

pc = 0.9
pm = 0.5

#Creamos una matriz de ceros
population = np.zeros([numberChromosomes, numberGenes])

#Para cada gen de la poblacion de cromosomas, le asignamos un valor aleatorio binario
for chromosome in range(numberChromosomes):
    for gene in range(numberGenes):
        population[chromosome,gene] = np.random.choice([0, 1])

fa = np.zeros([numberChromosomes], dtype=np.int)
for i in range(numberChromosomes):
    fa[i] = funcion_aptitud(population[i,:])

print("Población =>",population)
print ("Función de Aptitud =>",fa)

#Ciclo principal del algoritmo genético:
#Seleccion->Cruce->Mutación->Evaluación->Inserción
for i in range(numberIterations):
    #selection - simple random selection
    p1 = np.random.randint(numberChromosomes-1)
    p2 = np.random.randint(numberChromosomes-1)
    
    #crossing - One Point
    if(np.random.rand() <= pc):
        cross_point = np.random.randint(numberGenes)
        child1 = np.append(population[p1, 0:cross_point], population[p2, cross_point:])
        child2 = np.append(population[p2, 0:cross_point], population[p1, cross_point:])
        
    #mutation - Bit Inversion
    if(np.random.rand() <= pm):
        mut_point_c1 = np.random.randint(numberGenes-1)
        mut_point_c2 = np.random.randint(numberGenes-1)
        
        child1[mut_point_c1] = 1-child1[mut_point_c1]
        child2[mut_point_c2] = 1-child2[mut_point_c2]
    
    #evaluation
    eval_child1 = evalbin(child1)
    eval_child2 = evalbin(child2)
    
    #insertion - Max
    if(eval_child1 > fa[p1]):
        p[p1] = child1
        fa[p1] = eval_child1
    
    if(eval_child2 > fa[p2]):
        p[p2] = child2
        fa[p2] = eval_child2