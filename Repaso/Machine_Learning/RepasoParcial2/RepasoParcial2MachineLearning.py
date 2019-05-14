import numpy as np

#Punto 9 del taller. Realice un proceso de propagación hacia adelante para la red definida por los pesos
#anteriores, para ello:

def linear_activation(W, b, a):
    z = np.dot(W,a) + b
    
    return z

def sigmoid(z):
    '''
    Returns sigmoid activation for array z
    '''
    a = 1. / (1. + np.exp(-z)) 
    
    return a 


W1 = np.random.rand(2,3)
b1 = np.zeros([2,1])

W2 = np.random.rand(3,2)
b2 = np.zeros([3,1])

W3 = np.random.rand(2,3)
b3 = np.zeros([2,1])

W4 = np.random.rand(3,2)
b4 = np.zeros([3,1])

W5 = np.random.rand(1,3)
b5 = np.zeros([1,1])

print("Punto 9a. Inicialice en valores aleatorios los pesos y en ceros los bias. (escriba los valores de W y b).")
print("W1 ", W1)
print("b1 ", b1)
print("W2 ", W2)
print("b2 ", b2)
print("W3 ", W3)
print("b3 ", b3)
print("W4 ", W4)
print("b4 ", b4)
print("W5 ", W5)
print("b5 ", b5)


X = np.array([[round(np.random.uniform(1,7),2)],[round(np.random.uniform(1,7),2)],[round(np.random.uniform(1,7),2)]])
print("Punto 9b. Cree un ejemplo para la entrada con valores aleatorios. (escriba los valores del ejemplo de entrada). ",X)

#Punto 9c. Codifique el proceso de propagación hacia delante para la red neuronal: 

Z1 = linear_activation(W1, b1, X)
A1 = sigmoid(Z1)

Z2 = linear_activation(W2, b2, A1)
A2 = sigmoid(Z2)

Z3 = linear_activation(W3, b3, A2)
A3 = sigmoid(Z3)

Z4 = linear_activation(W4, b4, A3)
A4 = sigmoid(Z4)

Z5 = linear_activation(W5, b5, A4)
A5 = sigmoid(Z5)

print("Punto 9d. Calcule el valor de la salida y escríbalo. ",X, A5)