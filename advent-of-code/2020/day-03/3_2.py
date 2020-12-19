import sys

def countTree(grid, right, down):
    h = len(grid)
    w = len(grid[0])
    c = 0
    for i in range(down, h, down):
        if grid[i][(right * (i//down)) % w] == '#':
            c += 1
    return c

def main():
    with open("input") as f:
        data = f.read().splitlines()
    res = 1
    for i,j in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        print(i,j,countTree(data,i,j))
        res *= countTree(data, i, j)
    print(res)

main()
