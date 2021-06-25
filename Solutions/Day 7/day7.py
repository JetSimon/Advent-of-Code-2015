commands = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
    stripped = line.rstrip()
    commands.append(stripped)

inputFile.close()

def ParseCommand(val, wires):
    if(val.isdigit()):
        return int(val)
    if("AND" in val):
        a = val.split("AND")[0].strip()
        b = val.split("AND")[1].strip()
        if((not a.isdigit() and a not in wires) or (not b.isdigit() and b not in wires)):
            return "NO"
        a = wires[a] if not a.isdigit() else int(a)
        b = wires[b] if not b.isdigit() else int(b)
        out = a & b
    elif("OR" in val):
        a = val.split("OR")[0].strip()
        b = val.split("OR")[1].strip()
        if((not a.isdigit() and a not in wires) or (not b.isdigit() and b not in wires)):
            return "NO"
        a = wires[a] if not a.isdigit() else int(a)
        b = wires[b] if not b.isdigit() else int(b)
        out = a | b
    elif("RSHIFT" in val):
        a = val.split("RSHIFT")[0].strip()
        b = int(val.split("RSHIFT")[1].strip())
        if((not a.isdigit() and a not in wires)):
            return "NO"
        a = wires[a] if not a.isdigit() else int(a)
        out = a >> b
    elif("LSHIFT" in val):
        a = val.split("LSHIFT")[0].strip()
        b = int(val.split("LSHIFT")[1].strip())
        if((not a.isdigit() and a not in wires)):
            return "NO"
        a = wires[a] if not a.isdigit() else int(a)
        out = a << b
    elif("NOT" in val):
        a = val.split("NOT")[1].strip()
        if((not a.isdigit() and a not in wires)):
            return "NO"
        a = wires[a] if not a.isdigit() else int(a)
        out = ~ a
    else:
        if(val in wires):
            return wires[val]
        return "NO"
    
    if(out < 0):
        out = 65536 + out
    
    if(out > 65535):
        out = out - 65535
    
    return out

def solve(commands):
    wires = {}


    executed = []


    while len(executed) != len(commands):
        for command in commands:
            
            if(command not in executed):
                val = command.split("->")[0].strip()
                target = command.split("->")[1].strip()
                parsed = ParseCommand(val, wires)

                if(parsed != "NO"):
                    executed.append(command)
                    wires[target] = parsed
                    #print(wires)

    return wires

def solve2(commands):
    wires = solve(commands)
    return wires['a']

print(solve2(commands))