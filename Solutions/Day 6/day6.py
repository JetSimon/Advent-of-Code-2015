commands = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
    stripped = line.rstrip()
    commands.append(stripped)

inputFile.close()

def initGrid(xSize,ySize):
    grid = []
    for y in range(ySize):
        row = []
        for x in range(xSize):
            row.append(0)
        grid.append(row)
    return grid

def processCommand(grid, command):
    action = command.split(" ")[0] if command.split(" ")[0] == "toggle" else command.split(" ")[0] + " " + command.split(" ")[1]
    start = command.split(action)[1].split(" ")[1]
    end = command.split(action)[1].split(" ")[3]
    
    for y in range(int(start.split(",")[1]), int(end.split(",")[1])+1):
        for x in range(int(start.split(",")[0]), int(end.split(",")[0])+1):
            if(action == "turn off"):
                grid[y][x] = 0
            elif(action == "turn on"):
                grid[y][x] = 1
            if(action == "toggle"):
                grid[y][x] = 0 if grid[y][x] == 1 else 1

def processCommand2(grid, command):
    action = command.split(" ")[0] if command.split(" ")[0] == "toggle" else command.split(" ")[0] + " " + command.split(" ")[1]
    start = command.split(action)[1].split(" ")[1]
    end = command.split(action)[1].split(" ")[3]
    
    for y in range(int(start.split(",")[1]), int(end.split(",")[1])+1):
        for x in range(int(start.split(",")[0]), int(end.split(",")[0])+1):
            light = grid[y][x]
            if(action == "turn off"):
                grid[y][x] = light - 1 if light - 1 > 0 else 0
            elif(action == "turn on"):
                grid[y][x] = light + 1
            if(action == "toggle"):
                grid[y][x] = light + 2

def countOn(grid):
    count = 0
    for row in grid:
        count += row.count(1)
    return count

def countBrightness(grid):
    count = 0
    for row in grid:
        for light in row:
            count+=light
    return count

def solve(commands):
    grid = initGrid(1000,1000)

    amount = len(commands)
    doneAlready = 0
    
    for command in commands:
        processCommand(grid, command)
        doneAlready += 1
        #print(str((doneAlready/amount)*100) + "%")

    return countOn(grid)

def solve2(commands):
    grid = initGrid(1000,1000)

    amount = len(commands)
    doneAlready = 0
    
    for command in commands:
        processCommand2(grid, command)
        doneAlready += 1
        #print(str((doneAlready/amount)*100) + "%")

    return countBrightness(grid)

print(solve2(commands))