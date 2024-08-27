def areaOfTriangle(base, height):
    area = 0.5*base*height
    return area
    
base, height = input().split()

res = areaOfTriangle(int(base),int(height))
print(res)