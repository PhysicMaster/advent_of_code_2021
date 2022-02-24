import numpy as np


def find_low_points(matrix):
    low_points = np.zeros_like(matrix)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    #Center of the matrix
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if data[i, j] < data[i-1, j]:
                if data[i, j] < data[i+1, j]:
                    if data[i, j] < data[i, j-1]:
                        if data[i, j] < data[i, j+1]:
                            low_points[i, j] = 1
    #Row 1 minus corners
    for j in range(1, cols-1):
        if data[0, j] < data[1, j]:
            if data[0, j] < data[0, j-1]:
                if data[0, j] < data[0, j+1]:
                    low_points[0, j] = 1
    #Last row minus corners
    for j in range(1, cols-1):
        if data[rows-1, j] < data[rows-2, j]:
            if data[rows-1, j] < data[rows-1, j-1]:
                if data[rows-1, j] < data[rows-1, j+1]:
                    low_points[rows-1, j] = 1
    #Col 1 minus corners
    for i in range(1, rows-1):
        if data[i, 0] < data[i, 1]:
            if data[i, 0] < data[i-1, 0]:
                if data[i, 0] < data[i+1, 0]:
                    low_points[i, 0] = 1
    #Last col minus corners
    for i in range(1, rows-1):
        if data[i, cols-1] < data[i, cols-2]:
            if data[i, cols-1] < data[i-1, cols-1]:
                if data[i, cols-1] < data[i+1, cols-1]:
                    low_points[i, cols-1] = 1
    #Corners
    if data[0, 0] < data[1, 0]:
        if data[0, 0] < data[0, 1]:
            low_points[0, 0] = 1
    if data[0, cols-1] < data[0, cols-2]:
        if data[0, cols-1] < data[1, cols-1]:
            low_points[0, cols-1] = 1
    if data[rows-1, 0] < data[rows-1, 1]:
        if data[rows-1, 0] < data[rows-2, 0]:
            low_points[rows-1, 0] = 1
    if data[rows-1, cols-1] < data[rows-2, cols-1]:
        if data[rows-1, cols-1] < data[rows-1, cols-2]:
            low_points[rows-1, cols-1] = 1

    return low_points




archivo = './Inputs/example9.txt'
archivo = './Inputs/input9.txt'

data = np.genfromtxt(archivo, delimiter=1)

low_points = find_low_points(data)

risk = np.dot(data+1, low_points.T)
risk = sum(np.diag(risk))


print(risk)
