'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

The learner will read in a set of places and transition properties from CSV text files, and
    determine
    
'''
from place import Place
from transition import Transition, getTransitions
from state import State, getState

def main(places, transitions):
    #initialize states to 0
    states = []
    for place in places:
        states.append(State(0, place, getTransitions(place.getId(), transitions)))
    
    

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    #get command line args
    import sys
    
    placesFile = None
    transitionsFile = None
    
    try:
        placesFile = open(sys.argv[1], 'r')
        transitionsFile = open(sys.argv[2], 'r')
        
    except:
        print 'invalid file name'
        exit()
        
    #process CSV data
    #process places
    input = placesFile.readlines()
    places = []
    
    for line in input:
        x = line.rstrip().split(',')
        
        #build place
        id = int(x[0])
        name = x[1]
        reward = float(x[3])
        description = x[4]
        
        places.append(Place(id, name, reward, description))
    
    placesFile.close()
        
    #process transitions
    input = transitionsFile.readlines()
    transitions = []

    for line in input:
        x = line.rstrip().split(',')
        
        #build transition
        fromPlace = int(x[0])
        action = x[1]
        pairs = []
        for i in range(2, len(x), 2):
            #data is place,probability pairs
            pairs.append((int(x[i]), float(x[i+1])))
        
        transitions.append(Transition(fromPlace, action, pairs))
    
    transitionsFile.close()
    
    main(places, transitions)