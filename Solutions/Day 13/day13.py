import itertools

def loadData():
    f = open('input.txt','r')
    out = {'you':Person("you")}
    for line in f:
        line = line.strip()
        name = line.split(" ")[0]
        mul = 1 if line.split(" ")[2] == "gain" else -1
        target = line.split("to ")[1].replace(".","")
        amt = int(line.split(" happiness")[0].split(" ")[3])
        if name not in out:
            out[name] = Person(name)
        out[name].pref[target] = amt * mul
    return out
class Person():
    def __init__(self,name):
        self.name = name
        self.pref = {}
    
    def __repr__(self):
        return str(self.pref)

people = loadData()
seating = list(people.keys())

best = 0
perms = list(itertools.permutations(seating))

def scoreSeating(seats):
    score = 0
    for i in range(len(seats)):
        before = people[seats[i-1]].name
        after = people[seats[(i+1)%len(seats)]].name
        person = people[seats[i]]

        if before in person.pref:
            score += person.pref[before]
        
        if after in person.pref:
            score += person.pref[after]
    return score

for perm in perms:
    best = max(scoreSeating(perm),best)

print(best)