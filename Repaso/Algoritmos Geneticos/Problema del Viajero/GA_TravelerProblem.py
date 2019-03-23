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


def aptitud_function(index):
      
    #close loop between cities
    index = np.append(index,index[0])
    
    dist_sum = 0 #sum of distances of path
    
    for i in range(len(CityCoordinates['x'])):
        #cities index
        tx1 = CityCoordinates['x'][index[i]]
        tx2 = CityCoordinates['x'][index[i+1]]
        ty1 = CityCoordinates['y'][index[i]]
        ty2 = CityCoordinates['y'][index[i+1]]
        
        #linear distance between 2 adyacent cities
        dist_sum += np.sqrt( (tx1-tx2)**2 + (ty1-ty2)**2 )
    
    return 1.0/dist_sum


fa = np.zeros([numberChromosomes], dtype=np.float)
population = np.zeros([numberChromosomes, numberGenes], dtype=np.int)
#population initialization and aptitude function calculated
for i in range(numberChromosomes):
    population[i, :] = np.random.permutation(numberGenes) 
    fa[i] = aptitud_function(population[i])

h = 8





