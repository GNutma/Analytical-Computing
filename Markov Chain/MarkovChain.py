import numpy as np

state0 = [0.1, 0.7, 0.2]  # Hongerig, Tevreden, Opgejaagd
transitionName = [["HH", "HT", "HO"], 
                  ["TH", "TT", "TO"], 
                  ["OH", "OT", "OO"]]
transitionMatrix  = [[0.8, 0.1, 0.1], 
                     [0.4, 0.5, 0.1], 
                     [0.6, 0.2, 0.2]]
for row in nstate:
    print(row)
    print(np.dot(state0,row))