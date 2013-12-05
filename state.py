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
        self.bestTransition = None
        
    def getUtility(self):
        return self.utility
        
    def getPlace(self):
        return self.place
        
    def getId(self):
        return self.id
        
    def getTransitions(self):
        return self.transitions
        
    def getBestTransition(self):
        return self.bestTransition
        
    def isTerminal(self):
        return len(self.transitions) == 0
        
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
                x += transition.probabilityOfPlace(destination) * getState(destination, allStates).getUtility()
            
            possibleActions.append((x, transition))
            
        #choose the best action, and value is 0 if no action is 
        if len(possibleActions) > 0: 
            bestAction = max(possibleActions)[0]
            self.bestTransition = max(possibleActions)[1]
        else: 
            bestAction = 0
        
        self.utility = reward + bestAction
        
    '''
    This method will return a string representing Bellman's update formula.  This method calculates
    the neighbors of the current state, so all states have to be provided.
    
    param: allStates all states that are in the environment
    return: string representation of the formula
    '''
    def getFormula(self, allStates, terminal=False):
        '''get string representation of Bellman update'''
        formula = ''
        reward = round(self.place.getReward(), 4)
        
        if terminal: return str(reward)
        
        transition = self.bestTransition
        
        strPossibleActions = []
        for dest in transition.getDestinationPlaces():
            s = '(' + str(transition.probabilityOfPlace(dest)) + '*' 
            s += str(round(getState(dest, allStates).getUtility(), 4)) + ')'
            strPossibleActions.append(s)
            
        # build string
        formula += str(reward)
        
        formula += '+' + "+".join(strPossibleActions)
            
        return formula
        
'''
This method compares 2 states given, and returns a neg, 0, or pos number depending
on if the first element is greater than, equal to, or less than the second.

param: state1 first state 
param: state2 second state
return: neg if first is less than second, 0 if equal, pos if first is greater than second
'''
def compareStates(state1, state2):
    if state1.getUtility > state2.getUtility: return 1
    elif state1.getUtility == state2.getUtility: return 0
    elif state1.getUtility < state2.getUtility: return -1
        
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