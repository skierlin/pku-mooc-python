data = input()
result = 0
for i in range(len(data)):
    if '9' >= data[i] >= '0':
        result += 1

print(result)
