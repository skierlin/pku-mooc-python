n, m, k = map(int, input().split())
matrix_a = []
matrix_b = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))
for i in range(m):
    matrix_b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        result = 0
        for o in range(m):
            result += matrix_a[i][o]*matrix_b[o][j]
        print(result, end=" ")
    print()
