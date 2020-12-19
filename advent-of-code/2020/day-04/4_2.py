import sys
import re

def validPassport(passport):
    requiredFields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = { f.split(':')[0] : f.split(':')[1] for f in passport.split() }
    print(fields)
    valid = 0
    if len(requiredFields - fields.keys()) == 0:
        if re.search('^[0-9]{4}$', fields['byr']) and (1920 <= int(fields['byr']) <= 2002):
            valid += 1
        if re.search('^[0-9]{4}$', fields['iyr']) and (2010 <= int(fields['iyr']) <= 2020):
            valid += 1 
        if re.search('^[0-9]{4}$', fields['eyr']) and (2020 <= int(fields['eyr']) <= 2030):
            valid += 1 
        if fields['hgt'].endswith('cm') and (150 <= int(fields['hgt'][:-2]) <= 193):
            valid += 1
        if fields['hgt'].endswith('in') and (59 <= int(fields['hgt'][:-2]) <= 76):
            valid += 1
        if re.search('^#[0-9a-f]{6}$', fields['hcl']):
            valid += 1
        if re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', fields['ecl']):
            valid += 1
        if re.search('^[0-9]{9}$', fields['pid']):
            valid += 1
    
        print(valid)
        if valid == 7:
            return True
        else:
            return False
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
