from transition import *
from place import Place
from state import *
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
file.close()

dtransitions = []

for line in input:
    x = line.rstrip().split(',')
    
    fromPlace = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    dtransitions.append(Transition(fromPlace, action, pairs))

if debug: print 'deterministic transitions loaded'

file = open(os.getcwd() + r'\Input_Files\places.txt', 'r')
input = file.readlines()
file.close()

places = []

for line in input:
    x = line.rstrip().split(',')
    
    #build place
    id = int(x[0])
    name = x[1]
    reward = float(x[3])
    description = x[4]
    
    places.append(Place(id, name, reward, description))

if debug: print 'places loaded'
    
dstates = []
for place in places:
    dstates.append(State(0, place, getTransitions(place.getId(), dtransitions)))
    
if debug: print 'states initialized for deterministic transitions'