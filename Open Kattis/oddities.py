def oddOrEven(arr):
    for index in range(len(arr)):
        if arr[index]%2==0:
            print(f'{arr[index]} is even')
        else:
            print(f'{arr[index]} is odd')
    
def acceptInputs(number):
    inputs = []
    for index in range(number):
        data = int(input())
        inputs.append(data)
    oddOrEven(inputs)
    
number = int(input())
acceptInputs(number)