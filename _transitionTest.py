from transition import *
from place import Place
import os
import sys

debug = False
try:
    y = sys.argv[1]
    if y: debug = True
except:
    pass

file = open(os.getcwd() + r'\Input_Files\deterministic_transitions.txt', 'r')
input = file.readlines()

dtransitions = []

for line in input:
    x = line.rstrip().split(',')
    
    fromPlace = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    dtransitions.append(Transition(fromPlace, action, pairs))
    
for trans in dtransitions:
    p = 0.0
    for place in trans.getDestinationPlaces():
        p = p + trans.probabilityOfPlace(place)
    assert (p == 1.0)
    if debug: print trans.toString()
    
file.close()

if debug:print '========================================'

file = open(os.getcwd() + r'\Input_Files\non-deterministic_transitions.txt', 'r')
input = file.readlines()

ndtransitions = []
for line in input:
    x = line.rstrip().split(',')
    
    fromPlace = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    ndtransitions.append(Transition(fromPlace, action, pairs))

#test for probabilities summing to 1 and correct input
for trans in ndtransitions:
    p = 0.0
    for place in trans.getDestinationPlaces():
        p += trans.probabilityOfPlace(place)

    assert(str(p) == '1.0') #BIG HACK  ---- do not try at home, kids
    if debug: print trans.toString()
    
if debug: print '========================================'

#test getTransitions
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
    
    #pair up the ndtransitions with the fromPlace
for place in places:
    id = place.getId()
    x = getTransitions(id, ndtransitions)
    if debug: print '-->' + str(id)
    for trans in x:
        if debug: print trans.toString()
        assert(id == trans.getFromPlace())
    if debug: print '________________________________________________________________\n'
    
    
file.close()