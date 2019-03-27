import numpy as np

Characteristics = {
                    'Asesores': ['Paciente','Explicativo','Cordial','Tecnico','Agil'],
                    'Usuarios': ['Paciente','Explicativo','Cordial','Tecnico','Agil']
                  }

#GA parameters
numberIterations = 100 #number of iterations
numberChromosomes = 10 #number of individuals
numberGenes = len(Characteristics['Asesores']) #number of genes == cities

crossingProbability = 0.9 #Probabilidad de cruce
mutationProbability = 0.5 #Probabilidad de mutación

MinValue = 1
MaxValue = 45

child = None


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

print('\n-------------Población Inicial Asesor------------- \n', populationAssessor)

#Ciclo principal del algoritmo genético:
#Seleccion->Cruce->Mutación->Evaluación->Inserción
def ruletaSelection(fa):

    totalFa = np.sum([fa], dtype=np.float)
    percentFa = np.zeros([numberChromosomes], dtype=np.float)
    selectedCrhomosomes = np.zeros([2], dtype=np.int)

    for i in range(numberChromosomes):
        percentFa[i] = fa[i]/totalFa

    selectedCrhomosomes[0] = np.argmax(np.cumsum(percentFa) >= np.random.rand())
    selectedCrhomosomes[1] = np.argmax(np.cumsum(percentFa) >= np.random.rand())
    
    return selectedCrhomosomes


for i in range(numberIterations):

    selectedCrhomosomes = ruletaSelection(faAssessor)
    chromoSelectP1 = selectedCrhomosomes[0]
    chromoSelectP2 = selectedCrhomosomes[1]

    #Cruce Aritmetico Completo
    if(np.random.rand() <= crossingProbability):
        a = 0.5
        fatherA = populationAssessor[chromoSelectP1]
        fatherB = populationAssessor[chromoSelectP2]
        child = np.zeros([0], dtype=np.float)
        for m in range(numberGenes):
            child = np.append(child,a*fatherA[m]+(1-a)*fatherB[m])
    
    if(child is None):
        continue

    #Mutación, suma número aleatorio a un par de genes seleccionados aleatoriamente (cod. real)
    if(np.random.rand() <= mutationProbability):
        randomPosition = np.random.randint(numberGenes)
        child[randomPosition] =  child[randomPosition] + np.random.uniform(MinValue,MaxValue)/100
        randomPosition = np.random.randint(numberGenes)
        child[randomPosition] = child[randomPosition] + np.random.uniform(MinValue,MaxValue)/100
    
    #Evaluamos el hijo
    evaluationChild = aptitude_function(child)

    #Inserción
    randomPositionFa = np.random.choice([chromoSelectP1, chromoSelectP2])
    if(evaluationChild > faAssessor[randomPositionFa]):
        populationAssessor[randomPositionFa] = child
        faAssessor[randomPositionFa] = evaluationChild    

populationAssessorOrder = np.zeros([numberChromosomes, numberGenes], dtype=np.float)
count = 0

for i in np.argsort(faAssessor)[::-1]:
    populationAssessorOrder[count] = populationAssessor[i]
    count = count + 1

populationUserOrder = np.zeros([numberChromosomes, numberGenes], dtype=np.float)
count = 0

for i in np.argsort(faUser):
    populationUserOrder[count] = populationUser[i]
    count = count + 1

print('\n------------Población final Asesor-------------\n', populationAssessor)
print('\n------------Población Usuario----------------\n', populationUser)

#Asignación de asesores a usuarios:
#Los asesores con mayor calificación son asignados a los usuarios con las caracteristicas mas bajas.
#En este orden de ideas, el asesor mas calificado atenderá al usuario con las preferencias de menor calificación.
for i in range(numberChromosomes):
    print('\nEl usuario con preferencias ',aptitude_function(populationUserOrder[i]),
        'Sera atendido por el asesor con caracteristicas ',aptitude_function(populationAssessorOrder[i]))
