import numpy as np

archivo = './Inputs/example5.txt'
archivo = './Inputs/input5.txt'


origins = []
ends = []

with open(archivo) as data:

    for line in data:

        origin = line.split()[0]
        end = line.split()[2]

        origins.append(origin.split(','))
        ends.append(end.split(','))

origins = [[int(point) for point in origin] for origin in origins]
ends = [[int(point) for point in end] for end in ends]

origins = np.array(origins)
ends = np.array(ends)

max_x = max(max(origins[:, 0]), max(ends[:, 0]))
max_y = max(max(origins[:, 1]), max(ends[:, 1]))


field = np.zeros((max_y+1, max_x+1))

for i in range(origins.shape[0]):

    if origins[i][0] == ends[i][0]: #misma x
        
        x = origins[i][0]
        y1 = origins[i][1]
        y2 = ends[i][1]

        if y2 > y1:
            for y in range(y1, y2+1):
                field[y, x] += 1
        elif y1 > y2:
            for y in range(y2, y1+1):
                field[y, x] += 1

        else:
            field[x,x] += 1

    elif origins[i][1] == ends[i][1]: #same y

        y = origins[i][1]
        x1 = origins[i][0]
        x2 = ends[i][0]

        if x2 > x1:
            for x in range(x1, x2+1):
                field[y, x] += 1

        elif x1 > x2:
            for x in range(x2, x1+1):
                field[y, x] += 1

        else:
            field[x, x] += 1

    else: #diagonal lines

        x1 = origins[i][0]
        x2 = ends[i][0]
        y1 = origins[i][1]
        y2 = ends[i][1]

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        y = y1
        for x in range(x1, x2+1):
            field[y, x] += 1
            y += int( (y2-y1)/abs(y2-y1) )


          
print(field)

print(f'Hay {len(np.where(field>=2)[0])} puntos peligrosos')