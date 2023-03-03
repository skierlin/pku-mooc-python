n = int(input())
vec1 = list(map(int, input().split()))
vec2 = list(map(int, input().split()))

result = 0
for i in range(len(vec1)):
    result += vec1[i] * vec2[i]
print(result)