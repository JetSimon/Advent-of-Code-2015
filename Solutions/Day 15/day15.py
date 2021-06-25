c = [
    [5,-1,0,0,5],
    [-1,3,0,0,1],
    [0,-1,4,0,6],
    [-1,0,0,2,8]
]

best = 0

for i in range(0,100):
    for j in range(0, 100-i):
        for k in range(0,100-i-j):
            h = 100 - i - j - k
            a = c[0][0] * i + c[1][0] * j + c[2][0] * k + c[3][0] * h
            b = c[0][1] * i + c[1][1] * j + c[2][1] * k + c[3][1] * h
            d  = c[0][2] * i + c[1][2] * j + c[2][2] * k + c[3][2] * h
            e = c[0][3] * i + c[1][3] * j + c[2][3] * k + c[3][3] * h
            f = c[0][4] * i + c[1][4] * j + c[2][4] * k + c[3][4] * h

            if f != 500:
                continue

            score = a * b * d * e
            if a <= 0 or b <= 0 or d <= 0 or e <= 0:
                score =0
                continue
             #* f.
            best = max(score, best)

print(best)