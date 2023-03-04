def isverse(tmp):
    for i in range(len(tmp)):
        if tmp[i] != tmp[len(tmp) - i - 1]:
            return False
    return True


data = input()

result = []

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        tmp_str = data[i:j+1]
        if isverse(tmp_str):
            result.append(tmp_str)

result.sort(key=len)
for i in result:
    print(i)
