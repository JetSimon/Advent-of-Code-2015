commands = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
    stripped = line.rstrip()
    commands.append(stripped)
inputFile.close()

def solve(commands):
    totalLit = 0
    totalParse = 0
    for command in commands:
        passHex = False
        literalLength = len(command)
        parsedLength = literalLength - 2
        for i in range(1,len(command),1):
            if(passHex):
                passHex = False
            chunk = command[i:i+2]
            if(len(chunk) == 2 and not passHex):
                if(chunk[0] == "\\" and chunk[1] != "x"):
                    parsedLength-=1
                elif(chunk[0] == "\\" and chunk[1] == "x"):
                    parsedLength-=3
                    passHex = True
        totalLit = literalLength
        totalParse = totalParse
    return totalLit - totalParse
print(solve(commands))