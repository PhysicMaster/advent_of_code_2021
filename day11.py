import numpy as np


class Board():

    def __init__(self, matrix) -> None:
        self.board = matrix
        self.n_flashes = 0
        self.simultaneous_flash = None
        self.step = 0
    
    def run(self, steps):
        for i in range(steps):
            self._next_step()

    def _next_step(self):

        self.step += 1

        #First part: all up by one
        self.board += 1
        #Second part: all above 9 flash and cause chain reaction
        flashed = []
        new_flash = [[i for i in item] for item in np.argwhere(self.board > 9)]
        while len(new_flash)>0:
            for octopus in new_flash:
                self._flash(octopus)
                flashed.append(octopus)
            new_flash = [[i for i in item] for item in np.argwhere(self.board > 9)]
            new_flash = [item for item in new_flash if item not in flashed]
        #Final part: all flashed go to 0
        for i,j in flashed:
            self.board[i,j] = 0
        #Sum the amount of flashes
        self.n_flashes += len(flashed)
        if len(flashed) == 100 and self.simultaneous_flash == None:
            self.simultaneous_flash = self.step

    def _flash(self, position):
        neighbors = self._find_neighbors(position)
        self.board[neighbors] += 1

    def _find_neighbors(self, position):
        i, j = position
        rows, columns = self.board.shape
        neighbors = [[], []]
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):    
                if k >= 0 and k < rows and l >= 0 and l < columns:
                    neighbors[0].append(k)
                    neighbors[1].append(l)
        return (np.array(neighbors[0]), np.array(neighbors[1]))



archivo = './Inputs/example11.txt'
archivo = './Inputs/input11.txt'

data = np.genfromtxt(archivo, delimiter=1)

example = np.array([
    [1,1,1,1,1],
    [1,9,9,9,1],
    [1,9,1,9,1],
    [1,9,9,9,1],
    [1,1,1,1,1],
])


a = Board(data)
a.run(500)
print(a.n_flashes)
print(a.simultaneous_flash)

