import sys
import copy
import data

def mult_latina(matrizA, matrizB, orden):
    """
    Realiza la multiplicación latina entre dos matrices de caminos.
    
    En lugar de sumar productos escalares (como en la mult. convencional),
    concatena los caminos: si matrizA[i][k] contiene el camino P y
    matrizB[k][j] contiene el camino Q, el resultado es P concatenado con
    Q[1:] (se omite el primer vértice de Q para no repetir el nodo k).
    
    Solo se concatenan caminos cuya intersección de vértices visitados
    sea exactamente {k}, garantizando que no se repitan vértices
    (condición hamiltoniana).
    
    Retorna la nueva matriz de caminos resultante.
    """
    # Matriz resultado inicializada con listas vacías (celda sin caminos)
    tempMatrix = [[[] for _ in range(orden)] for _ in range(orden)]

    for i in range(orden):
        for j in range(orden):
            caminos_ij = []  # Caminos válidos encontrados para la celda (i, j)

            for k in range(orden):
                # Obtenemos todos los caminos en la celda (i,k) y (k,j)
                caminos_ik = matrizA[i][k]  # Lista de caminos (cada uno es lista de vértices)
                caminos_kj = matrizB[k][j]

                # Si alguna celda está vacía, no hay camino por este k
                if not caminos_ik or not caminos_kj:
                    continue

                for camino1 in caminos_ik:
                    for camino2 in caminos_kj:
                        vertices_1 = set(camino1)
                        vertices_2 = set(camino2)

                        # Condición latina: la intersección debe ser SOLO el nodo k
                        # Esto asegura que no se repitan vértices en el camino resultante
                        if vertices_1 & vertices_2 == {camino2[0]}:
                            # Concatenamos: camino1 + camino2 sin su primer elemento (k ya está en camino1)
                            nuevo_camino = camino1 + camino2[1:]
                            caminos_ij.append(nuevo_camino)

            tempMatrix[i][j] = caminos_ij

    return tempMatrix


def imprimir_matriz(matriz, orden, vertices):
    """
    Imprime la matriz de caminos de forma legible.
    Cada celda muestra los caminos separados por comas.
    """
    for i in range(orden):
        fila = []
        for j in range(orden):
            caminos = matriz[i][j]
            if not caminos:
                fila.append("  0  ")
            else:
                # Convierte cada camino (lista de índices) a string de nombres de vértices
                strs = [
                    "".join(str(vertices[v]) for v in camino)
                    for camino in caminos
                ]
                fila.append(", ".join(strs))
        print("  |  ".join(fila))
    print()


# ──────────────────────────────────────────────
# Lectura y validación de datos
# ──────────────────────────────────────────────

swAR = False
vertices  = data.n_vertex
matriz_ad = data.adcy_matrix
orden     = len(vertices)

print("\nAnalizando los datos...")

if orden != len(matriz_ad):
    print(
        "\nLa cantidad de vértices no encaja con el número de"
        "\nfilas en la matriz de adyacencia."
        "\n\nRevise el archivo de datos e inténtelo de nuevo.\n\n"
    )
    sys.exit()
elif orden != len(matriz_ad[0]):
    print(
        "\nLa cantidad de vértices no encaja con el número de"
        "\ncolumnas en la matriz de adyacencia."
        "\n\nRevise el archivo de datos e inténtelo de nuevo.\n\n"
    )
    sys.exit()
else:
    for i in range(orden):
        if matriz_ad[i][i] != 0:
            matriz_ad[i][i] = 0
            if not swAR:
                swAR = True
                print("\nLa matriz no representa un grafo simple."
                      "\nSe omitirán los lazos.\n")

print("Datos verificados exitosamente.\n\nProsiguiendo...\n")

# ──────────────────────────────────────────────
# Paso 1: Construir la matriz H^1
# Cada celda (i, j) con arista contiene el camino [i, j] (índices internos).
# Los índices internos van de 0 a n-1; se traducen a nombres de vértice al imprimir.
# ──────────────────────────────────────────────

# matrizH almacena listas de caminos; cada camino es una lista de índices de vértice
matrizH = [[[] for _ in range(orden)] for _ in range(orden)]

for i in range(orden):
    for j in range(orden):
        if matriz_ad[i][j] != 0:
            # Hay arista entre i y j: el camino elemental es [i, j]
            matrizH[i][j] = [[i, j]]

print("La matriz H^1 es:\n")
imprimir_matriz(matrizH, orden, vertices)

# ──────────────────────────────────────────────
# Pasos 2 y 3: Multiplicación latina iterativa
# Se repite (n-2) veces para obtener H^(n-1).
# En cada paso r, calculamos H^(r+1) = H^r · H^1.
# Cuando r = n-1 la matriz contiene todos los caminos hamiltonianos.
# ──────────────────────────────────────────────

matrizH1 = copy.deepcopy(matrizH)  # H^1 se mantiene fijo como segundo operando
r = 1

while r < orden - 1:
    print(f"Multiplicación latina H^{r} · H^1  →  H^{r+1}:\n")
    matrizH = mult_latina(matrizH, matrizH1, orden)
    r += 1
    print(f"La matriz H^{r} es:\n")
    imprimir_matriz(matrizH, orden, vertices)

# ──────────────────────────────────────────────
# Paso 4: Extraer y mostrar los caminos hamiltonianos
# La fila i de H^(n-1) contiene los caminos hamiltonianos que parten del vértice i.
# ──────────────────────────────────────────────

print("=" * 60)
print(f"CAMINOS HAMILTONIANOS ENCONTRADOS EN H^{orden - 1}:\n")

caminos_totales = []

for i in range(orden):
    for j in range(orden):
        for camino in matrizH[i][j]:
            # Un camino hamiltoniano visita exactamente n vértices distintos
            if len(camino) == orden and len(set(camino)) == orden:
                nombres = [str(vertices[v]) for v in camino]
                caminos_totales.append(nombres)
                print("  (" + ", ".join(nombres) + ")")

if not caminos_totales:
    print("  No se encontraron caminos hamiltonianos.")
    print("  Verifique que el grafo sea semi-hamiltoniano.")

print(f"\nTotal: {len(caminos_totales)} camino(s) hamiltoniano(s).\n")