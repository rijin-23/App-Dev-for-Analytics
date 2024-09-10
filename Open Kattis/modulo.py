def modulo(inputs):
    tracker = {}
    count = 0
    for num in inputs:
        if num%42 not in tracker:
            tracker[num%42] = 1
    for key in tracker:
        count+=1
    return count

i = 0
data = []
while i<10:
    n = int(input())
    data.append(n)
    i+=1
print(modulo(data))