from transition import Transition
import os


file = open(os.getcwd() + r'\Input_Files\deterministic_transitions.txt', 'r')
input = file.readlines()

transitions = []

for line in input:
    x = line.rstrip().split(',')
    
    fromState = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    transitions.append(Transition(fromState, action, pairs))
    
for trans in transitions:
    assert(trans.probabilityOfState(trans.getDestinationStates()[0]) == 1.0)
    print trans.toString()
    
file.close()

file = open(os.getcwd() + r'\Input_Files\non-deterministic_transistions.txt', 'r')
input = file.readlines()

transitions = []
for line in input:
    x = line.rstrip().split(',')
    
    fromState = int(x[0])
    action = x[1]
    pairs = []
    for i in range(2, len(x), 2):
        pairs.append((int(x[i]), float(x[i+1])))
    
    transitions.append(Transition(fromState, action, pairs))
    
for trans in transitions:
    print trans.toString()
    
file.close()