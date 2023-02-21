n = int(input())
result = 0
max_data = 0
for i in range(n):
    x, y = map(int, input().split())
    if 140 >= x >= 90 and 60 <= y <= 90:
        result += 1
    else:
        max_data = max(max_data, result)
        result = 0
max_data = max(max_data, result)
print(max_data)
