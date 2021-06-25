class Deer():
    def __init__(self,name,speed,time,rest):
        self.name = name

        self.speed = speed
        self.time = time
        self.moveTime = time

        self.maxCoolDown = rest
        self.coolDown = 0
        self.pos = 0

        self.score = 0

    def __repr__(self):
        return "pos: " + str(self.pos) + ", score:" + str(self.score)

    def tick(self):
        if self.coolDown == 0:
            self.moveTime = self.time

        if self.moveTime > 0:
            self.pos += self.speed
        elif self.moveTime == 0:
            self.coolDown = self.maxCoolDown

        self.moveTime -= 1
        self.coolDown -= 1
    

def loadData():
    out = {}
    f = open('input.txt','r')
    for line in f:
        line = line.strip()
        name = line.split(" ")[0]
        speed = int(line.split("fly ")[1].split(" ")[0])
        time = int(line.split("for ")[1].split(" ")[0])
        rest = int(line.split("rest for ")[1].split(" ")[0])
        out[name] = Deer(name, speed, time, rest)
    return out

deer = loadData()

for time in range(2503):
    for d in deer:
        deer[d].tick()
    best = 0
    bestDeer = None
    for d in deer:
        if deer[d].pos > best:
            bestDeer = deer[d]
            best = deer[d].pos
    bestDeer.score += 1

bestScore = 0

for key in deer:
    d = deer[key]
    bestScore = max(bestScore, d.score)

print(bestScore)