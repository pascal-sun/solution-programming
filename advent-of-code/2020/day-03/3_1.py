import sys

def countTree(grid):
    h = len(grid)
    w = len(grid[0])
    c = 0
    for i in range(1, h):
        if grid[i][(3*i) % w] == '#':
            c += 1
    return c

def main():
    with open("input") as f:
        data = f.read().splitlines()
    print(countTree(data))
    
main()
