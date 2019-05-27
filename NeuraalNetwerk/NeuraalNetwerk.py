import sys, json
import numpy as np
from pprint import pprint

# python .\NeuraalNetwerk.py example-2layer.json

with open(sys.argv[1]) as f:
    data = json.load(f)

VectorX = np.array([1,1,1,1,1])
for layer in data:
    layer = data[layer]
    shape = (int(layer["size_out"]),int(layer["size_in"]))
    Matrix0 = np.zeros(shape)
    for laag in layer["weights"]:
        for getal in layer["weights"][laag]:
            waarde = float(layer["weights"][laag][getal])*(VectorX[int(laag)-1])
            Matrix0[int(getal)-1,int(laag)-1] = waarde
    # print(Matrix0.astype(float))
    VectorX = (np.sum(Matrix0, axis=1))
VectorY = VectorX
print(VectorY)