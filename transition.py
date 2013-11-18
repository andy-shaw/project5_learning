'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

This class is a transition.  The class contains the current state, the action taken, a list of 
the states resulting from that action, and the probability that the the resulting state is what 
actually is the result.
'''

class Transition:
    '''transition properties'''
    
    def __init__(self, fromState, action, destinationStates):
        '''fromState, action, destinationStates is list of state,probability pairs'''
        self.fromState = fromState
        self.action = action
        self.destinationStates = destinationStates

    def getAction(self):
        return self.action
        
    def getFromState(self):
        return self.fromState
        
    def getDestinationStates(self):
        states = []
        for state in self.destinationStates:
            states.append(state[0])
        return states
        
    def indexOfState(self, state):
        for i in range(len(self.destinationStates)):
            if self.destinationStates[i][0] == state:
                return i
        
    def toString(self):
        s = ''
        s += str(self.fromState) +'\t'+ str(self.action)
        for dest in self.destinationStates:
            s += '\t' + repr(dest)
            
        return s
        
    def probabilityOfState(self, state):
        '''return the probability of the given state'''
        for i in self.destinationStates:
            #i is the pair: state, probability
            if i[0] == state:
                return i[1]