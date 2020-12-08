dimensions = []
ribbons = []
inputFile = open('input.txt', 'r') 


for line in inputFile:
    stripped = line.rstrip()
    l = int(stripped.split("x")[0])
    w = int(stripped.split("x")[1])
    h = int(stripped.split("x")[2])
    surfaceArea = 2*l*w + 2*w*h + 2*h*l
    smallestSide = min([l*w,l*h,h*w])
    smallestPerim = min([l+l+w+w, h+h+w+w, l+l+h+h])
    ribbons.append(smallestPerim + (l*w*h))
    #dimensions.append( surfaceArea + smallestSide)

inputFile.close()

print(sum(ribbons))