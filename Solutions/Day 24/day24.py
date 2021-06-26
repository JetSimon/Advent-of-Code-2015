import itertools

def mul(a):
    s = 1
    for e in a:
        s *= e
    return s

f = open('input.txt','r')
gifts = []
for line in f:
    gifts.append(int(line.strip()))

weightNeeded = sum(gifts) / 4

for size in range(len(gifts)):
    combos = itertools.combinations(gifts, size)
    for combo in combos:
        combo = list(combo)
        if sum(combo) == weightNeeded:
            print( mul(combo)) 
            exit()