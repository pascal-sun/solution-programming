import sys

def checkPass(password):
    policy, pwd = password.split(': ')
    policy, letter = policy.split()
    low, high = map(int,policy.split('-'))
    print(pwd, letter, low, high, pwd[low-1], pwd[high-1])    
    s = 0
    if pwd[low - 1] == letter:
        s += 1
    if pwd[high - 1] == letter:
        s += 1

    return s == 1

def main():
    with open("input") as f:
        data = f.read()
    passwords = data.split('\n')
    c = 0
    for password in passwords[:-1]:
        print(password)
        if checkPass(password):
            c += 1
    print(c)

main()
