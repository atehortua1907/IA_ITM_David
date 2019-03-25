import numpy as np

Characteristics = {
                    'Asesores': ['Paciente','Explicativo','Cordial','Tecnico','Agil'],
                    'Usuarios': ['Paciente','Explicativo','Cordial','Tecnico','Agil']
                  }

#GA parameters
numberIterations = 100 #number of iterations
numberChromosomes = 100 #number of individuals
numberGenes = len(Characteristics['Asesores']) #number of genes == cities

pc = 0.9 #Probabilidad de cruce
pm = 0.5 #Probabilidad de mutación

MinValue = 1
MaxValue = 45


def aptitude_function(chrommosome):
    return np.sum([chrommosome], dtype=np.float)
        

faAssessor = np.zeros([numberChromosomes], dtype=np.float)
faUser = np.zeros([numberChromosomes], dtype=np.float)
populationAssessor = np.zeros([numberChromosomes, numberGenes], dtype=np.float)
populationUser = np.zeros([numberChromosomes, numberGenes], dtype=np.float)

#population initialization and aptitude function calculated
for i in range(numberChromosomes):
    for j in range(numberGenes):
        populationAssessor[i, j] = np.random.uniform(MinValue,MaxValue)
        populationUser[i, j] = np.random.uniform(MinValue,MaxValue)
    faAssessor[i] =  aptitude_function(populationAssessor[i])
    faUser[i] =  aptitude_function(populationUser[i])

#Ciclo principal del algoritmo genético:
#Seleccion->Cruce->Mutación->Evaluación->Inserción
# for i in range(numberIterations):

print('Población Asesor /n', populationAssessor)
print('Población Usuario /n', populationUser)