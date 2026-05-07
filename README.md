# KAUFMANN-MALGRANGER
## Descripción
Dado un grafo G = (V, A) de orden n, en caso de que el grafo sea semihamiltoniano, el algoritmo enumera sin redundancia todos los caminos elementales de longitudes hasta n-1 que parten de cada vértice.
## ¿Qué hace el algoritmo?
El algoritmo de Kaufmann-Malgranger sigue el siguiente flujo:
1. A partir de la matriz de adyacencia del grafo, se crea la matriz H^1, donde cada elemento distinto de 0 se reemplazará por ij, siendo i y j los vértices adyacentes. (Ejemplo: si los vértices A y B están conectados, donde hay un valor distinto de cero en su matriz de adyacencia, ese valor será reemplazado por AB en la columna de B, y BA en la fila de A)
2. Con base en la matriz anterior, se inicia un índice r en 1. Ese será el índice inicial de la matriz.
3. Se realiza **multiplicación latina** de las matrices: esto es [H]^(r+1) = [H]^r ⋅ [H]^1
4. El paso 3 se repite hasta que r = n - 1. En ese caso, cuando la matriz sea [H]^(n-1), la fila i contendrá todos los caminos hamiltonianos que parten del nodo i.
## Implementación
Algunos aspectos a considerar son los siguientes:
1. Lectura de la matriz de adyacencia
2. Conversión de elementos de la matriz a la forma ij
3. **Multiplicación latina**
4. Guardado de las matrices [H]^(r+1)
5. Validación de los caminos hamiltonianos generados en la matriz [H]^(n-1)
