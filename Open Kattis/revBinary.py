def revBinary(n):
    binary = bin(n)[2:]
    binary = binary[-1::-1]
    power = 0
    decimal = 0
    for digit in range(len(binary)-1,-1,-1):
        decimal += (2**power)*int(binary[digit])
        power+=1
    return decimal
    

n = int(input())
print(revBinary(n))