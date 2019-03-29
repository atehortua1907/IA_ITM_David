import numpy as np
import matplotlib.pyplot as plt
import FuzzyFunctions as fuzzyFunctions #Archivo con funciones genericas


def main():
    #Ejemplo Propinas

    #1. Inicializar parametros

    service_poor = "poor"
    service_good = "good"
    service_excellent = "excellent"
    funcion_service_poor = "trapezoid"
    funcion_service_good = "triangular"
    funcion_service_excellent = "trapezoid"
    params_poor = {"a":0, "b":0, "c":2, "d":5}
    params_good = {"a":2, "m":5, "b":8}
    params_excellent = {"a":5, "b":7, "c":10, "d":10}


    food_rancid = "rancid"
    food_delicious = "delicious"
    funcion_food_rancid = "trapezoid"
    funcion_food_delicious = "trapezoid"
    params_rancid = {"a":0, "b":4, "c":7, "d":4}
    params_delicious = {"a":6, "b":8, "c":10, "d":10}

    tip_cheap = "cheap"
    tip_average = "average"
    tip_generous = "generous"
    funcion_tip_cheap = "triangular"
    funcion_tip_average = "triangular"
    funcion_tip_generous = "trapezoid"
    params_cheap = {"a":0, "m":6, "b":12.5}
    params_average = {"a":6, "m":12.5, "b":20}
    params_generous = {"a":12.5, "b":20, "c":25, "d":30}

    #2 fusificar

    service = 9
    food = 9

    fuzzy_sets_servicio = {service_poor:(funcion_service_poor, params_poor), service_good:(funcion_service_good, params_good), service_excellent:(funcion_service_excellent, params_excellent)}
    service_fuzzy = fuzzyFunctions.fuzzify(service, fuzzy_sets_servicio)
        
    fuzzy_sets_food = {food_rancid:(funcion_food_rancid, params_rancid), food_delicious:(funcion_food_delicious, params_delicious)}
    food_fuzzy = fuzzyFunctions.fuzzify(food, fuzzy_sets_food)

    print(service_fuzzy)
    print(food_fuzzy)

    #3. Resolver reglas
    r1 = fuzzyFunctions.fuzzy_operator("OR", {"a":service_fuzzy["poor"], "b":food_fuzzy["rancid"]})
    r2 = service_fuzzy["good"]
    r3 = fuzzyFunctions.fuzzy_operator("OR", {"a":service_fuzzy["excellent"], "b":food_fuzzy["delicious"]})

    print(r1,r2,r3)

    #4. Implicacion 
    T = np.linspace(0,25, 1000)
    fuzzy_set_cheap = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_cheap, params_cheap)
    fuzzy_set_average = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_average, params_average)
    fuzzy_set_generous = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_generous, params_generous)

    plt.plot(T, fuzzy_set_cheap, 'r')
    plt.plot(T, fuzzy_set_average, 'g')
    plt.plot(T, fuzzy_set_generous, 'b')
    plt.show()

    fs_cheap_truncated = fuzzyFunctions.fuzzy_implication(r1, fuzzy_set_cheap)
    fs_average_truncated= fuzzyFunctions.fuzzy_implication(r2, fuzzy_set_average)
    fs_generous_truncated = fuzzyFunctions.fuzzy_implication(r3, fuzzy_set_generous)

    plt.plot(T, fs_cheap_truncated, 'r')
    plt.plot(T, fs_average_truncated, 'g')
    plt.plot(T, fs_generous_truncated, 'b')
    plt.show()

    #5. Agregacion
    aggregated_tip = fuzzyFunctions.fuzzy_aggregation([fs_cheap_truncated, fs_average_truncated, fs_generous_truncated])
    plt.fill(T, aggregated_tip)
    plt.show()

    #6. desfusificar
    salida = fuzzyFunctions.fuzzy_defuzzy(T, aggregated_tip, "centroid")
    print("al señor se le recomienda pagar: ", salida)
    
if __name__ == '__main__':
   main()

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

##Ejemplo con edades y clasificaciones
EDAD = np.linspace(0,50, 1000)
edad = 32
                   
params_conjunto_infante = {"a":0, "b":0, "c":12, "d":16}
params_conjunto_adolescente = {"a":12, "m":16, "b":21}
params_conjunto_adulto = {"a":16, "b":21, "c":50, "d":50}

funcion_infante = "trapezoid"
funcion_adolescente = "triangular"
funcion_adulto = "trapezoid"

f_set_infante = fuzzyFunctions.generate_fuzzy_set(EDAD, funcion_infante, params_conjunto_infante)
f_set_adolescente = fuzzyFunctions.generate_fuzzy_set(EDAD, funcion_adolescente, params_conjunto_adolescente)
f_set_adulto = fuzzyFunctions.generate_fuzzy_set(EDAD, funcion_adulto, params_conjunto_adulto)

plt.plot(EDAD, f_set_infante, 'r')
plt.plot(EDAD, f_set_adolescente, 'g')
plt.plot(EDAD, f_set_adulto, 'b')
plt.show()

conjunto_infante = "infante"
conjunto_adolescente = "adolescente"
conjunto_adulto = "adulto"

diccionario_parametros = {conjunto_infante:(funcion_infante, params_conjunto_infante), conjunto_adolescente:(funcion_adolescente, params_conjunto_adolescente), conjunto_adulto:(funcion_adulto, params_conjunto_adulto)}


edad_fuzzy = fuzzyFunctions.fuzzify(edad, diccionario_parametros)

print("la variable concreta: ", edad, " fue fusificada como: ", edad_fuzzy)

parameters = {"a": 0.6}
print(fuzzyFunctions.fuzzy_operator("NOT", parameters))
