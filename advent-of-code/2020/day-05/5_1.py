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
    res = []
    for boardingPass in boardingPasses:
        row, column = seatID(boardingPass)
        res.append(row * 8 + column)
    print(max(res))

main()
