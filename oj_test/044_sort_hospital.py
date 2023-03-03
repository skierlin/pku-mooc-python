n = int(input())

data1 = {}
data2 = {}

for i in range(n):
    num, age_str = input().split()
    age = int(age_str)
    if age >= 60:
        data2[num] = age
    else:
        data1[num] = age

sort_data = sorted(data2.items(), key=lambda x: x[1], reverse=True)
for num, age in sort_data:
    print(num)
for num, age in data1.items():
    print(num)