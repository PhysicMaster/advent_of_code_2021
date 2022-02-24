import numpy as np

class Board():
    
    def __init__(self, values: np.ndarray) -> None:
        
        self.values = values
        self.marked = np.zeros_like(self.values)

    def check_number(self, number):

        position = np.where(self.values==number)


        self.marked[position] = 1

    def _row_win(self, row):
        return sum(row)/len(row) == 1

    def _column_win(self, column):
        return sum(column)/len(column) == 1

    def check_win(self):

        for row in self.marked:
            if self._row_win(row) == True:
                return True

        for column in self.marked.T:
            if self._column_win(column) == True:
                return True
        
        return False


class Game():

    def __init__(self, number_list, board_list) -> None:
        
        self.numbers = number_list
        self.boards = board_list
        
    def run(self):

        another = True
        while another == True:
            another = self._new_turn()

    def _new_turn(self):
        
        for board in self.boards:

            board.check_number(self.numbers[0])
            
            if board.check_win():

                suma = sum(board.values[np.where(board.marked == 0)])
                numero_ganador = self.numbers[0]

                print(f'Bingo! The answer is {suma * numero_ganador}')
                return False


        if len(self.numbers) == 1:
            print(f'El juego terminó sin ganador')
            return False
        self.numbers = self.numbers[1:]
        return True



class ModifiedGame():

    def __init__(self, number_list, board_list) -> None:
        
        self.numbers = number_list
        self.boards = board_list
        
    def run(self):

        another = True
        while another == True:
            another = self._new_turn()

    def _new_turn(self):
        
        for board in reversed(self.boards):

            board.check_number(self.numbers[0])
            number = self.numbers[0]
            
            if board.check_win():

                if len(self.boards) == 1:

                    suma = sum(self.boards[0].values[np.where(board.marked == 0)])
                    numero_ganador = self.numbers[0]
                    print(suma)
                    print(numero_ganador)
                    print(f'Tenemos perdedor! La respuesta es {suma*numero_ganador}')
                    return False
                
                else:
                    self.boards.remove(board)

        if len(self.numbers) == 1:
            print(f'El juego terminó sin perdedor')
            return False
        self.numbers = self.numbers[1:]
        return True






archivo = './Inputs/example4.txt'
archivo = './Inputs/input4.txt'


with open(archivo) as data:

    numeros = data.readline().split(',')
    next(data)

    list_of_boards = []
    matrix = []

    for line in data:

        if len(line.split()) == 0:
            list_of_boards.append(matrix)
            matrix = []

        else:
            matrix.append(line.split())
    
    list_of_boards.append(matrix)


#Pasar str a int

numeros = [int(numero) for numero in numeros]
list_of_boards = [[[int(numero) for numero in row] for row in board] for board in list_of_boards]


list_of_boards = [Board(np.array(board)) for board in list_of_boards]


game = Game(numeros, list_of_boards)
#game.run()

game2 = ModifiedGame(numeros, list_of_boards)
game2.run()


