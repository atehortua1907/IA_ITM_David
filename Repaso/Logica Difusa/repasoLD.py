import numpy as np
import matplotlib.pyplot as plt

"""
Implements a Boolean set.
Arguments:
x_domain -- domain of variable x (array)
x_set -- tuple of values that represents the set within domain of x

Returns:
parameters -- boolean (True, False) list of values inside x_set
"""
def boolean_set(x_domain, x_set):
    val = np.logical_and(x_domain >= x_set[0], x_domain <= x_set[1])
    return val

#Grafiquemos algunos conjuntos Booleanos para una variable  𝑥  en el rango 0, 10

limit1 = 0
limit2 = 100

##Genera una lista de reales entre el limit1 y el limit2, con 500 resultados
domain = np.linspace(limit1, limit2, 500)

##Tupla de limite para esta gategoria de menor
menor = (0.1,12) 

##lista booleana de 500 bit donde los bit true 
#corresponden a los rangos en domain que se encuentren en la tupla menor
bool_set_1 = boolean_set(domain,menor) 

adolescente = (13,17)
bool_set_2 = boolean_set(domain,adolescente)

adulto = (18,90)
bool_set_3 = boolean_set(domain,adulto)

plt.fill(domain, bool_set_1)
plt.fill(domain, bool_set_2)
plt.fill(domain, bool_set_3)

plt.title("Three Boolean sets for variable x")
plt.show()
