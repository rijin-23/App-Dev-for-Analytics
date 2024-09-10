def lastFactDigit(iteration,n):
    for num in n:
        if num>=5:
            print(0)
        else:
            if num==1:
                print(1)
            elif num==2:
                print(2)
            elif num==3:
                print(6)
            elif num==4:
                print(4)

iteration = int(input())
data = []
for index in range(iteration):
    inputs = int(input())
    data.append(inputs)

lastFactDigit(iteration, data)

