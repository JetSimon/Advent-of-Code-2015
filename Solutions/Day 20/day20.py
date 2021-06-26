from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


goal = 34000000
start = 500000
end = int(goal/10)

cache = {}

for i in range(start, end):
    per = (i / end) * 100
    if per % 1 == 0:
        print(per,"% done")

    pres = 0

    fac = factors(i)
    
    for f in fac:
        if i/f <= 50:
            pres += f * 11

    cache[i] = pres
    #print(pres)

    if pres >= goal:
        print(i, " has ", pres)
        break

#print(cache)
