n = int(input())
data = list(map(int,(input().split())))

data.sort()

print(int(data[-1]) - int(data[0]))

