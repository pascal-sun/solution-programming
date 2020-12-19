import sys

FILENAME = sys.argv[1]

def parse():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
        timestamp = int(lines[0])
        IDs = []
        for ID in lines[1].split(','):
            if ID != 'x': IDs.append(int(ID))
    return timestamp, IDs 

def earliestBus(timestamp, ID):
    previous = timestamp // ID
    return (previous + 1) * ID

def main():
    timestamp, IDs = parse()
    departs = {}

    for ID in IDs:
        time = earliestBus(timestamp, ID)
        departs[time] = ID    
    
    nextBusTime = min(departs)
    nextBusID = departs[nextBusTime]
    print(nextBusID * (nextBusTime - timestamp))

main()
