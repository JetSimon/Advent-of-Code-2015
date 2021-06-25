data = ""
f = open('input.txt','r')

for line in f:
    data = eval(line.strip())

def sumChildren(e):
    if type(e) == int:
        return e

    count = 0
    if type(e) == list:
        for n in e:
            count += sumChildren(n)
        return count
    
    if type(e) == dict:
        for key in e:
            if e[key] == "red":
                return 0 
        for key in e:
            count += sumChildren(e[key])
        return count

    return 0



count = 0
for e in data:
    count += sumChildren(e)
print(count)