'''
Author: Andy Shaw
Date:   11/18/2013
Course: CSE 3521 - Assignment 04

This is the place class.  It keeps track of a state id number, a reward, and a description of the
place.
'''

class Place():
    ''' Place on campus.'''
    
    def __init__(self, id, reward, description):
        self.id = id
        self.reward = reward
        self.description = description
        
    def getId(self):
        return self.id
        
    def getReward(self):
        return self.reward
        
    def getDescription(self):
        return self.description
            