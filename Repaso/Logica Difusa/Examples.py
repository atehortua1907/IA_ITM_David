import numpy as np
import matplotlib.pyplot as plt
import FuzzyFunctions as fuzzyFunctions #Archivo con funciones genericas

#Completar: aproximadamente 3 lineas de codigo
parameters_conjunto_baja = {"a":0, "b":0, "c":15, "d":20}
parameters_conjunto_media = {"a":15, "m":21.5, "b":27.5}
parameters_conjunto_alta = {"a":21.5, "b":27.5, "c":40, "d":40}

t = 16.7

#completar: aproximadamente 3 lineas de codigo
miu_baja = fuzzyFunctions.membership(t, "trapezoid", parameters_conjunto_baja)
miu_media = fuzzyFunctions.membership(t, "triangular", parameters_conjunto_media)
miu_alta = fuzzyFunctions.membership(t, "trapezoid", parameters_conjunto_alta)

#completar la lista de pertenencias
t_fuzzy = [miu_baja, miu_media, miu_alta]

print("temperatura fuzzy: ", t_fuzzy)

#Obtengamos y visualicemos todo el conjunto fuzzy utilizando la función anterior

resolucion = 100
T = np.linspace(0, 30, resolucion)

#utilicemos comprehension de python para generar todo el vector del conjunto fuzzy
conjunto_baja = np.array([fuzzyFunctions.membership(t, "trapezoid", parameters_conjunto_baja) for t in T])

plt.plot(T, conjunto_baja)
plt.show()

##------Grafiquemos todos los conjuntos fuzzy de la variable  𝑇 Utilicemos para ello la funcion generate_fuzzy_set------##
params_conjunto_baja = {"a":0, "b":0, "c":15, "d":20}
params_conjunto_media = {"a":15, "m":22.5, "b":27.5}
params_conjunto_alta = {"a":22.5, "b":30, "c":45, "d":45}

resolucion = 1000
T = np.linspace(0, 50, resolucion)

conjunto_baja = fuzzyFunctions.generate_fuzzy_set(T, "trapezoid", params_conjunto_baja)
conjunto_media = fuzzyFunctions.generate_fuzzy_set(T, "triangular", params_conjunto_media)
conjunto_alta = fuzzyFunctions.generate_fuzzy_set(T, "trapezoid", params_conjunto_alta)

plt.plot(T,conjunto_baja, 'r')
plt.plot(T,conjunto_media, 'g')
plt.plot(T,conjunto_alta, 'b')
plt.show()


#Utilicemos la función genérica para fusificar la variable t=16.7  ∈𝑇
params_conjunto_baja = {"a":0, "b":0, "c":15, "d":20}
params_conjunto_media = {"a":15, "m":22.5, "b":27.5}
params_conjunto_alta = {"a":22.5, "b":30, "c":45, "d":45}

funcion_baja = "trapezoid"
funcion_media = "triangular"
funcion_alta = "trapezoid"

key_baja = "baja"
key_media = "media"
key_alta = "alta"

t = 16.7
fuzzy_sets = {key_baja:(funcion_baja, params_conjunto_baja), key_media:(funcion_media, params_conjunto_media), key_alta:(funcion_alta, params_conjunto_alta)}

print(fuzzyFunctions.fuzzify(t, fuzzy_sets))