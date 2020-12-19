import sys

def checkPass(password):
    policy, pwd = password.split(':')
    policy, letter = policy.split()
    low, high = map(int,policy.split('-'))

    if low <= pwd.count(letter) <= high:
        return True
    else:
        return False 

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
