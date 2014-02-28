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
import random, math

def main(places, transitions, silent, invisible=False):

    numberOfRestarts = 1000

    #initialize states to 0
    states = []
    for place in places:
        states.append(State(0, place, getTransitions(place.getId(), transitions)))
    
    #declare state for scope
    state = None
    
    #variable to keep track of how many iterations states don't change utilities
    noChange = 0
    total = 99999999
    oldTotal = 1
    converged = 0
    
    for i in range(numberOfRestarts):
        #select a random state to start in
        state = states[random.randint(0, len(states) -1)]
        if not silent and converged == 0: print '' #newline
        
        while not state.isTerminal():
            #update the utility for that state
            state.updateUtility(states)
            
            #use absolute value of oldTotal / total < .9999 as the indicator converged values
            values = []
            for x in states: values.append(x.getUtility())
            total = sum(values)
            if str(total) == str(oldTotal): noChange += 1
            else: noChange = 0
            
            oldTotal = total
            
            if noChange == 10: converged = i
            
            if not silent and converged == 0: print "State:{0}\tBest:{1}\tUtility({2})={3}={4}".format(str(state.getId()).ljust(3), state.getBestTransition().getActionAsString(),state.getId(),  state.getFormula(states), round(state.getUtility(),4))

            #if not a terminal, then choose the state from the best transition
            state = getState(state.getBestTransition().choosePlace(), states)
            
        #update and print terminal state
        state.updateUtility(states)
        
        if not silent and converged == 0: print "State:{0}\tBest:{1}\tUtility({2})={3}={4}".format(str(state.getId()).ljust(3), 'Terminal', state.getId(), state.getFormula(states, True), round(state.getUtility(),4))
        
    
    #output policy

    #output iteration of convergence
    if not invisible: print '\nConsidered converged on iteration {0} of {1}'.format(converged, numberOfRestarts)
    
    if not invisible: print '\nResults'
    if not invisible: print '-'*80
    for state in states:
        if not state.isTerminal(): 
            if not invisible: print 'State:{0}\tUtility = {1}\tPolicy = {2}'.format(str(state.getId()).ljust(3), str(state.getUtility()).ljust(15), state.getBestTransition().getActionAsString())
        else: 
            if not invisible: print 'State:{0}\tUtility = {1}\tPolicy = {2}'.format(str(state.getId()).ljust(3), str(state.getUtility()).ljust(15), 'Terminal')

    return converged

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
        
    try: 
        if sys.argv[3] == "SILENT": silent = True
        else: silent = False
    except: 
        silent = False
        
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

    f = open('stats.txt', 'a')
    stat = main(places, transitions, silent, True)
    f.write(str(stat) + ',')
    f.close()