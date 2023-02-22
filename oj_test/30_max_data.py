b, a  = map(int, input().split())
result = 0
while a%b != 0:
    a, b = b, a%b

print(b)