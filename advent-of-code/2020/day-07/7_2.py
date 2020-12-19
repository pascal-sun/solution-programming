import sys

def getGraph(data):
    graph = {}
    for rule in data:
        firstPart, secondPart = rule.replace('.', '').split('bags contain ')
        keyColor1, keyColor2 = firstPart.split()
        key = keyColor1 + ' ' + keyColor2
        vals = secondPart.split(', ')
        for val in vals:
            if val == 'no other bags':
                graph[key] = []
            else:
                num, valColor1, valColor2, _ = val.split()
                graph[key] = graph.get(key, []) + [(int(num), valColor1 + ' ' + valColor2)]
    return graph        

def numberBags(bags, graph):
    print(bags)
    if len(bags) == 0:
        return 1
    else:
        res = 0
        for bag in bags:
            print(bag)
            res += bag[0] * numberBags(graph[bag[1]], graph)
        print(res)
        return res

def main():
    with open('input1') as f:
        data = f.read().splitlines()
    graph = getGraph(data)
    for k,v in graph.items():
        print(k,v)
    print('---------------------')
    res = numberBags(graph['shiny gold'], graph)
    print(res)

main()
