'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

The state holds the current weight/value of the location, the place, and the possible outgoing
transitions.
'''

class State:
    '''Weight, place, and possible transitions'''
    def __init__(self, weight, place, transitions):
        self.weight = weight
        self.place = place
        self.transitions = transitions
        
    def getTransitions(self):
        return transitions
        
    def updateWeight(self):
        self.weight = 