import sys

FILENAME = sys.argv[1]

def parse():
    data = []
    with open(FILENAME) as f:
        lines = f.read().splitlines()
        for line in lines:
            action, value = line[0], int(line[1:])
            data.append((action, value))
    return data

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def finalPositionPart1(instructions):
    posX, posY = 0, 0
    direction = 0
    degrees = {0: 'E', 90: 'N', 180: 'W',270: 'S'}

    for instruction in instructions:
        action, value = instruction

        print(instruction)

        if action == 'F':
            action = degrees[direction % 360]

        if action == 'N':
            posY += value
        elif action == 'S':
            posY -= value
        elif action == 'E':
            posX += value
        elif action == 'W':
            posX -= value
        elif action == 'L':
            direction += value
        elif action == 'R':
            direction -= value
        print(posX,posY)
    return posX, posY

def finalPositionPart2(instructions, waypoint):
    wpX, wY = waypoint
    posX, posY = 0, 0
    direction = 0
    degrees = {0: (0, 0), 90: 'N', 180: 'W',270: 'S'}

    for instruction in instructions:
        action, value = instruction

        print(instruction)

        if action == 'F':
            posX += wpX * value
            posY += wpY * value
        elif action == 'N':
            wpY += value
        elif action == 'S':
            wpY -= value
        elif action == 'E':
            wpX += value
        elif action == 'W':
            wpX -= value
        elif action == 'L':
            
            direction += value
        elif action == 'R':
            direction -= value
        print(posX,posY)
    return posX, posY

def main():
    instructions = parse()
    print(f'Part One: {manhattan((0,0), finalPositionPart1(instructions))}')

main()
