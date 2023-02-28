data = input()
res = ''
for i in range(len(data)):
    if 'a' <= data[i] <= 'z':
        print(data[i].upper(), end="")
    elif 'A' <= data[i] <= 'Z':
        print(data[i].lower(), end="")
    else:
        print(data[i], end="")