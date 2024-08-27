def findR2(r1,s):
    r2 = 2*s-r1
    return r2

r1,s = input().split()

res = findR2(int(r1),int(s))
print(int(res))