import sys

FILENAME = sys.argv[1]

def parse():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines 

def createMemory(lines):
    currentMask = ''
    mem = {}
    for line in lines:
        action, value = line.split(' = ')
        if action == 'mask':
            currentMask = value
        else:
            indice = action[4:-1]
            res = int(value)
            for i, m in enumerate(currentMask):
                if m == '0':
                    res = res & ~2**(35 - i)
                elif m == '1':
                    res = res | 2**(35 - i)
            mem[indice] = res
    return mem

def main():
    lines = parse()
    mem = createMemory(lines)
    print(mem)
    print(sum(mem.values()))

main()
