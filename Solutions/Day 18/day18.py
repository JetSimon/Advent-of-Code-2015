from copy import deepcopy

def getLit(grid):
    count = 0
    for row in grid:
        for p in row:
            if p == "#":
                count += 1
    return count

def loadGrid():
    grid = []
    f = open('input.txt','r')
    for line in f:
        grid.append(list(line.strip()))
    return grid

def printGrid(grid):
    for row in grid:
        print(row)
    print("\n")

def validPos(grid,y,x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

def getNext(grid, y , x):
    count = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dy == 0 and dx == 0 or not validPos(grid, y+dy, x+dx):
                continue
            if grid[y+dy][x+dx] == "#":
                count += 1
    return count

grid = loadGrid()
m=len(grid[0])-1
for step in range(100):
    grid[0][0] = "#"
    grid[0][m] = "#"
    grid[m][0] = "#"
    grid[m][m] = "#"
    nextGrid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid)):
            n = getNext(grid, y, x)
            pix = grid[y][x]
            if(pix == "#"):
                if n != 2 and n != 3:
                    nextGrid[y][x] = "."
            else:
                if n == 3:
                    nextGrid[y][x] = "#"
    grid = nextGrid
grid[0][0] = "#"
grid[0][m] = "#"
grid[m][0] = "#"
grid[m][m] = "#"
print(getLit(grid))