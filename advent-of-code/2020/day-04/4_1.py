import sys

def validPassport(passport):
    requiredFields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = { f.split(':')[0] for f in passport.split() }
    if len(requiredFields - fields) == 0:
        return True
    else:
        return False

def main():
    with open("input") as f:
        data = f.read()
    passports = data.split('\n\n')
    c = 0
    for i, passport in enumerate(passports):
        if validPassport(passport):
            c += 1
    print(c)
main()
