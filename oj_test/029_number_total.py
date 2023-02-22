l, r = input().split()
count = 0
for i in range(int(l),int(r)+1):
    for j in range(len(str(i))):
        if str(i)[j] == '2':
            count += 1
print(count)