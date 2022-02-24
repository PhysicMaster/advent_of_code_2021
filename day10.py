from pickle import TRUE
import numpy as np


class Chunk:

    OPENED_BY = {
    ')' : '(',
    ']' : '[',
    '>' : '<',
    '}' : '{',
    }

    CLOSED_BY = {
    '(' : ')',
    '[' : ']',
    '<' : '>',
    '{' : '}',
    }

    OPENERS = {'(', '[', '{', '<'}
    ENDERS = {')', ']', '}', '>'}
        

    def __init__(self, string):
        
        self.chunk = list(string)
        self.corrupt = False
        self.first_corrupt_char = None
        self.to_complete = None

        self.corrupt = self._is_corrupt()
 


    def _is_corrupt(self):
        list_openers = []
        for char in self.chunk:
            if char in self.OPENERS:
                list_openers.append(char)
            else:
                if list_openers.pop() != self.OPENED_BY[char]:
                    self.first_corrupt_char = char
                    return True

        #Si llega aquí es que solo es incompleto
        self.to_complete = [self.CLOSED_BY[char] for char in reversed(list_openers)]
        return False
        
        


SCORES_CORRUPT = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}


SCORES_INCOMPLETE = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4,
}


archivo = './Inputs/example10.txt'
archivo = './Inputs/input10.txt'


total_corruption_score = 0
incomplete_scores = []

with open(archivo) as data:

    for line in data:
        something = Chunk(line.rstrip("\n"))
        if something.corrupt:
            print(f'Corrupt line, bad ender {something.first_corrupt_char}')
            total_corruption_score += SCORES_CORRUPT[something.first_corrupt_char]
        else:
            print(f'Incomplete line. Put {something.to_complete} to fix')
            partial_incomplete_score = 0
            for char in something.to_complete:
                partial_incomplete_score *= 5
                partial_incomplete_score += SCORES_INCOMPLETE[char]
            incomplete_scores.append(partial_incomplete_score)
            
incomplete_scores.sort()

print(total_corruption_score)
print(incomplete_scores[int( (len(incomplete_scores)-1)/2 )])