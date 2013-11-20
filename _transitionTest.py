from transition import *
from place import Place
import os


file = open(os.getcwd() + r'\Input_Files\deterministic_transitions.txt', 'r')
input = file.readlines()

transitions = []

for line in input:
    x = line.rstrip().split(',')
    
    fromPlace = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    transitions.append(Transition(fromPlace, action, pairs))
    
for trans in transitions:
    p = 0.0
    for place in trans.getDestinationPlaces():
        p = p + trans.probabilityOfPlace(place)
    assert (p == 1.0)
    
file.close()

file = open(os.getcwd() + r'\Input_Files\non-deterministic_transistions.txt', 'r')
input = file.readlines()

transitions = []
for line in input:
    x = line.rstrip().split(',')
    
    fromPlace = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    transitions.append(Transition(fromPlace, action, pairs))

#test for probabilities summing to 1 and correct input
for trans in transitions:
    p = 0.0
    for place in trans.getDestinationPlaces():
        p += trans.probabilityOfPlace(place)

    assert(str(p) == '1.0') #BIG HACK  ---- do not try at home, kids
    
file = open(os.getcwd() + r'\Input_Files\places.txt', 'r')
input = file.readlines()
places = []

for line in input:
    x = line.rstrip().split(',')
    
    #build place
    id = int(x[0])
    name = x[1]
    reward = float(x[3])
    description = x[4]
    
    places.append(Place(id, name, reward, description))
    
for place in places:
    id = place.getId()
    x = getTransitions(id, transitions)
    for trans in x:
        assert(id == trans.getFromPlace())
    
file.close()