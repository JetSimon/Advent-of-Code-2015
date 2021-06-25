def inc(c):
    wrapped = False
    n = ord(c) + 1
    if n > 122:
        wrapped = True
        n -= 26
    return chr(n), wrapped

def generate(old):
    pos = len(old) - 1
    wrapped = True
    new = list(old)

    while wrapped:
        new[pos], wrapped = inc(new[pos])
        pos -= 1
        if pos < 0:
            pos = len(old) - 1

    new = "".join(new)
    return new

def straightThree(s):
    for i in range(len(s)-2):
        a = ord(s[i])
        b = ord(s[i+1])
        c = ord(s[i+2])
        if a == b - 1 and b == c - 1:
            return True
    return False

def noBadLetters(s):
    return 'i' not in s and 'o' not in s and 'l' not in s

def twoPairs(s):
    pairs = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            pairs.append(s[i])
    return len(set(pairs)) >= 2

def valid(s):
    return noBadLetters(s) and straightThree(s) and twoPairs(s)

password = "cqjxxyzz"
first = True
while first or not valid(password):
    first = False
    password = generate(password)
print(password)