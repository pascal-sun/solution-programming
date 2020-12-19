import sys

def jolts(data):
    data.append(0)
    data.append(max(data)+3)
    data = sorted(data)
    wahid = 0
    thalatha = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff == 1:
            wahid += 1
        elif diff == 3:
            thalatha += 1
    return wahid, thalatha 

def arrangement(data):
    



def main():
    with open('input') as f:
        data = list(map(int, f.read().splitlines()))
    print(data)
    wahid, thalatha = jolts(data)
    print(wahid * thalatha)

main()

