import math
data, y = input().split()

res = 8

if int(data) > 1000 :
    res += (math.ceil((int(data)-1000) / 500))*4

if y == 'y':
    res += 5

print(res)
