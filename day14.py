
from collections import Counter


archivo = './Inputs/example14.txt'
#archivo = './Inputs/input14.txt'
n_steps = 40

insertions = dict()
with open(archivo) as data:
    polymer = data.readline()

    next(data)

    for line in data:
        insertions[line.split()[0]] = line.split()[2]

polymer = polymer.rstrip('\n')

for step in range(n_steps):

    length = len(polymer)

    for i in range(len(polymer)-1, 0, -1):
        
        pair = polymer[i-1:i+1]
        
        if pair in insertions.keys():
            polymer = polymer[:i] + insertions[pair] + polymer[i:]

    counter = Counter(polymer)

    print(f' Step {step+1}: {counter} {counter.most_common()[0][1] - counter.most_common()[-1][1]}')