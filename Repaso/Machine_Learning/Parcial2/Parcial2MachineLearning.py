import numpy as np

def linear_activation(W, b, X):
    z = np.dot(W.T,X) + b
    
    return z

def sigmoid(z):
    '''
    Returns sigmoid activation for array z
    '''
    a = 1. / (1. + np.exp(-z)) 
    
    return a 

def backward_propagation(A, X, Y):
    m = X.shape[1]
    
    dz = A - Y
    dW = np.dot(X, dz.T) / m
    db = np.sum(dz) / m
    
    return (dW, db)

def loss(y, a):
    return -(y * np.log(a) + (1-y) * np.log(1-a))

def cost(logloss):
    return np.mean(logloss)


# def linear_activation(W, b, a):
#     z = np.dot(W,a) + b
    
    # return z

# def sigmoid(z):
#     '''
#     Returns sigmoid activation for array z
#     '''
#     a = 1. / (1. + np.exp(-z)) 
    
#     return a 


W = np.array([[0.5],[-0.8]])
b = -1.23
X = np.array([[0.0],[1.0]])
Y = 1.0
learning_rate = 0.5

num_epochs = 10000

for i in range(num_epochs):
    ## Forward Propagation
    Z1 = linear_activation(W,b,X)
    A1 = sigmoid(Z1)
    
    # Z2 = linear_activation(W2,b2,X2)
    # A2 = sigmoid(Z2)
    
    # Z3 = linear_activation(W3,b3,X3)
    # A3 = sigmoid(Z3)
    
    #Backward Propagation
    (dW1, db1) = backward_propagation(A1,X, Y)
    # (dW2, db2) = backward_propagation(A2,X2, Y2)
    # (dW3, db3) = backward_propagation(A3,X3, Y3)
    
    #Weight Updates
    W -= learning_rate * dW1
    b -= learning_rate * db1
    # W2 -= learning_rate * dW2
    # b2 -= learning_rate * db2
    # W3 -= learning_rate * dW3
    # b3 -= learning_rate * db3
    
    #Cost estimation
    J1 = cost(loss(Y,A1))
    # J2 = cost(loss(Y2,A2))
    # J3 = cost(loss(Y3,A3))
    
    
    if(i%1000 == 0):
        print("costo regresor 1 -- iteracion ", i, ": ", J1)
        # print("costo regresor 2 -- iteracion ", i, ": ", J2)
        # print("costo regresor 3 -- iteracion ", i, ": ", J2)

print("W1 actualizado: ",W, "b1 actualizado: ", b)
# print("W2 actualizado: ",W2, "b2 actualizado: ", b2)
# print("W3 actualizado: ",W3, "b3 actualizado: ", b3)


W1 = np.random.rand(4,3)
b1 = np.zeros([4,1])

W2 = np.random.rand(2,4)
b2 = np.zeros([2,1])

W3 = np.random.rand(3,2)
b3 = np.zeros([3,1])

W4 = np.random.rand(5,3)
b4 = np.zeros([5,1])

W5 = np.random.rand(1,5)
b5 = np.zeros([1,1])

print("Punto 5.1. Inicialice los parámetros W y b de la red con valores aleatorios (escriba dichos valores).")
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

X =  np.array([[round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2)],[round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2)],[round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2),round(np.random.uniform(1,7),2)]])
print("Punto 5.2 entrada x de 3 ejemplos (samples) con valores arbitrarios",X)

#Punto 5.3. Codifique el proceso de propagación hacia adelante: 

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

print("Calcule el valor de salida (escriba este valor). ",X, A5)