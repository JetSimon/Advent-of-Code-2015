from copy import deepcopy

class Location():
    def __init__(self,id):
        self.id = id
        self.dest = {}
    
    def __repr__(self):
        return str(self.dest)

    def addDest(self, id, score):
        self.dest[id] = score

    def goto(self, id):
        score = self.dest[id]
        return score

def readInput():
    out = {}
    f = open('input.txt', 'r')
    for line in f:
        raw = line.strip()
        origin = raw.split(" to ")[0]
        dest = raw.split(" to ")[1].split(" =")[0]
        score = int(raw.split(" = ")[1])
        
        if origin not in out:
            out[origin] = Location(origin)
        
        if dest not in out:
            out[dest] = Location(dest)
        
        out[origin].addDest(dest, score)
        out[dest].addDest(origin, score)

    return out
map = readInput()

print(map)
print("# nodes:",len(map))

best = [[0]]

def getShortest(current, map, visited, score):
    if current in visited:
        return 999999

    visited.append(current)
    #print(visited, score)
    if len(visited) >= len(map):
        return score

    best = 999999

    for dest in map[current].dest:
        s = map[current].goto(dest)
        att = getShortest(dest, map, visited[:], score + s)
        best = min(best, att)

    return best

def getLongest(current, map, visited, score):
    if current in visited:
        return 0

    visited.append(current)
    #print(visited, score)
    if len(visited) >= len(map):
        return score

    best = 0

    for dest in map[current].dest:
        s = map[current].goto(dest)
        att = getLongest(dest, map, visited[:], score + s)
        best = max(best, att)

    return best

for id in map:
    score = getLongest(id, deepcopy(map), deepcopy([]), 0)
    best[0][0] = max(score, best[0][0])

print(best)