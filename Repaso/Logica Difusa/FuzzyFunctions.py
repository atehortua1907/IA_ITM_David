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

"""
Implements Zadeh's Fuzzy Operators.

Arguments:
operator -- string with name of operator: "AND", "OR", "NOT"
parameters -- dictionary with parameters of operator

Returns:
k -- operators value
"""

def fuzzy_operator(operator, parameters):
    k = 0
    if(operator == "AND"):
        a = parameters["a"]
        b = parameters["b"]
        k = min(a, b)
    elif(operator == "OR"):
        a = parameters["a"]
        b = parameters["b"]
        k = max(a, b)
    elif(operator == "NOT"):
        a = parameters["a"]
        k = 1 - a
    else:
        print("Invalid operator.")
    
    return k

"""
Implements fuzzy implication (MIN).

Arguments:
r -- scalar from rules solving and grouping.
fuzzy_set -- A fuzzy set (array of values).

Returns:
s -- implication result. An array of numeric values.
"""
def fuzzy_implication(r, fuzzy_set):
    val = np.minimum(r, fuzzy_set)
    return val

"""
Implements Aggregation fuzzy operator using MAX.

Arguments:
fuzzy_sets -- A list with fuzzy_sets of output variable. All sets must have same dimension.

Returns:
val -- Aggregation result. An array of values.
"""
def fuzzy_aggregation(fuzzy_sets):
    val = np.zeros([fuzzy_sets[0].shape[0]])
    
    for s in fuzzy_sets:
        val = np.maximum(val, s)
        
    return val

"""
Implements defuzzification (centroid, bisector).

Arguments:
Y -- array with range of output variable Y
fuzzy_set_output -- A fuzzy_set of output variable.
method -- string with name of deffuzification method. can be "centroid", "bisector"

Returns:
val -- scalar value of crisp output variable.
"""
def fuzzy_defuzzy(Y, fuzzy_set_output, method="centroid"):
   
    if(method == "centroid"):
        val = np.sum(Y * fuzzy_set_output) /  np.sum(fuzzy_set_output)
    elif(method == "bisector"):
        val = None
    
    return val

"""
Implements common consecuent grouping.

Arguments:
rules -- list of values from resolved antecedents of rules with same consecuent

Returns:
val -- max from rules
"""

def fuzzy_group(rules):
    val = np.max(rules)
    return val