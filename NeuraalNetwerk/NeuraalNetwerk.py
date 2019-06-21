import sys
import json
import numpy as np
from pprint import pprint

# python .\NeuraalNetwerk.py example-2layer.json

def MatrixVermenigvuldiging(matrix1, matrix2):
    Vermenigdvuldig_Matrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    for a in range(0, len(matrix1)):
        for b in range(0, len(matrix2[0])):
            for c in range(0, len(matrix1[0])):
                Vermenigdvuldig_Matrix[a][b] += matrix1[a][c] * matrix2[c][b]
    return Vermenigdvuldig_Matrix


def printmatrix(matrix):
    print("Matrix van laag {}:".format(lagen))
    for row in matrix:
        print("\t",end="")
        for item in row:   
            print(round(item,2), end = '\t')
        print()
    print()

with open(sys.argv[1]) as f:
    data = json.load(f)

VectorX = []
size_in = int(data[list(data.keys())[0]]["size_in"])
for i in range(size_in):
    VectorX.append([1])

print("Inputvector:\n\t",end="")
for item in VectorX:
    print(round(item[0],2), end='\t')
print("\n")

Matrixen = [] 
for layer in data:
    layer = data[layer]
    size_in = int(layer["size_in"])
    size_out = int(layer["size_out"])
    Matrix = np.zeros((size_out,size_in))
    for laag in layer["weights"]:
        for getal in layer["weights"][laag]:
            waarde = float(layer["weights"][laag][getal])*(VectorX[int(laag)-1][0])
            Matrix[int(getal)-1,int(laag)-1] = waarde
    Matrixen.append(Matrix)
    VectorY = (np.sum(Matrix, axis=1))

lagen = 1
for Matrix in Matrixen:
    printmatrix(Matrix)
    lagen +=1

if len(Matrixen) != 1:
    VectorY = Matrixen[0]
    for transition in range(1, len(Matrixen)):
        VectorY = MatrixVermenigvuldiging(Matrixen[transition], VectorY)
    VectorY = MatrixVermenigvuldiging(VectorY, VectorX)
else:
    VectorY = MatrixVermenigvuldiging(Matrixen[0], VectorX)

print("Uitkomen van de matrix(en):\n\t",end="")
for item in VectorY:
    print(round(item[0],2), end='\t')

