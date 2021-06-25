def lookSay(s, depth):
    if depth > 0:
        #print(s)
        out = ""
        
        current = s[0]
        amt = 1
        for i in range(len(s)-1):
            c = s[i]
            if  s[i+1] != current:
                out += str(amt) + current
                amt = 1
                current = s[i+1]
            else:
                amt += 1
        out += str(amt) + current
        return lookSay(out, depth - 1)
    else:
        return s

print( len(lookSay("1321131112", 50)))