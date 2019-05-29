import numpy as np
import matplotlib.pyplot as plt

file = open("verkeerssimulatie-rechteweg-snelheden.csv", "r")
positie1 = []
positie2 = []
positie3 = []
regel1 =1
b1 =121
b2 =121
b3 =121
for regel in file:
    if regel1 == 1:
        regel = regel.strip("\n").split(";")
        positie1.append(float(regel[1]))
        positie2.append(float(regel[2]))
        positie3.append(float(regel[3]))
        regel1 = 0
    else:   
        regel = regel.strip("\n").split(";")
        tijd = float(regel[0])        
        auto1 = float(regel[1])
        auto2 = float(regel[2])
        auto3 = float(regel[3])
        positie1.append(positie1[-1]+(0.1*auto1))
        positie2.append(positie2[-1]+(0.1*auto2))
        positie3.append(positie3[-1]+(0.1*auto3))

plt.plot(positie1,'r')
plt.plot(positie2,'g')
plt.plot(positie3,'b')
plt.axis([0, 1200, -10,950])
plt.show()