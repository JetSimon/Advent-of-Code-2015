score = 0 

f = open('input.txt', 'r')
for line in f:
    raw = line.strip()
    l = len(raw) + 2
    l += raw.count('"')
    l += raw.count("\\")
    score += l - len(raw)
print(score)

    
