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
    
    def __init__(self, fromPlace, action, destinationPlaces):
        '''fromPlace, action, destinationStates is list of place,probability pairs'''
        self.fromPlace = fromPlace
        self.action = action
        self.destinationPlaces = destinationPlaces

    def getAction(self):
        return self.action
        
    def getFromPlace(self):
        return self.fromPlace
        
    def getDestinationPlaces(self):
        places = []
        for place in self.destinationPlaces:
            places.append(place[0])
        return places
        
    def indexOfPlace(self, place):
        for i in range(len(self.destinationPlaces)):
            if self.destinationPlaces[i][0] == place:
                return i
        
    def toString(self):
        s = ''
        s += str(self.fromPlace) +'\t'+ str(self.action)
        for dest in self.destinationPlaces:
            s += '\t' + repr(dest)
        return s

    def probabilityOfPlace(self, place):
        '''return the probability of the given place'''
        for i in self.destinationPlaces:
            #i is the pair: place, probability
            if i[0] == place:
                return i[1]

'''
Given a list of transitions, this method with find all transitions that start from
the provided place id.

param: id place id
param: transitions list of transitions
returns: list of transitions that originate at id
'''
def getTransitions(id, transitions):
    result = []
    for transition in transitions:
        if transition.getFromPlace() == id:
            result.append(transition)
    return result