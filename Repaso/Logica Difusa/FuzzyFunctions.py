"""
Implements a membership function.

Arguments:
x -- crisp variable
membership_function -- string with the name of membership function: "trapezoid", "triangular"
parameters -- dictionary of parameters for membership function

Returns:
m_x -- float membership of x with respect to memebership_function
"""
import numpy as np

def membership(x, membership_function, parameters):
    m_x = 0
    
    if(membership_function == "trapezoid"):
        a = float(parameters["a"])
        b = float(parameters["b"])
        c = float(parameters["c"])
        d = float(parameters["d"])
        
        if(x <= a or x >= d):
            m_x = 0
        elif(x >= a and x <= b):
            m_x = (x-a)/(b-a)
        elif(x > b and x < c):
            m_x = 1
        elif(x >= c and x < d):
            m_x = (d-x)/(d-c)
            
    
    elif(membership_function == "triangular"):
        a = float(parameters["a"])
        m = float(parameters["m"])
        b = float(parameters["b"])
        
        if(x <= a):
            m_x = 0
        elif(x > a and x <= m):
            m_x = (x-a)/(m-a)
        elif(x > m and x < b):
            m_x = (b-x)/(b-m)
        else:
            m_x = 0
    
    return m_x


"""
    Permite generar el conjunto fuzzy de una variable X,
    dada la variable  𝑋 , el tipo de conjunto fuzzy y sus parametros
"""
def generate_fuzzy_set(X, membership_function, parameters):
    fuzzy_set = np.array([membership(x, membership_function, parameters) for x in X])
    return fuzzy_set

"""
Implements a fuzzify function.

Arguments:
x -- crisp variable
fuzzy_sets -- dictionary with next form: {"set_name":(membership_function, parameters)}
    membership_function: string with the name of membership_function: "trapezoid", "triangular"
    parameters -- dictionary of parameters for membership function

Returns:
f_x -- dictionary of membership values of x with respect to each set in fuzzy_sets (keys)
"""
def fuzzify(x, fuzzy_sets):
    ##CODE HERE
    #f_x = []
    f_x = {} #lista de valores de pertenencia por cada conjunto difuso
    
    keys = fuzzy_sets.keys()
    
    for k in keys:
        #CODE HERE: utilizar la funcion membership(x, membership_function, parameters)
        #m = membership(x, fuzzy_sets[k]..., fuzzy_sets[k]...)
        m = membership(x, fuzzy_sets[k][0], fuzzy_sets[k][1])
        #f_x.append(k)
        f_x[k]=m
    
    return f_x