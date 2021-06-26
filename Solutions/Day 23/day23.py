def loadInst():
    out = []
    f = open('input.txt','r')
    for line in f:
        line = line.strip()
        out.append(line)
    return out


instructions = loadInst()
pos = 0
reg = {'a':1, 'b':0}

while pos < len(instructions):
    step = instructions[pos]
    command = step.split(" ")[0]
    if command == "hlf":
        key = step.split(" ")[1]
        reg[key] /= 2
    elif command == "tpl":
        key = step.split(" ")[1]
        reg[key] *= 3
    elif command == "inc":
        key = step.split(" ")[1]
        reg[key] += 1
    elif command == "jmp":
        off = int(step.split(" ")[1])
        pos += off
        continue
    elif command == "jie":
        off = int(step.split(" ")[2])
        key = step.split(" ")[1].replace(",","")
        if reg[key] % 2 == 0:
            pos += off
            continue
    elif command == "jio":
        off = int(step.split(" ")[2])
        key = step.split(" ")[1].replace(",","")
        if reg[key] == 1:
            pos += off
            continue
    pos += 1
print(reg)
