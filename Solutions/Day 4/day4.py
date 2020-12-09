import hashlib
key = "bgvyzdsv"
num = 0

while True:
    e = "bgvyzdsv" + str(num)
    toHash = hashlib.md5(e.encode())
    hashed = toHash.hexdigest()
    if hashed[0:6] == "000000":
        print(num)
        break
    num+=1
