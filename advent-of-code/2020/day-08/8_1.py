import sys

def accumulatorValue(data):
    seen = set()
    pointer = 0
    val = 0
    while True:
        if pointer in seen:
            return val
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

def main():
    with open("input") as f:
        data = f.read().splitlines()
    print(accumulatorValue(data))

main()
