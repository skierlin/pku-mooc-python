data = input()
n = len(data)
flag = True
for i in range(n):
    if data[i] != data[n-1-i]:
        flag = False
        print("no")
        break

if flag:
    print("yes")
