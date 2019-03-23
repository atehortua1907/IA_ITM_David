##Problema de la Bolsa (representación binaria)

import numpy as np

# En este problema se requiere maximizar el beneficio sin sobrepasar la capacidad.
# Se emplea el algoritmo genético con codificación binaria (genbin), debido que la
# codificación binaria me permite con 1 lógico incluir el elemento, y con un 0 excluirlo.
# Finalmente se encuentra que elementos se deben agregar de tal forma que se maximice el beneficio.

#GA parameters
numberIterations = 100 #number of iterations
numberChromosomes = 10 #number of individuals
numberGenes = 7 #number of genes == items in problem

pc = 0.9 #Probabilidad de cruce
pm = 0.5 #Probabilidad de mutación

#Variables para los hijos seleccionados
child1 = None
child2 = None


#1. Genero un población, matriz de codificación binaria [n*7] 
population = np.round(np.random.random([numberChromosomes, numberGenes]))

#2. Diseñamos la función de aptitud
def funcion_aptitud(chromosome):
    peso = np.array([28, 11, 15, 19, 5, 3, 8]) 
    valor = np.array([40, 22, 30, 37, 8, 5, 12])

    CapacidadMax = 44    

    if (np.sum(peso*chromosome) > CapacidadMax):
        aptitud = 0
    else:
        aptitud = np.sum(valor*chromosome)
    
    return aptitud

fa = np.zeros([numberChromosomes], dtype=np.int)
for i in range(numberChromosomes):
    fa[i] = funcion_aptitud(population[i,:])

print("Población inicial =>",population)
print ("Función de Aptitud para población inicial =>",fa)

#Ciclo principal del algoritmo genético:
#Seleccion->Cruce->Mutación->Evaluación->Inserción
for i in range(numberIterations):
    #3. Selection - simple random selection
    chromoSelectP1 = np.random.randint(numberChromosomes-1)
    chromoSelectP2 = np.random.randint(numberChromosomes-1)
  
    #4. Crossing - One Point
    if(np.random.rand() <= pc):
        cross_point = np.random.randint(numberGenes)
        child1 = np.append(population[chromoSelectP1, 0:cross_point], population[chromoSelectP2, cross_point:])
        child2 = np.append(population[chromoSelectP2, 0:cross_point], population[chromoSelectP1, cross_point:])

    if(child1 is None):
        continue

    #5. Mutation - Bit Inversion
    if(np.random.rand() <= pm):
        mut_point_c1 = np.random.randint(numberGenes-1)
        mut_point_c2 = np.random.randint(numberGenes-1)
        
        child1[mut_point_c1] = 1-child1[mut_point_c1]
        child2[mut_point_c2] = 1-child2[mut_point_c2]
    
    #6. Evaluation
    eval_child1 = funcion_aptitud(child1)
    eval_child2 = funcion_aptitud(child2)
    
    #7. Insertion - Max
    if(eval_child1 > fa[chromoSelectP1]):
        population[chromoSelectP1] = child1
        fa[chromoSelectP1] = eval_child1
    
    if(eval_child2 > fa[chromoSelectP2]):
        population[chromoSelectP2] = child2
        fa[chromoSelectP2] = eval_child2

print('<-------------Resultados------------->')    
print("Población final =>",population)
print ("Función de Aptitud para población final =>",fa)
print('La mejor configuración para la bolsa es: ', population[np.argmax(fa)])
print('Con una función de aptitud de: ', fa[np.argmax(fa)])
print('<------------------------------------>') 