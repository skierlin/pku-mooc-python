day = int(input())
result = [0 for i in range(3)]
for i in range(day):
    data = list(map(int, input().split()))
    result[0] += data[0]
    result[1] += data[1]
    result[2] += data[2]
print('%d %d %d %d' % (result[0], result[1], result[2], result[0]+result[1]+result[2]))
