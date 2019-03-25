##Problema del viajero (representación entera)

import numpy as np
import matplotlib.pyplot as plt


'''
Determinar cual es la mejor ruta que minimice el recorrido por las ciudades ubicadas
en las coordenadas indicadas en la imagen ProblemaViajero.PNG 

Para resolver este problema se emplea el algoritmo genético con codificación entera en donde
no se repiten los números (no se repiten ciudades).
Para evaluar los cromosomas se requiere diseñar la funciona de evaluación.
'''
#GA parameters
numberIterations = 100 #number of iterations
numberChromosomes = 100 #number of individuals
numberGenes = 12 #number of genes == cities

pc = 0.9 #Probabilidad de cruce
pm = 0.5 #Probabilidad de mutación


CityCoordinates = {
                    'x': [1, 1, 1, 1, 2.5, 2.5, 3.5, 3.5, 7.0, 10.0, 7.0, 7.0],
                    'y': [1, 3, 7, 8, 7.5, 1.0, 2.0, 8.2, 15.5, 13.5, 12.1, 12]
                  }

plt.plot(CityCoordinates['x'], CityCoordinates['y'], 'b*')#cities
plt.title('Coordenadas de la Ciudad')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()


def aptitud_function(chromosomeRoute):
      
    #close loop between cities
    chromosomeRoute = np.append(chromosomeRoute,chromosomeRoute[0])
    
    dist_sum = 0 #sum of distances of path
    
    for i in range(len(CityCoordinates['x'])):
        #cities index
        tx1 = CityCoordinates['x'][chromosomeRoute[i]]
        tx2 = CityCoordinates['x'][chromosomeRoute[i+1]]
        ty1 = CityCoordinates['y'][chromosomeRoute[i]]
        ty2 = CityCoordinates['y'][chromosomeRoute[i+1]]
        
        #linear distance between 2 adyacent cities
        dist_sum += np.sqrt( (tx1-tx2)**2 + (ty1-ty2)**2 )
    
    return np.round(1.0/dist_sum, 5)


fa = np.zeros([numberChromosomes], dtype=np.float)
population = np.zeros([numberChromosomes, numberGenes], dtype=np.int)

#population initialization and aptitude function calculated
for i in range(numberChromosomes):
    population[i, :] = np.random.permutation(numberGenes) 
    fa[i] = aptitud_function(population[i])

#Ciclo principal del algoritmo genético:
#Seleccion->Cruce->Mutación->Evaluación->Inserción
for i in range(numberIterations):
    #selection - best selection (parent1)
    p1_index = np.argsort(fa)[::-1][0] #Retorna el indice de la mejor aptitud
    p2_index = np.random.randint(numberChromosomes)
    p1 = population[p1_index]
    p2 = population[p2_index]
    
    #cross: permutation one point
    if(np.random.rand() <= pc):
        cross_point = np.random.randint(numberGenes)
        child1 = p1[0:cross_point]
        child2 = p2[0:cross_point]
        
        init_k = cross_point
        for k in range(numberGenes):
            j = (init_k+k)%numberGenes #Crea el indice que permite obtener el valor a partir del punto de corte hasta volver al punto de corte
            
            #child1 == p2[j] retorna una matriz boleana donde un valor true es el elemento que sea igual al comparado
            #np.count_nonzero devuelve el numero de ceros encontrados
            #np.count_nonzero(child1 == p2[j]) aquí solo puede devolver número de ceros igual a 1 o a 0, esto se toma como falso o verdadero

            if not(np.count_nonzero(child1 == p2[j])):
                child1 = np.append(child1, p2[j])
            
            if not(np.count_nonzero(child2 == p1[j])):
                child2 = np.append(child2, p1[j])

    #mutation: order change
    if(np.random.rand() <= pm):
        mut_point_c1 = np.random.randint(numberGenes-1)
        mut_point_c2 = np.random.randint(numberGenes-1)
    
        temp = child1[mut_point_c1]
        child1[mut_point_c1] = child1[mut_point_c2]
        child1[mut_point_c2] = temp
        
        temp = child2[mut_point_c1]
        child2[mut_point_c1] = child2[mut_point_c2]
        child2[mut_point_c2] = temp
    
    #evaluation
    eval_child1 = aptitud_function(child1)
    eval_child2 = aptitud_function(child2)
    
    #insertion - max
    if(eval_child1 > fa[p1_index]):
        population[p1_index] = child1
        fa[p1_index] = eval_child1
    
    if(eval_child2 > fa[p2_index]):
        population[p2_index] = child2
        fa[p2_index] = eval_child2    





