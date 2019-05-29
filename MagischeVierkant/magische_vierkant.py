import numpy
def printVierkant(Vierkant):
    print("  {} {} {}\n  {} {} {}\n  {} {} {}".format(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],))

# gegevenVierkant = numpy.array([0, 3, 0,
#                                0, 0, 9,
#                                6, 0, 0])
# gegevenVierkant = numpy.array([ 0, 3, 0,
#                                 0, 0, 9,
#                                 0, 0, 2])
gegevenVierkant = numpy.array([0, 3, 0,
                               0, 0, 9, 
                               6, 0, 0])
v = gegevenVierkant
print("Gegeven vierkant:")
printVierkant(v)
count = 0
nonzero_location = []
nonzero_getallen = []
for getal in gegevenVierkant:
    if getal != 0:
        nonzero_getallen.append(getal)  # slaat alle getallen die niet 0 zijn op in nonzero_getallen
        nonzero_location.append(count)  # Slaat de locatie op van deze nonzero getallen
    count+= 1
X = numpy.array([[2/3, 0, -1], #Berekening voor X1
                 [2/3, -1, 0], #Berekening voor X2
                 [-1/3, 1, 1], #Berekening voor X3
                 [-2/3, 1, 2], #Berekening voor X4 
                 [1/3, 0, 0],  #Berekening voor X5 
                 [4/3, -1, -2],#Berekening voor X6 
                 [1, -1, -1],  #Berekening voor X7 
                 [0, 1, 0],    #Berekening voor X8 
                 [0, 0, 1]])   #Berekening voor X9
                 
BerekeningX = numpy.array([X[nonzero_location[0]], X[nonzero_location[1]], X[nonzero_location[2]]])
getallen = numpy.array([nonzero_getallen[0],nonzero_getallen[1],nonzero_getallen[2]])

if numpy.linalg.det(BerekeningX) == 0:   # waarde van Determinant wordt bekeken gecontreerd dat deze niet 0 is dit moet eerst want anders is er geen oplossing.
    print("\nBerekening kan niet gemaakt worden,\n    Determinant = 0")
else:
    solve = numpy.linalg.solve(BerekeningX, getallen)    # berekent de ombekenden variabelen
    som = (int(round(solve[0]))) #De voorheen onbekende som
    opgelosteVierkant = [int(round(numpy.dot(getal, solve))) for getal in X]
    v = opgelosteVierkant
    check = [(v[0]+v[1]+v[2]), #Horizontale check
             (v[3]+v[4]+v[5]), #Horizontale check
             (v[6]+v[7]+v[8]), #Horizontale check
             (v[0]+v[3]+v[6]), #Verticale check
             (v[1]+v[4]+v[7]), #Verticale check
             (v[2]+v[5]+v[8]), #Verticale check
             (v[0]+v[4]+v[8]), #Diagonale check
             (v[2]+v[4]+v[6])] #Diagonale check

    gelukt = True
    for total in check: # checkt of de totaal van elke regel gelijk is aan de som
        if total != som:
            gelukt = False

    if gelukt == True:
        print("\nOpgeloste vierkant:")
        printVierkant(v)
    
    if gelukt == False:
        print("\nGeen Oplossing:\n  som is niet gelijk")