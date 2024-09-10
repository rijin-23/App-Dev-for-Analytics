def winner(num):
    if num%2==0:
        return 'Bob'
    else:
        return 'Alice'
    
n = int(input())
print(winner(n))