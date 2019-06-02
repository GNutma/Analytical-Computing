import numpy as np
import matplotlib.pyplot as plt

file = open("verkeerssimulatie-rechteweg-snelheden.csv", "r")
positie1 = []
positie2 = []
positie3 = []
regel1 =1
b1 =0
b2 =0
b3 =0
for regel in file:
    if regel1 == 1:
        regel = regel.split(";")
        positie1.append(float(regel[1]))
        positie2.append(float(regel[2]))
        positie3.append(float(regel[3]))
        regel1 = 0
    else:   
        regel = regel.split(";")
        tijd = float(regel[0])        
        auto1 = float(regel[1])
        auto2 = float(regel[2])
        auto3 = float(regel[3])
        positie1.append(positie1[-1]+(0.1*auto1))
        positie2.append(positie2[-1]+(0.1*auto2))
        positie3.append(positie3[-1]+(0.1*auto3))
        if (positie2[-1]+1) >= (positie1[-1]-1) and b1 == 0:
            b1 = tijd
            print("Er is een botsing plaatsgevonden tussen auto 2 en 1 om tijdstip: {}".format(tijd))
        if (positie3[-1]+1) >= (positie1[-1]-1) and b2 == 0:
            b2 = tijd
            print("Er is een botsing plaatsgevonden tussen auto 3 en 1 om tijdstip: {}".format(tijd))
        if (positie2[-1]+1) >= (positie3[-1]-1) and b3 == 0:
            b3 = tijd
            print("Er is een botsing plaatsgevonden tussen auto 3 en 3 om tijdstip: {}".format(tijd))

plt.plot(positie1,'r')
plt.plot(positie2,'g')
plt.plot(positie3,'b')
plt.axis([0, 1200, -10,950])
plt.show()