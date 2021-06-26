import re

def loadData():
    data = {}
    f = open('input.txt','r')
    for line in f:
        line = line.strip()
        key = line.split(" => ")[0]
        val = line.split(" => ")[1]
        if key in data:
            data[key].append(val)
        else:
            data[key] = [val]
    f.close()
    return data
g = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
data = loadData()
ways = set()
count = 0
scores = set()

def step(seed, goal, depth):
    if len(scores) != 0 and depth > min(scores):
        return

    if seed == goal or len(seed) > len(goal):
        if len(scores) > 0 and depth < min(scores):
            print( min(scores))
        scores.add(depth)
        return

    one = False
    for e in data:
        matches = re.finditer(e, seed)
        for match in matches:
            one = True
            cp = seed
            index = match.span()[0]
            cp = cp[0:match.span()[0]] + cp[match.span()[1]:]
            for val in data[e]:
                cp2 = list(cp)
                cp2.insert(index, val)
                cp2 = "".join(cp2)
                step(cp2, goal, depth + 1)
    if not one:
        return

step("e", g, 0)
print(min(scores))