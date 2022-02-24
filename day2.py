

depth = 0
x = 0


archivo = './Inputs/example2.txt'
archivo = './Inputs/input2.txt'



forward = []
up = []
down = []

with open(archivo) as data:
    for line in data:
        if line.startswith('forward'):
            forward.append(int(line.split()[1]))
        elif line.startswith('up'):
            up.append(int(line.split()[1]))
        elif line.startswith('down'):
            down.append(int(line.split()[1]))

x += sum(forward)
depth += sum(down) - sum(up)

print(f'La posición final es hor = {x} y depth = {depth}, cuya multiplicación da {x*depth}')



##### second part


class Submarine():

    def __init__(self) -> None:
        super().__init__()
        self.depth = 0
        self.x = 0
        self.aim = 0

    def forward(self, value) -> None:
        self.x += value
        self.depth += self.aim*value

    def down(self, value) -> None:
        self.aim += value
    
    def up(self, value) -> None:
        self.aim -= value


sub = Submarine()

with open(archivo) as data:
    for line in data:
        if line.startswith('forward'):
            sub.forward(int(line.split()[1]))
        elif line.startswith('up'):
            sub.up(int(line.split()[1]))
        elif line.startswith('down'):
            sub.down(int(line.split()[1]))

print(f'La posición final es hor = {sub.x} y depth = {sub.depth}, cuya multiplicación es {sub.x*sub.depth}')

