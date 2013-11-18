from place import Place
import os

file = open(os.getcwd() + r'\Input_Files\places.txt', 'r')
input = file.readlines()

places = []
for line in input:
    x = line.rstrip().split(',')
    
    id = int(x[0])
    name = x[1]
    reward = float(x[3])
    description = x[4]
    
    places.append(Place(id, name, reward, description))
    
for place in places:
    print place.toString()