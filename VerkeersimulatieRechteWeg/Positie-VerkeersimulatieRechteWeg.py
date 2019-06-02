import numpy as np
import matplotlib.pyplot as plt

file = open("verkeerssimulatie-rechteweg-posities.csv", "r")
auto1 = []
auto2 = []
for regel in file:
    regel = regel.split(";")
    auto1.append(float(regel[1]))
    auto2.append(float(regel[2]))

snelheden1 = []
verschillen = np.diff(auto1)
for verschil in verschillen:
        snelheid = verschil/0.1   
        snelheden1.append(snelheid)

snelheden2 = []
verschillen = np.diff(auto2)
for verschil in verschillen:
        snelheid = verschil/0.1   
        snelheden2.append(snelheid)

print("De Topsnelheid van Auto 1:\n{}\nEn de Langzaamste snelheid van Auto 1:\n{}\n".format(round(max(snelheden1),3),round(min(snelheden1),3)))
print("De Topsnelheid van Auto 2:\n{}\nEn de Langzaamste snelheid van Auto 2:\n{}\n".format(round(max(snelheden2),3),round(min(snelheden2),3)))

plt.plot(snelheden1)
plt.plot(snelheden2)
plt.axis([0, 220, 0, 7])
plt.show()