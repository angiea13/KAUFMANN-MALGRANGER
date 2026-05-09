import sys
import copy
import data

#LA LÓGICA ESTÁ MALA MALÍSIMA
def mult_latina(matrizH, matrizH1, orden):
    # matriz resultado, inicializada en vacío
    tempMatrix = [[0 for _ in range(orden)] for _ in range(orden)]
    
    for i in range(orden):
        for j in range(orden):
            for k in range(orden):
                camino1 = set(matrizH[i][k])
                camino2 = set(matrizH1[k][j])                
                if set(camino1) & set(camino2) == {k}:
                    tempMatrix[i][j] += str(set(camino1)) + str(set(camino2)[1:])                        
            print(str(tempMatrix[i][j]), end="      ")
        print()
    return tempMatrix

swAR = False
vertices = data.n_vertex
matriz_ad = data.adcy_matrix
orden = len(vertices)

print("\nAnalizando los datos...")

if orden != len(matriz_ad):
    print("\nLa cantidad de vértices no encaja con el número de\nfilas en la matriz de adyacencia.\n\nRevise el archivo de datos e inténtelo de nuevo.\n\n")
    sys.exit()
elif orden != len(matriz_ad[0]):
    print("\nLa cantidad de vértices no encaja con el número de\nfilas en la matriz de adyacencia.\n\nRevise el archivo de datos e inténtelo de nuevo.\n\n")
    sys.exit()
else:
    for i in range(orden):
        if matriz_ad[i][i] != 0:
            matriz_ad[i][i] = 0
            if  not swAR:
                swAR = True
                print("\nLa matriz no representa un grafo simple.\nSe omitirán los lazos.\n")
print("Datos verificados exitosamente.\n\nProsiguiendo...\n")

matriz_H = copy.deepcopy(matriz_ad)

print("La matriz H^1 es:\n")

for i in range(orden):
    for j in range(orden):
        if matriz_ad[i][j] == 0:
            matriz_H[i][j] = "0"
        else:
            matriz_H[i][j] = str(vertices[i]) + str(vertices[j])
        print(matriz_H[i][j], end="     ")
    print("")

print("\nLA MULT. LATINA 1 DA:")
matrizH2 = mult_latina(matriz_H, matriz_H, orden)

