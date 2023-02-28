data = input()

flag = False
for i in data:
    if data.count(i) == 1:
        flag = True
        print(i)
        break

if not flag:
    print("no")
