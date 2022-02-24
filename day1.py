import numpy as np


archivo = './Inputs/example1.txt'
archivo = './Inputs/input1.txt'

data = np.loadtxt(archivo)


increase = []
for i in range(1, len(data)):
    increase.append(1 if data[i]>data[i-1] else 0)

print(f'The number of measurements that increase is {sum(increase)}')


windows = []
for i in range(2, len(data)-1):
    windows.append(1 if data[i]+data[i+1]+data[i-1] 
                      > data[i-1]+data[i]+data[i-2] else 0)

print(f'The number of increased windows is {sum(windows)}')