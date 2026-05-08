import sys
import copy
import data

def mult_latina(matrizH, matrizH1, orden):
    tempMatrix = copy.deepcopy(matrizH1)
    for i in range(orden):
        for j in range(orden):
            cont_comb = 0
            ACT_ult_dig = str(matrizH[i][j])[-1]
            print("Último digito vaino: " + ACT_ult_dig)
            if ACT_ult_dig != "0":
                for k in range(orden):
                    print("Matriz destino vaino: " + matrizH1[i][k])
                    if str(matrizH1[i][k])[0] == ACT_ult_dig and cont_comb == 0:
                        tempMatrix[i][j] = ACT_ult_dig + str(matrizH1[i][k])[1:]
                        print("Encontrado amen")
                        cont_comb += 1
                    elif str(matrizH1[i][k])[0] == ACT_ult_dig and cont_comb > 0:
                        tempMatrix[i][j] += "," + ACT_ult_dig + str(matrizH1[i][k])[1:]
                for k in range(orden):
                    print(f"Matriz destino vaino {k}: " + matrizH1[k][j])
                    if str(matrizH1[k][j])[0] == ACT_ult_dig and cont_comb == 0:
                        tempMatrix[i][j] = ACT_ult_dig + str(matrizH1[k][j])[1:]
                        print("Encontrado amen")
                        cont_comb += 1
                    elif str(matrizH1[k][j])[0] == ACT_ult_dig and cont_comb > 0:
                        tempMatrix[i][j] += "," + ACT_ult_dig + str(matrizH1[k][j])[1:]
            else:
                tempMatrix[i][j] = "0"
            if cont_comb == 0:
                tempMatrix[i][j] = "0"
            print(tempMatrix[i][j], end="       ")
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

