'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

The learner will read in a set of places and transition properties from CSV text files, and
    determine
    
'''
from place import Place
from transition import Transition, getTransitions
from state import State, getState, compareStates
import random

def main(places, transitions):

    numberOfRestarts = 50

    #initialize states to 0
    states = []
    for place in places:
        states.append(State(0, place, getTransitions(place.getId(), transitions)))
    
    #declare state for scope
    
    for i in range(numberOfRestarts):
        #select a random state to start in
        state = states[random.randint(0, len(states) -1)]

        print state
        while not state.isTerminal():
            #update the utility for that state
            state.updateUtility(states)

            #if not a terminal, then choose the state from the best transition
            state = getState(state.getBestTransition().choosePlace(), states)

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