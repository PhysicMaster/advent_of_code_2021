import numpy as np
from collections import deque



def count(list_of_fish):

    lista = np.zeros(9)

    for number in range(0, 9):
        lista[number] = list_of_fish.count(number)

    return lista



archivo = './Inputs/example6.txt'
archivo = './Inputs/input6.txt'

with open(archivo) as data:
    for line in data:
        state = line.split(',')


#list of fishes, each item is a fish with X days left to reproduce
state = [int(d) for d in state]


#now in the list each item says how many fishes have i days left
state = count(state)
state = [int(d) for d in state]
state = deque(state)



ndays = 10000000

for day in range(ndays):

    #Añado como dia 7 los hijos para que pasen a 6
    state[7] += state[0]

    state.rotate(-1)

print(f'After {ndays} days, there are {sum(state)} fishes')

