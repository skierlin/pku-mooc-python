import math
h, r = map(int, input().split())

barrel = 3.14*r*r*h

print(math.ceil(20000/barrel))