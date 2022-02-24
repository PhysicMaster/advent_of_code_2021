import numpy as np


def binlist2int(lista):
    num = 0
    for item in lista:
        num = num*2 + item
    return num

archivo = './Inputs/example3.txt'
archivo = './Inputs/input3.txt'

data = np.genfromtxt(archivo, delimiter=1)

column_sum = np.sum(data, axis=0)

gamma = np.round(column_sum / data.shape[0])

epsilon = [1]*data.shape[1] - gamma

power_consumption = binlist2int(gamma)* binlist2int(epsilon)

print(f'gamma {gamma} epsilon {epsilon} pow {power_consumption}')



oxygen = np.copy(data)

for i in range(oxygen.shape[1]):

    if oxygen.shape[0] == 1:
        break

    mean =  sum(oxygen[:, i]) / oxygen.shape[0]

    if mean == 0.5:
        mean = 1

    good = np.round(mean)

    good = np.where(oxygen[:, i] == good)

    oxygen = oxygen[ good ]

print(oxygen)



co2 = np.copy(data)

for i in range(co2.shape[1]):

    if co2.shape[0] == 1:
        break

    mean =  sum(co2[:, i]) / co2.shape[0]

    if mean == 0.5:
        mean = 1

    good = 1 - np.round(mean)

    good = np.where(co2[:, i] == good)

    co2 = co2[ good ]

print(co2)

print(f'life support {binlist2int(oxygen[0]) * binlist2int(co2[0])} ')