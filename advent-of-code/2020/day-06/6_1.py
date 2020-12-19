import sys

def numbersYes(form):
    form = form.split('\n')
    s = set()
    for line in form:
        for letter in line:
            s.add(letter)
    return len(s)

def main():
    with open("input") as f:
        data = f.read()
    forms = data.split('\n\n')
    res = 0
    for form in forms:
        res += numbersYes(form)
    print(res)

main()
