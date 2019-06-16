import sys, json
import numpy as np
from pprint import pprint

# python .\NeuraalNetwerk.py example-2layer.json

with open(sys.argv[1]) as f:
    data = json.load(f)

for layer in data:
    layer = data[layer]
    size_in = int(layer["size_in"])
    break

VectorX = []
for i in range(size_in):
    VectorX.append(1)

print("Inputvector:\n\t",end="")
for item in VectorX:
    print(round(item,2), end='\t')
print("\n")
lagen = 0
for layer in data:
    layer = data[layer]
    shape = (int(layer["size_out"]),int(layer["size_in"]))
    Matrix = np.zeros(shape)
    lagen +=1
    for laag in layer["weights"]:
        for getal in layer["weights"][laag]:
            waarde = float(layer["weights"][laag][getal])*(VectorX[int(laag)-1])
            Matrix[int(getal)-1,int(laag)-1] = waarde
    print("Matrix van laag {}:".format(lagen))
    for row in Matrix:
        print("\t",end="")
        for item in row:   
            print(round(item,2), end = '\t')
        print()
    print()
    VectorY = (np.sum(Matrix, axis=1))

print("Uitkomen van de matrix(en):\n\t",end="")
for item in VectorY:
    print(round(item,2), end='\t')

