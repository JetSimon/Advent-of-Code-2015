def loadData():
    aunts = []
    f = open('input.txt','r')
    for line in f:
        line = line.strip()
        name = line.split(":",1)[0]
        aunt = {'name':name}
        for pair in line.split(":",1)[1].strip().split(","):
            key = pair.split(":")[0].strip()
            val = int(pair.split(":")[1].strip())
            aunt[key] = val
        aunts.append(aunt)
    f.close()
    return aunts

def loadFilter():
    filters = {}
    f = open('filter.txt','r')
    for line in f:
        line = line.strip()
        key = line.split(":")[0]
        val = int(line.split(":")[1].strip())
        filters[key]=val
    return filters

aunts = loadData()
filters = loadFilter()
valid = aunts[:]

while len(valid) > 1:
    nextValid = []
    for aunt in aunts:
        add = True
        for filter in filters:
            if filter in ['cats','trees'] and filter in aunt and aunt[filter] < filters[filter]:
                add = False
                break
            elif filter in ['pomeranians','goldfish'] and filter in aunt and aunt[filter] > filters[filter]:
                add = False
                break
            elif filter not in ['cats','trees','pomeranians','goldfish'] and filter in aunt and filters[filter] != aunt[filter]:
                add = False
                break
        if add:
            nextValid.append(aunt)
    valid = nextValid
    print(valid)

print(valid)