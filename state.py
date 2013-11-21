'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

The state holds the current utility/value of the location, the place, and the possible outgoing
transitions.
'''

class State:
    '''utility, place, and possible transitions'''
    def __init__(self, utility, place, transitions):
        self.utility = utility
        self.place = place
        self.id = place.getId()
        self.transitions = transitions
        
    def getUtility(self):
        return self.utility
        
    def getPlace(self):
        return self.place
        
    def getId(self):
        return self.id
        
    def getTransitions(self):
        return self.transitions
        
    '''
    This method will update the utility of the State.  This algorithm will look at destination
    states, so all states in the environment need to be passed.  It is assumed that gamma is 1.
    
    param: allStates all states that are in the environment
    '''
    def updateUtility(self, allStates):
        '''utility = reward + maxAction(sum of all probabilities * neighbor utility)'''
        reward = self.place.getReward()
        
        possibleActions = []
        #get all actions
        for transition in self.transitions:
            x = 0.0
            for destination in transition.getDestinationPlaces():
                x += transition.probabilityOfPlace() * getState(destination, allStates).getUtility()
            
            possibleActions.append((x, transition))
            
        #choose the best action
        bestAction = max(possibleActions)
        
        self.utility = reward + bestAction

'''
Given an id, and a set of states, this function returns the state with the matching id.

param: id id of a state
param: states set of states to search in
return: state with provided id, or -1 if not found
'''
def getState(id, states):
    for state in states:
        if state.getId() == id:
            return state
    return -1