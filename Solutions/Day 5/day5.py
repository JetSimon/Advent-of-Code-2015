import re 


def passes(test):
    pattern = r"[aeiou]"
    pattern2 = r'(.)\1'
    first = len(re.findall(pattern, test ,re.MULTILINE)) >= 3
    second = re.search(pattern2, test ,re.MULTILINE) != None
    third = "ab" not in test and "cd" not in test and "pq" not in test and "xy" not in test
    return first and second and third

def passes2(test):
    chunks = []
    last=None
    for i in range(0,len(test),1):
        
        chunk = test[i:i+2]
        if(len(chunk) == 2):
            if(chunk != last):
                chunks.append(chunk)
            last=chunk if chunk != last else None
        #print(chunk)
    pairTest = len(set(chunks)) < len(chunks)

    repeatTest = False
    for i in range(0,len(test),1):
        chunk = test[i:i+3]
        if(len(chunk) == 3):
            if(chunk[0] == chunk[2]):
                repeatTest = True
    return pairTest and repeatTest
inputFile = open('input.txt', 'r') 

count = 0

for line in inputFile:
    stripped = line.rstrip()
    if passes2(stripped):
        count +=1

inputFile.close()

print(count)