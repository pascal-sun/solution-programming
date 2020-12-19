import sys

def find2020(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]

def main():
    with open("input") as f:
        data = f.read()
    numbers = list(map(int,data.split()))
    print(find2020(numbers))

main()
