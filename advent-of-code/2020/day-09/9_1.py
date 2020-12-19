import sys
from collections import deque

def findError(numbers, length):
    preamble = deque(numbers[:length])
    for i in range(length, len(numbers)):
        isCorrect = False
        for p in preamble:
            if abs(numbers[i] - p) in preamble:
                isCorrect = True
                break
        
        if isCorrect == False:
            return(numbers[i])

        preamble.append(numbers[i])
        preamble.popleft()

def findContiguous(numbers, error):
    smallest = 0 
    largest = 1
    s = numbers[smallest] + numbers[largest]
    while True:
        if s == error:
            return smallest, largest
        elif s < error:
            largest += 1
            s += numbers[largest]
        else:
            s -= numbers[smallest]
            smallest += 1

def main():
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().splitlines()))

    resPart1 = findError(data, int(sys.argv[2]))
    print(resPart1)
    
    resPart2 = findContiguous(data, resPart1)
    res = data[resPart2[0]:resPart2[1]+1]
    print(min(res)+max(res))

main()
