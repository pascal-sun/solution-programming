import sys

def numbersYes(form):
    form = form.split()
    d = {}
    for line in form:
        for letter in line:
            d[letter] = d.get(letter,0) + 1
    res = 0
    for key, val in d.items():
        if val == len(form):
            res += 1
    return res

def main():
    with open("input") as f:
        data = f.read()
    forms = data.split('\n\n')
    res = 0
    for form in forms:
        res += numbersYes(form)
    print(res)
main()
