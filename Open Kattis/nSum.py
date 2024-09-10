def addition(n):
    sum = 0
    num = input().split()
    if len(num) != n:
        return None
    else:
        for number in num:
            sum += int(number)
    return sum

n = int(input())
print(addition(n))