Inteligencia Artificial
Trabajo #1
Sobre estrategias de búsqueda
Fecha de asignación: 25/02/2018
Fecha de entrega: 04/03/2018
Porcentaje evaluativo: 10%
Número máximo de integrantes: 3
Formato y medio de entrega: Código fuente + informe escrito que contenga la descripción del trabajo
y los experimentos realizados. El trabajo debe ser enviado en formato comprimido al correo:
pedroatencio@itm.edu.co
Descripción:
Implementar búsqueda de costo uniforme (UCS), primero el mejor (BFS) y A* para resolver un
problema sobre el mapa de bucharest utilizado en clase y compartido a continuación:

Para ello, deberán:
1. Almacenar el mapa: posicisiones (x,y) y costos de ruta entre ciudades en una o varias
estructuras computacionales de datos. Nota: el costo entre ciudades se toma directamente de la
Figura. 1.
2. Implementar la función heurística: la cuál cambia los valores de la heurística de acuerdo al
objetivo (O) definido antes de realizar la búsqueda. Puede utilizar la distancia euclídea1
entre

dos puntos como función heurística.
3. Implementar la función de sucesión:
4. Implementar la estructura de los nodos: Contiene los campos: estado, padre, costo y
heurística.

1 https://en.wikipedia.org/wiki/Euclidean_distance
Figura. 1: Rumanian Map.

Inteligencia Artificial
Trabajo #1
Sobre estrategias de búsqueda
5. Implementar los métodos de búsqueda: UCS, Best-FS y A*. Para cada caso los métodos de
búsqueda deben poder ingresar como argumentos el estado inicial (I) y el estado objetivo (O).
6. Implementar el método para encontrar la solución: dado el nodo objetivo como argumento.
