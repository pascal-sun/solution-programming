import sys

def nbAdjOccupied(data, x, y):
    occupied = 0
    for i,j in [(-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]:
        if 0 <= x+i < len(data) and 0 <= y+j < len(data[0]):
            if data[x+i][y+j] == '#':
                occupied += 1
    return occupied

def nbOccupied(data):
    nb = 0
    for d in data:
        nb += d.count('#')
    return nb

def kursii(data):
    tmp = []
    for d in data:
        t = d.copy()
        tmp.append(t)

    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            if data[i][j] != '.':
                occupied = nbAdjOccupied(data, i, j)
                if data[i][j] == 'L' and occupied == 0:
                    tmp[i][j] = '#'
                elif data[i][j] == '#' and occupied >= 4:
                    tmp[i][j] = 'L'

    return tmp

def prettyPrint(data):
    for d in data:
        print(*d, sep='')
    print()

def main():
    with open('input') as f:
        data = list(map(list, f.read().splitlines()))

    previous = data
    current = kursii(data)

    while previous != current:
        previous, current = current, kursii(current)

    print(nbOccupied(current))
main()
    
