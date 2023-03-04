n = int(input())

for i in range(n):
    data = input()
    result = []
    for j in range(len(data)):
        if data[j] == '<':
            if j+1 < len(data) and (data[j+1] == '<' or data[j+1] == '>'):
                continue
            if j+2 < len(data) and data[j+2] == '<':
                continue
            if j+2 < len(data) and data[j+2] == '>':
                result.append(data[j+1])
                # print(data[j+1], end=" ")
                continue
            if j+3 < len(data) and data[j+3] == '<':
                continue
            if j+3 < len(data) and data[j+3] == '>':
                result.append(data[j+1: j+3])
                # print(data[j+1: j+3], end=" ")
                continue
            if j+4 < len(data) and data[j+4] == '<':
                continue
            if j+4 < len(data) and data[j+4] == '>':
                result.append(data[j+1: j+4])
                # print(data[j+1: j+4], end=" ")
                continue
    if len(result) == 0:
        print("NONE")
    else:
        for item in result:
            if (item[0] != '0' or len(item) == 1):
                print(int(item), end=" ")
        print()


