import sys

def accumulatorValue(data):
    seen = set()
    pointer = 0
    val = 0
    while pointer != len(data):
        if pointer in seen:
            return False, val
        seen.add(pointer)
        operation, argument = data[pointer].split()
        if operation == 'nop':
            pointer += 1
        elif operation == 'acc':
            pointer += 1
            if argument[0] == '+':
                val += int(argument[1:])
            else:
                val -= int(argument[1:])
        elif operation == 'jmp':
            if argument[0] == '+':
                pointer += int(argument[1:]) 
            else:
                pointer -= int(argument[1:])
    return True, val

def corrected(data):
    print(data)
    res, val = accumulatorValue(data)
    if res:
        return val
    else:
        for i in range(len(data)):
            operation, argument = data[i].split()
            if operation == 'nop':
                tmp = data.copy()
                tmp[i] = 'jmp ' + argument 
                res, val = accumulatorValue(tmp)
                if res:
                    print(res, val)
                    print(tmp)
            elif operation == 'jmp':
                tmp = data.copy()
                tmp[i] = 'nop ' + argument
                res, val = accumulatorValue(tmp)
                if res:
                    print(tmp)
                    print(res, val)
            
def main():
    with open("input") as f:
        data = f.read().splitlines()
    
    corrected(data)

main()
