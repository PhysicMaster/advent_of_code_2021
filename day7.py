import numpy as np

archivo = './Inputs/example7.txt'
archivo = './Inputs/input7.txt'

with open(archivo) as data:

    for line in data:

        crabs = line.split(',')

crabs = np.array([int(crab) for crab in crabs])

left_crab = min(crabs)
right_crab = max(crabs)
max_dist = right_crab - left_crab



total_spent = []
for x_pos in range(left_crab, right_crab+1):

    fuel_spent = [abs(crab - x_pos) for crab in crabs]
    total_spent.append(fuel_spent)

total_spent = np.array(total_spent)
total_spent = np.sum(total_spent, axis=1)

print(f'The minimum field needed is {min(total_spent)}')





def triang(number: int):
    return int(number*(number+1)/2)


total_spent = []
for x_pos in range(left_crab, right_crab+1):

    steps = [abs(crab - x_pos) for crab in crabs]
    fuel_spent = [triang(step) for step in steps]
    total_spent.append(fuel_spent)

total_spent = np.array(total_spent)
total_spent = np.sum(total_spent, axis=1)

print(f'The minimum field needed is {min(total_spent)}')