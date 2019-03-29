import numpy as np
import matplotlib.pyplot as plt
import FuzzyFunctions as fuzzyFunctions #Archivo con funciones genericas


def main():
    #Ejemplo Propinas

    #1. Inicializar parametros

    ##-----Parametros para el servicio------##
    service_poor = "malo"
    service_good = "bueno"
    service_excellent = "excelente"
    funcion_service_poor = "trapezoid"
    funcion_service_good = "triangular"
    funcion_service_excellent = "trapezoid"
    params_poor = {"a":0, "b":0, "c":2, "d":5}
    params_good = {"a":2, "m":5, "b":8}
    params_excellent = {"a":5, "b":8, "c":10, "d":10}

    ##-----Parametros para la comida------##
    food_rancid = "desagradable"
    food_medium = "regular"
    food_delicious = "delicious"
    funcion_food_rancid = "trapezoid"
    funcion_food_medium = "trapezoid"
    funcion_food_delicious = "trapezoid"
    params_rancid = {"a":0, "b":0, "c":2, "d":3}
    params_medium = {"a":2, "b":3, "c":5, "d":6}
    params_delicious = {"a":5, "b":6, "c":10, "d":10}

    ##--------Parametros Propina---------#
    tip_cheap = "cheap"
    tip_average = "average"
    tip_generous = "generous"
    funcion_tip_cheap = "trapezoid"
    funcion_tip_average = "triangular"
    funcion_tip_generous = "trapezoid"
    params_cheap = {"a":0, "b":0, "c":1, "d":3}
    params_average = {"a":1, "m":3, "b":7}
    params_generous = {"a":3, "b":7, "c":10, "d":10}

    ##-----Dibujamos conjuntos Fuzzy-----##
    # Servicio = np.linspace(0,15, 1000)

    # f_set_infante = fuzzyFunctions.generate_fuzzy_set(Servicio, funcion_service_poor, params_poor)
    # f_set_adolescente = fuzzyFunctions.generate_fuzzy_set(Servicio, funcion_service_good, params_good)
    # f_set_adulto = fuzzyFunctions.generate_fuzzy_set(Servicio, funcion_service_excellent, params_excellent)

    # plt.plot(Servicio, f_set_infante, 'r')
    # plt.plot(Servicio, f_set_adolescente, 'g')
    # plt.plot(Servicio, f_set_adulto, 'b')
    # plt.show()

    #2 fusificar

    service = 3.1
    food = 5.8

    fuzzy_sets_servicio = {service_poor:(funcion_service_poor, params_poor), service_good:(funcion_service_good, params_good), service_excellent:(funcion_service_excellent, params_excellent)}
    service_fuzzy = fuzzyFunctions.fuzzify(service, fuzzy_sets_servicio)
        
    fuzzy_sets_food = {food_rancid:(funcion_food_rancid, params_rancid),food_medium:(funcion_food_medium, params_medium), food_delicious:(funcion_food_delicious, params_delicious)}
    food_fuzzy = fuzzyFunctions.fuzzify(food, fuzzy_sets_food)

    print(service_fuzzy)
    print(food_fuzzy)

    #3. Resolver reglas
    r1 = fuzzyFunctions.fuzzy_operator("OR", {"a":service_fuzzy[service_poor], "b":food_fuzzy[food_rancid]})
    r2 = service_fuzzy[service_good]
    r3 = fuzzyFunctions.fuzzy_operator("NOT", {"a":food_fuzzy[food_rancid]})
    r4 = fuzzyFunctions.fuzzy_operator("OR", {"a":service_fuzzy[service_excellent], "b":food_fuzzy[food_delicious]})

    print(r1,r2,r3,r4)

    #Agrupar reglas consecuentes
    rules = [r1,r2,r3,r4]
    print(fuzzyFunctions.fuzzy_group(rules))

    #4. Implicacion 
    T = np.linspace(0,12, 1000)
    fuzzy_set_cheap = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_cheap, params_cheap)
    fuzzy_set_average = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_average, params_average)
    fuzzy_set_generous = fuzzyFunctions.generate_fuzzy_set(T, funcion_tip_generous, params_generous)

    plt.plot(T, fuzzy_set_cheap, 'r')
    plt.plot(T, fuzzy_set_average, 'g')
    plt.plot(T, fuzzy_set_generous, 'b')
    plt.show()

    fs_cheap_truncated = fuzzyFunctions.fuzzy_implication(r1, fuzzy_set_cheap)
    fs_average_truncated= fuzzyFunctions.fuzzy_implication(r2, fuzzy_set_average)
    fs_generous_truncated = fuzzyFunctions.fuzzy_implication(r4, fuzzy_set_generous)

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