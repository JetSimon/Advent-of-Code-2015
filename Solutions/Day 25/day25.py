seed = 20151125

goal = [2947, 3029]

def code(last, depth):
    code = last
    for i in range(1,depth):
        per = (i / (depth-1)) * 100
        if per % 1 == 0:
            print(per,"% done")
        code = (code * 252533) % 33554393
    return code

row = 1
col = 1
startRow = 1
counter = 1

# row <= 1 or set col to 1 and +1 starting col
while( [row, col] != goal ):
    counter += 1
    row -= 1
    col += 1
    if row < 1:
        startRow += 1
        row = startRow
        col = 1

print("translated to", counter )
print( "CODE:", code(seed, 17850354) )

