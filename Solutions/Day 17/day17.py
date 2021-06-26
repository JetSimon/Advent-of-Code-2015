def fill(jars, amount, combo, combos):
    if amount == 0:
        #print(combo)
        combos.append(";".join(sorted(combo)))
        return 1
    elif amount < 0:
        return 0
    
    filled = 0
    
    for i in range(len(jars)):
        if str(i) not in combo:
            jar = jars[i]
            comboCopy = combo[:]
            comboCopy.append(str(i))
            filled += fill(jars, amount - jar, comboCopy, combos)

    return filled

def getJars():
    f = open('input.txt','r')
    out = []
    for line in f:
        out.append(int(line.strip()))
    return out

ways = 0
jars = getJars()
combos = []

fill(jars, 150, [], combos)

#print(set(combos))
cm = list(set(combos))
print(cm)

smallest = 999
for c in cm:
    c = c.split(";")
    if len(c) < smallest:
        smallest = len(c)
amt = 0
for c in cm:
    c = c.split(";")
    if len(c) == smallest:
        amt += 1

print("there are", amt,"ways of size",smallest)