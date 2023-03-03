m, n = map(int, input().split())
result = [[0 for i in range(n)] for j in range(m)]
# print(result)
data = []
for i in range(m):
    data.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            result[i][j] = data[i][j]
        else:
            result[i][j] = round((data[i][j]+data[i-1][j]+data[i+1][j]+data[i][j-1]+data[i][j+1])/5)
for i in range(m):
    for j in range(n):
        print(result[i][j], end=" ")
    print()
