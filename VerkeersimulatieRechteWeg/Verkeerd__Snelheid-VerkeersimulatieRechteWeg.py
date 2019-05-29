import numpy as np
import matplotlib.pyplot as plt
import csv

tijd = []
auto1 = []
auto2 = []
auto3 = []
with open("verkeerssimulatie-rechteweg-snelheden.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for regel in reader:
        tijd.append(float(regel[0]))
        auto1.append(float(regel[1]))
        auto2.append(float(regel[2])) 
        auto3.append(float(regel[3]))
tijd.pop(0)
x= tijd
p1 = auto1.pop(0)
p2 = auto2.pop(0)
p3 = auto3.pop(0)
print(p1,p2,p3)
positie1 = [np.trapz(auto1[0:i+2],tijd[0:i+2]) + p1 for i in range(len(tijd)-1)]
positie2 = [np.trapz(auto2[0:i+2],tijd[0:i+2]) + p2 for i in range(len(tijd)-1)]
positie3 = [np.trapz(auto3[0:i+2],tijd[0:i+2]) + p3 for i in range(len(tijd)-1)]


b1 =121
b2 =121
b3 =121
v = 0
for x in range(len(tijd)-1):
    if (positie2[v]+1) >= (positie1[v]-1) and b1 > tijd[v]:
        b1 = tijd[v]
        print("Er is een bosting plaatsgevonde tussen auto 1 en auto 2 om {}\n".format(b1))
    if (positie3[v]+1) >= (positie1[v]-1) and b2 > tijd[v]:
        b2 = tijd[v]
        print("Er is een bosting plaatsgevonde tussen auto 1 en auto 3 om {}\n".format(b2))
    if (positie2[v]+1) >= (positie3[v]-1) and b3 > tijd[v]:
        b3 = tijd[v]
        print("Er is een bosting plaatsgevonde tussen auto 1 en auto 2 om {}\n".format(b3))
    v+=1

plt.plot(positie1,'r')
plt.plot(positie2,'g')
plt.plot(positie3,'b')
plt.axis([0, 1200, -10,950])
plt.show()

