import sys

def seatID(boardingPass):
    row, column = boardingPass[:-3], boardingPass[-3:]
    row = int(row.replace('B','1').replace('F','0'),2)
    column = int(column.replace('R','1').replace('L','0'),2)
    return row, column

def main():
    with open("input") as f:
        data = f.read()

    boardingPasses = data.split()
    totalSeat = 127 * 8 + 7

    somme = 0
    veryBack = -1
    veryFron = totalSeat + 1

    res = []
    for boardingPass in boardingPasses:
        row, column = seatID(boardingPass)
        val = row * 8 + column
        somme += val
        res += [val]
        if val > veryBack: veryBack = val
        if val < veryFron: veryFron = val

    sommeBack = veryBack * (veryBack + 1) / 2
    sommeFron = veryFron * (veryFron + 1) / 2
    
    r = sommeBack - (somme + sommeFron - veryFron)
    print(r)

main()
